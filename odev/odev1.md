** SORU: **
abc dizini altında a b ve c isimli klasörler oluştur. Bu klasörlerin altına sırası ile 1, 2 ve 3 isimli dosyalar oluştur../abc
 > ./abc/a
  ./abc/a/1
  ./abc/c
  ./abc/c/3
  ./abc/b
  ./abc/b/2
Daha sonra ./abc/a ve ./abc/b dizininde bulunan sırası ile 1 ve 2 isimli dosyaları c dizinine taşı
  ./abc
  ./abc/a
  ./abc/c
  ./abc/c/1
  ./abc/c/3
  ./abc/c/2
  ./abc/b

** CEVAP ve AÇIKLAMALAR: **
mkdir abc #abc adinda bir klasor olusturdum.
cd abc #abc klasorune girdim.
mkdir a b c #bu komut a,b,c adinda uc yeni klasor olusturur.
ll abc #abc klasorunu listelemek icin kullandim.
touch a/1 #a klasorunun icine 1 isimli dosya olusturdum.
touch b/2 #b klasorunun icine 2 isimli dosya olusturdum.
touch c/3 #c klasorunun icine 3 isimli dosya olusturdum.
ls a #a klasorunu listeledim.
ls b #b klasorunu listeledim.
ls c #c klasorunu listeledim.
mv a/1 c/ #a klasorundeki 1 dosyasini c klasorune tasidim.
mv b/2 c/ #b klasorundeki 2 dosyasini c klasorune tasidim.
ls c #c klasorunu listelemek icin ls komutunu kullandim.

ALTERNATİG ÇÖZÜM
mkdir -p ./abc/{a,b,c} # abc dizini olmasa bile bir tane oluşturur ve altına a, b ve c dizinlerini oluşturur
touch abc/a/1 abc/b/2 abc/c/3  | 1,2 ve 3 dosyalarını sırası ile a, b ve c dizileri altında oluşturur.
mv abc/a/1 abc/b/2 abc/c/ 


