#!/bin/python
#SAFA BAYAR  Ogrenci No: 161906001
#calistirmak icin: 'mpiexec -n 4 python Hamming.py '
from random import randint
from mpi4py import MPI		#Kutuphane tanimlamalari

comm = MPI.COMM_WORLD
rank = comm.Get_rank() 		#Paralellestirmek icin kutuphanedekileri degisken olarak ataniyor.
size = comm.Get_size()

sum=0		#Degiskenlerin sifirlanmasi ve tanimlanmasi asamasi.
a = []
b = []			#a ve b nin bos array tanimlanmasidir.
z = randint(0,10000)	#0 ile 10000 arasinda rastgele deger uretmektedir.
def randos():		#randos adinda fonksiyon tanimlanmakta.
    for rast in range(0,z):		#rastgele aralikta dizi olustutmasi asamsi range in amaci siralamadir. 
        k = randint(0,1)	#k ve l degiskenine rastgele 0 1 araliginda deger olusturmaktadir.
        l = randint(0,1)
        a.append(k)		#append veri yapilarinda array e integer eklemek icin kullaniliyor.
        b.append(l)

    p = 0			
    for pos in range(0,z):		#rastgele olusan arraylerin icinde gezinebilmek icin for dongusu ve range methodu
        if a[pos] != b[pos]:	#degerlerin farkil oldugu yer de asagidaki yazi yazdirilacak.
            #print  pos ,'degerinde esit degildir a degeri ' ,a[pos] ,'b degeri' ,b[pos]
            p += 1		#sayac tutulmasi nedeni toplam kac tane esit olmayan deger oldugunu tutmak

    print 'Hamming mesafesi ' , p	#sayac sayesinde hamming mesafesi tutulmakta.


if rank ==0:				#sifirinci  yani main cekirdek atatigimiz degere gelince asagidakini uygula anlamina geliyor. 
    for i in range(1,size):		#size degiskeni yukarda kac cekirdege sahip oldugumuzu gosterir. 
        data = randos()		#fonksiyonu degiskene atiyoruz. mpi'da parametre olarak fonksiyon kullanamamaktayiz. 
        sum = comm.recv(source=i)	#sum degeri butun cekirdeklere dagitilan islemin sonucudur.
                
else:
        sum = randos()			#eger cekirdeklere dagitilmiyor ise sifirinci yani main cekirdekte islemin yapilmasini belirtmekte
        comm.send(sum, dest=0)

