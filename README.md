# mail gonderen keylogger
 keylogları mail ile gönderen program
Keylogger, klavye dinleme programıdır. Klavyeden basılan tuşlar dinlenerek bir  dosyaya kaydedilir ve kötü niyetle kullanılabilir. Genellikle şifre tahmini için kullanılır.

Bu projede klavyeden basılan tuşlar dinlerek bir dosyaya kaydedilmiş ve dosya mail ile gönderilmiştir.Proje için yapılması gerekenler şuanlardır;

Klavye dinlemek için pynput kütüphanesi projeye eklenmelidir.
Mail göndermek için smtplib kütüphanesi, maile dosya eklemek için MIME kütüphaneleri eklenmelidir.
myMailadress kısmına gönderenin mail adresi, password kısmına gönderenin mail adresini şifresi girilmelidir.
sendTo kısmına mailin gönderileceği mail adresi girilmelidir.
Projeyi çalıştırmadan önce gönderici mailine giriş sağlanabilmesi için hesap ayarlarından güvenliği düşük uygulama erişimine izin verilmelidir.

 Şu linkten izin kısmına ulaşabilirsiniz : https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Mu79lBKIpRQvxt3GkxzFJgG07yGVR1GdneweG7BS9wMeBdZDhzdbGhYkUUa9GiQEJmMIWRi_JrwE8lQ_WL_e-16Hia2w

Loglar  ‘logs.txt’ text dosyasında toplanacağı için önceden projeye logs.txt adlı text dosyası eklenmelidir. Çünkü dosya “append” ile açılıyor koda göre. Eğer logs.txt adında bir dosya oluşturmadan proje çalıştırılıcaksa dosya “write” ile açılmalıdır, sonra bir kez çalıştırılıp dosya oluştuktan sonra “append” ile değiştirilmelidir.
