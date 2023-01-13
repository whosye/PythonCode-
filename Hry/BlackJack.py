from random import randrange 
MAX = 21
MAX_K = 11
A =  randrange(1,MAX_K) 
print('Celková hodnota je:' + str(A))
while True:
    Q = input('Dalsi kartu? Y/N ')
    if Q.upper() == 'N': 
        print('Tvoje body: ' + str(A))
        Krup = randrange(1,MAX_K)
        print('Krupier '+str(Krup))
        if A > Krup:
                print('VYHRA')
        else:
                print('PROHRA')
                A=0
    elif Q.upper() == 'Y':
        P = randrange(1,MAX_K)
        A = A + P
        print('Tvoje body: ' + str(A))
        if A > MAX: 
            print('PROHRA '+ str(A))
            A=0

    


