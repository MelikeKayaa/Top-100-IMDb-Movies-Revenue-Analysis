# kullanacağımız kütüphanleri import edelim.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# veri setini yükleyelim.
df = pd.read_csv(r'C:\Users\kayam\OneDrive\Masaüstü\Filmler python projesi\movies.csv')

print(df.head()) # veriye genel bakış
print(df.columns) # sütun adlarına bakış: numara,film adı,yayın yılı, kategori,çalışma süresi,tür,imdb puanı,oylar,genel toplam
print(df.shape) # satır-sütun sayısı
print(df.info()) # verimize daha detaylı bakalım
print(df.isnull().sum()) # eksik veri var mı diye kontrol edelim. 1. tane varmış.
print(df['gross_total'].head(68)) # eksik değerin olduğu sütuna bakalım.

# eksik değerin yerine sütunun medyan değerini girecektik ama yazı tipinde olduğu için ilk önce düzenleme yapacağız.

# dolar işaretlerini kaldırıp onların yerine boşluk koyacağız.
df['gross_total'] = df['gross_total'].str.replace('$','', regex=False) # regex= false; dolar işareti özel karakter ama biz onu düz metin olarak ele alıp değiştireceğiz. o yüzden false yazdık.

# şimdi de milyonun M harfine aynı işlemi yapacağız.
df['gross_total'] = df['gross_total'].str.replace('M','',regex=False)

# şimdi yazıları sayıya çevireceğiz.
df['gross_total'] = pd.to_numeric(df['gross_total'],errors='coerce') # pd.to_numeric: string olan sayıları yazıya çevirir(float), errors='coerce' ifadesi yazıya çevrilemeyen değerleri NaN (eksik) yapar.

# şimdi de eksik değerin olduğu sütunun medyanına bakalım.
ort = df['gross_total'].median()
print('ortalama gross_total: ',ort)

# medyanı eksik değerin olduğu yere atayalım.
df.loc[df['gross_total'].isnull(), 'gross_total'] = ort

# atamayı doğru yaptık mı diye kontrol edelim.
print(df['gross_total'].isnull().sum())
print(df['gross_total'].head(70))

# en yüksek gişe hasılatı yapan film hangisi ?
print(df[df['gross_total'] == df['gross_total'].max()])

# ortalama gişe gelirinin üstünde kazanan filmler neler ?
ortalama = df['gross_total'].mean()
print(df[df['gross_total'] > ortalama])

# en yüksek gişe parasına sahip filmler nelerdir? grafik ile görelim.
df_shorted = df.sort_values(by='gross_total',ascending=False) # gross_totale göre büyükten küçüğe sıralama yapılır ve yeni bir değişkene atanır.

# ilk 10 değeri aldık.
top10 = df_shorted.head(10)

# bu 10 değerin film isimleri ve gişe paralarını gösterdik.
print(top10[['movie_name','gross_total']])

# grafikte okunurluğu artırmak için film isimlerini biraz kısaltacağız.
kisaltilmis_isimler = top10['movie_name'].str.slice(0,20)
print(kisaltilmis_isimler)

# grafiği oluşturalım.
plt.figure(figsize=(12,6))
plt.bar(kisaltilmis_isimler,top10['gross_total'])
plt.title('En Yüksek Gişe Hasılatına Sahip 10 Film')
plt.xlabel('Film Adı')
plt.ylabel('Gişe Hasılatı (Milyon $)')
plt.xticks(rotation=45,ha= 'right') # yazılar üst üste binmesin diye açılarını ve yönlerini azıcık değiştirdik.
plt.tight_layout() # yazılar grafiğin dışına taşmasın diye
plt.show()

# imdb puanı ile gişe hasılatı arasındaki ilişkiyi inceleyelim.
plt.figure(figsize=(10,6))
plt.scatter(df['imdb_rating'], df['gross_total'])
plt.title('IMDb Puanı vs Gişe Hasılatı')
plt.xlabel('IMBd Puanı')
plt.ylabel('Gişe Hasılatı (Milyon $)')
plt.grid(True)
plt.show()

# Yaş sınırlamasına göre filmlerin ortalama gişe hasılatını hesaplayıp görselleştirelim
category_gross = df.groupby('category')['gross_total'].mean().sort_values(ascending=False)
plt.figure(figsize= (10,6)) # grafik figürün genişliği 10 yüksekliği 6
sns.barplot(x= category_gross.index, y=category_gross.values) # çubuk grafik x ekseninde yaş sınırlamaları , y ekseninde her kategorinin gişe ortalaması olacak
plt.title('Yaş Sınırlamasına Göre Ortalama Gişe Hasılatı')
plt.xticks(rotation= 45, ha='right')
plt.ylabel('Ortalama Gişe Hasılatı ($)')
plt.show()

print(df['category'].unique()) # kategori değişkenindeki benzersiz değerlere baktık.

# --- KATEGORİ DEĞİŞKENİNDEKİ DEĞERLERİN ANLAMLARI ---

# R = Restricted → 17 yaş altı ebeveynle izlemeli. Şiddet, küfür, cinsellik olabilir.
# PG = 	Parental Guidance Suggested → Ebeveyn rehberliği önerilir. Küçük çocuklar için bazı içerikler uygun olmayabilir.
# PG-13 = Parents Strongly Cautioned → 13 yaş altı için uygun olmayabilir. Biraz şiddet, argo veya cinsellik olabilir.
# Passed = Eski filmlerde kullanılan bir terim. Film Hays Code'dan (eski bir sansür sistemi) geçtiği anlamına gelir.
# Approved = 1930'lar–1960'lar arası kullanılan eski sistemin etiketi.
# G = General Audiences → Her yaşa uygun. Hiçbir sakıncalı içerik yok.
# GP = 	Eski bir versiyon. 1970’lerde kısa bir süre kullanıldı, sonradan PG’ye dönüştürüldü.

# Türlerine göre filmlerin ortalama gişe hasılatını hesaplayıp görselleştirelim
genre_gross = df.groupby('genre')['gross_total'].mean().sort_values(ascending=False)
plt.figure(figsize=(16,9))
sns.barplot(x=genre_gross.index, y= genre_gross.values)
plt.title('Türlerine Göre Filmlerin Ortalama Gişe Hasılatı')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Ortalama Gişe Hasılatı (Milyon $)',fontsize= 15)
plt.xlabel('Türler',fontsize=15)
plt.tight_layout()  # yazıların grafik dışında kalmasını engellemek için kullandık.
plt.show()

# en verimli kategoriler - ımdb & gişe karşılaştırması
genre_performance = df.groupby('genre')[['imdb_rating', 'gross_total']].mean().sort_values(by='imdb_rating', ascending=False)
print(genre_performance)

# Yıllara göre gişe hasılatındaki değişikliklere bakalım
yearly_gross = df.groupby('year_of_release')['gross_total'].mean().sort_index()
plt.figure(figsize=(18,9))
sns.lineplot(x=yearly_gross.index, y=yearly_gross.values,marker='o')
plt.title('Yıllara Göre Ortalama Gişe Hasılatı')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Yıl',fontsize=15)
plt.ylabel('Ortalama Gişe Hasılatı (Milyon $)',fontsize=15)
plt.grid(True)
plt.tight_layout()
plt.show()
