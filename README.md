# Web Dizin Tarayıcı (Directory Buster)

Siber güvenlik ve web teknolojilerine olan ilgimden dolayı, hazır araçların arka planda nasıl çalıştığını anlamak için geliştirdiğim bir Python scriptidir.

Projenin Amacı
Web sitelerinde linki paylaşılmamış olsa bile sunucuda var olan "gizli" klasörleri veya dosyaları (örn: admin panelleri, unutulmuş yedek dosyaları) tespit etme mantığını kavramaktır. "Security by Obscurity" kavramının neden yetersiz olduğunu uygulamalı olarak görmek için bu aracı kodladım.

Nasıl Çalışıyor?
Script, kullanıcıdan bir hedef URL ve bir kelime listesi (wordlist) alır. Listedeki her kelimeyi hedef URL'in sonuna ekleyerek (Örn: site.com/admin) siteye HTTP GET istekleri gönderir.
- Eğer sunucu "200 OK" yanıtı verirse, o dizinin var olduğu anlaşılır ve ekrana yazdırılır.
- "403 Forbidden" yanıtları da dosyanın var olduğunu ama iznimiz olmadığını gösterdiği için raporlanır.
- "404 Not Found" yanıtları ise görmezden gelinir.

- Python 3
- Requests Kütüphanesi 

Kullanım
1. "wordlist.txt" adında bir dosya oluşturun ve içine denenecek kelimeleri (admin, login, test vb.) alt alta yazın.
2. Terminalden scripti çalıştırın:
   python buster.py http://[SITENIZ].com

Yasal Uyarı
Bu araç tamamen eğitim amaçlıdır ve sadece izinli olunan sistemlerde (kendi yerel sunucunuzda veya test sitelerinde) kullanılmalıdır. 

Emircan Bingöl
