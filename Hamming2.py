#import multiprocessing
from random import randint
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

class slist(list):
    @property
    def length(self):
        return len(self)

def hamming(x, y):
    dist = 0;

    if(x != y):
        dist=1

    return dist

def control(array1,array2,totalprocess):
    result=0
    for i in range(0,totalprocess):
        result += hamming(array1[i],array2[i])
    print(result)


if __name__ == "__main__":  # confirms that the code is under main function
    sum = 0
    a=[]
    b=[]
    i=0
    number = 100
    totalprocess = number
    #
    # pool = multiprocessing.Pool(totalprocess)
    #
    tasks=[]

    array1 = slist(range(number))
    array2 = slist(range(number))

    num1 = 0
    num2 = 0
    i = 0
    result=0
    while i < totalprocess:
        num1 = randint(0,1)
        array1[i] = num1
        num2 = randint(0,1)
        array2[i] = num2
        i += 1
        tasks.append((num1,num2))




    if rank == 0:				#sifirinci  yani main cekirdek atatigimiz degere gelince asagidakini uygula anlamina geliyor.
        for i in range(1,size):		#size degiskeni yukarda kac cekirdege sahip oldugumuzu gosterir.

            data = control(array1,array2,totalprocess)		#fonksiyonu degiskene atiyoruz. mpi'da parametre olarak fonksiyon kullanamamaktayiz.
            sum = comm.recv(source=i)	#sum degeri butun cekirdeklere dagitilan islemin sonucudur.
    else:
        sum = control(array1,array2,totalprocess)		#eger cekirdeklere dagitilmiyor ise sifirinci yani main cekirdekte islemin yapilmasini belirtmekte
        comm.send(sum, dest=0)





        #########################################
    # results = [pool.apply_async(hamming, t) for t in tasks]
    #
    # distance = 0
    # for result in results:
    #     distance += result.get()
    #     pool.close()
    #     pool.join()
    #
    # for var in range (0,number):
    #     print array1[var],
    # print('\n')
    # for var in range (0,number):
    #     print array2[var],
    # print('\n')
    # print("Distance: %d" %distance)
