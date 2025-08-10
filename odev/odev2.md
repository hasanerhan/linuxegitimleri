**SORU:**


> - odev1 dosyas??ndaki ./abc/c klas??r??nde bulunan 1 dosyan??n kullan??c?? ve izin durumalar??n?? g??ster. ve a????klay??c?? bilgi yaz. ??rne??in x dosyas??n??n kullanc??s?? irmak grubu wheel ve irmak kullan??c??s??n??n izni okuma, yazma ve ??al????t??rma vb. 


> - 1 nolu dosyanin  izin durumalar??n?? kullan??c?? i??in sadece okuma grup i??in sadece yazma ve di??erleri i??in hi?? izin vermeyecek duruma getir.


> - 2 nolu dosyanin izin durumlarini kullanici okuma ve yazma, grup yazma ve calistirma, diger okuma ve calistirma


**CEVAP ve A??IKLAMALAR:**


> ll ./abc/c/1 


<<<<<<< HEAD
<<<<<<< HEAD:odev/odev2.md
-rw-r--r-- 1 irmakguney staff 0 A??u 10 18:30 ./abc/c/1 


en bastaki dosya tipi ve izinleridir.??lk karakter - dosya tipidir - bir dosya oldugunu d ise bir klasor oldugunu gosterir.rw- dosyanin sahibinin izinleridir.(r)okuma izni vardir,(w)yazma izni vardir,(-)calistirma izni yoktur.rw- dosyanin sahibinin izinleridir.r-- dosyanin ait oldugu grubun izinleridir,r-- diger kullanicilarin izinleridir.(./abc/c/1)dosyanin adidir.irmakguney:dosyanin sahibi olan kullanici adidir.0:Dosyanin boyutudur.ait oldugu grubun ismi staff.


> chmod 420 ./abc/c/1   chmod komutu bir dosyanin izinlerini degistirmeye yarar 420 ise dosyanin yeni izinlerini sayisal olarak belirler.4:okuma(r),2:yazma(w)1:calistirma(x).4 
=======
bu komut belirtilen dosyanin ozelliklerini,dosya turunu,izinlerini,sahibini,grubunu,boyutunu,son degistirilme tarihini ve adini listeledi.


-rw-r--r-- 1 irmakguney staff 0 Ağu 10 18:30 ./abc/c/1 


en bastaki dosya tipi ve izinleridir.İlk karakter - dosya tipidir - bir dosya oldugunu d ise bir klasor oldugunu gosterir.rw- dosyanin sahibinin izinleridir.(r)okuma izni vardir,(w)yazma izni vardir,(-)calistirma izni yoktur.rw- dosyanin sahibinin izinleridir.r-- dosyanin ait oldugu grubun izinleridir,r-- diger kullanicilarin izinleridir.(./abc/c/1)dosyanin adidir.irmakguney:dosyanin sahibi olan kullanici adidir.0:Dosyanin boyutudur.ait oldugu grubun ismi staff.



chmod 420 ./abc/c/1 


chmod komutu bir dosyanin izinlerini degistirmeye yarar 420 ise dosyanin yeni izinlerini sayisal olarak belirler.4:okuma(r),2:yazma(w)1:calistirma(x).4 
>>>>>>> a5f8a56 (odev2 duzeltme)


> (kullanici): sadece okuma izin verir.2(grup):sadece yazma izni verir. 0(digerleri):hicbir izin vermez.


<<<<<<< HEAD
chmod 635 ./abc/c/2   bu komut sayesinde 2 nolu dosyanin izinlerini degistirecegiz chmod komutuna verdigimiz 635 sayisi,dosyanin yeni izinlerini belirler.6:(kullanici icin)= okuma ve yazma izni verir.3:(grup icin)yazma ve calistirma izni verir.5(digerleri icin):okuma ve calistirma izni verir.
=======
CEVAP ve A??IKLAMALAR:
> ll ./abc/c/1   bu komut belirtilen dosyanin ozelliklerini,dosya turunu,izinlerini,sahibini,grubunu,boyutunu,son degistirilme tarihini ve adini listeledi.


> -rw-r--r-- 1 irmakguney staff 0 A??u 10 18:30 ./abc/c/1 

en bastaki dosya tipi ve izinleridir.


> ??lk karakter - dosya tipidir - bir dosya oldugunu d ise bir klasor oldugunu gosterir.


> rw- dosyanin sahibinin izinleridir.


> (r)okuma izni vardir,(w)yazma izni vardir,(-)calistirma izni yoktur.


> rw- dosyanin sahibinin izinleridir.r-- dosyanin ait oldugu grubun izinleridir,r-- diger kullanicilarin izinleridir.


> (./abc/c/1)dosyanin adidir.


> irmakguney:dosyanin sahibi olan kullanici adidir.


> 0:Dosyanin boyutudur.


> ait oldugu grubun ismi staff.


> chmod 420 ./abc/c/1   chmod komutu bir dosyanin izinlerini degistirmeye yarar 420 ise dosyanin yeni izinlerini sayisal olarak belirler.


> 4:okuma(r),2:yazma(w)1:calistirma(x).4 
(kullanici): sadece okuma izin verir.


> 2(grup):sadece yazma izni verir. 0(digerleri):hicbir izin vermez.


> chmod 635 ./abc/c/2   bu komut sayesinde 2 nolu dosyanin izinlerini degistirecegiz chmod komutuna verdigimiz 635 sayisi,dosyanin yeni izinlerini belirler.


> 6:(kullanici icin)= okuma ve yazma izni verir.


> 3:(grup icin)yazma ve calistirma izni verir.


> 5(digerleri icin):okuma ve calistirma izni verir.
>>>>>>> a3d90b0 (I've updated the project.):odev/odev2
=======
chmod 635 ./abc/c/2 


bu komut sayesinde 2 nolu dosyanin izinlerini degistirecegiz chmod komutuna verdigimiz 635 sayisi,dosyanin yeni izinlerini belirler.6:(kullanici icin)= okuma ve yazma izni verir.3:(grup icin)yazma ve calistirma izni verir.5(digerleri icin):okuma ve calistirma izni verir.
>>>>>>> a5f8a56 (odev2 duzeltme)





