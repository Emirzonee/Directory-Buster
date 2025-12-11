import requests
import sys
import os

def banner():
    print("-" * 50)
    print("🕵️  PYTHON WEB DIRECTORY BUSTER")
    print("-" * 50)

def dir_buster(target_url, wordlist_file):
    # Dosya var mi kontrol et
    if not os.path.exists(wordlist_file):
        print(f"[!] HATA: '{wordlist_file}' dosyasi bulunamadi!")
        sys.exit()

    print(f"[+] Hedef: {target_url}")
    print(f"[+] Wordlist: {wordlist_file}")
    print("-" * 50)

    # Dosyayi satir satir oku
    with open(wordlist_file, "r") as file:
        for line in file:
            word = line.strip() # Satir sonundaki bosluklari temizle
            full_url = f"{target_url}/{word}"
            
            try:
                # Siteye istek at (Request)
                response = requests.get(full_url, timeout=3)
                
                # HTTP Kodlarini Kontrol Et
                if response.status_code == 200:
                    print(f"[+] BULUNDU (200): {full_url}")
                elif response.status_code == 403:
                    print(f"[!] YASAKLI (403): {full_url}")
                # 404 (Bulunamadi) hatalarini bilerek yazdirmiyoruz, ekrani kirletmesin.
                
            except requests.exceptions.ConnectionError:
                pass # Baglanti hatasi olursa gec
            except KeyboardInterrupt:
                print("\n[!] Islem iptal edildi.")
                sys.exit()

if __name__ == "__main__":
    banner()
    
    if len(sys.argv) < 2:
        print("Kullanim: python buster.py <hedef_url>")
        print("Ornek: python buster.py http://testphp.vulnweb.com")
        sys.exit()
    
    target = sys.argv[1]
    wordlist = "wordlist.txt"
    
    dir_buster(target, wordlist)