# IMDB TOP 100 Film Analizi Projesi

## Proje Özeti 

Bu projede, farklı yıllarda vizyona giren filmlerin gişe hasılatları incelendi. Amaç, türlere, yaş sınıflandırmalarına ve yıllara göre gişe gelirlerindeki değişimleri görmekti. Veriler üzerinde temizlik, eksik değerlerle başa çıkma ve görselleştirme adımları uygulandı.


## Veri Seti

Bu projede kullanılan veri seti Kaggle platformundan alınmıştır. Veri seti IMDb tarafından tüm zamanların en yüksek puan alan filmlerinin listesini içermektedir. Listedeki filmler 1972-2015 yılları arasındaki filmlerden oluşmaktadır.

https://www.kaggle.com/datasets/themrityunjaypathak/imdb-top-100-movies


## Kullanılan Teknolojiler 

- Python
- Pandas
- Matplotlib
- Seaborn
- PyCharm( geliştirme ortamı )


## Veri Ön İşleme

- Eksik veriler belirlendi uygun şekilde temizlendi
- Aykırı değerlerin etkisini azaltmak için ortalama yerine medyan kullanıldı.( Ortalama: 117.42653 -  Medyan: 68.77)
- Değişken isimleri sadeleştirildi ve anlamlı hale getirildi.
- Kategorik değişkenlerdeki benzersiz sınıflar incelendi


## Keşifsel Veri Analizi (EDA)

- En yüksek gişe hasılatına sahip türler ve yaş sınıflandırmaları incelendi.
- Yıllara göre ortalama gişe geliri analiz edildi.
- En verimli kategoriler incelendi.
- IMDb puanı ile gişe hasılatı arasındaki ilişki incelendi.( IMDb puanı yüksek olan her filmin gişede de yüksek gelir elde edemediği görüldü.)
- Belirli yılarda düşüşler / gelişmeler olduğu tespit edildi.


## Öne Çıkan Bulgular

- PG-13 ve PG gibi sınıflandırmalar, daha yüksek gişe gelirine sahip olabiliyor.
- Action, Adventure ve Animation türleri genel olarak daha yüksek gelir elde etmiş.
- Gişe hasılatında yıllara göre dalgalanmalar mevcut ama genel olarak artan bir eğilim görülüyor.
- IMDb puanı yüksek olan her film her zaman yüksek gişe başarısı göstermemektedir. Bu da eleştirmen beğenisi ile ticari başarının her zaman paralel gitmediğini ortaya koymaktadır.


## Projeyi Çalıştırmak için

1. Python yüklü olmalı
2. Kullanılan teknolojilerdeki kütüphaneler kurulmalı
3. Veri seti dosyası proje ile aynı dizinde olmalı
4. Proje çalıştırılarak analizler incelenebilir.


## Sonuç

Veri görselleştirme ve analizle, sinema sektörünün bazı dinamiklerini daha net görmek mümkün oldu. Bu tarz çalışmalar hem veri analizi becerilerini geliştiriyor hem de gerçek dünyadaki verileri yorumlama açısından çok faydalı oluyor.


















