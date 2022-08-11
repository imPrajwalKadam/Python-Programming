def Addition(iNo1,iNo2):
    iSum =int(iNo1)+int(iNo2)
    return iSum

iRet = 0
iValue1 = input("Inter First number")
print(iValue1)
iValue2 = input("Enter Second number")
print(iValue2)
iRet = Addition(iValue1, iValue2)
print("Addition of two number is",iRet)