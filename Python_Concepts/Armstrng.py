'''
accept number from user and chek Armstrong or not
input : 512
5*5*5 + 1*1*1 +2*2*2 == 512 arm else not arm

'''

def ChkArm(ino):
    iDigit = 0
    iadd = 0    
    imult = 1
    print(ino)  
    print(type(ino))
    temp = ino
    icnt = 0
    while temp != 0:
        temp = temp//10
        icnt += 1

    print(icnt)
    temp = ino
    i = 0

    while temp != 0:
        iDigit = temp %10
        for i in range(icnt):
            print(imult)
            imult = imult * iDigit
        
        iadd = iadd + imult
        imult = 1
        temp = temp // 10
    if iadd == ino:
        print("number is armstrong : ")
    else:
        print("number is not armstrong : ")




ino = int(input("Enter a number: "))
ChkArm(ino)