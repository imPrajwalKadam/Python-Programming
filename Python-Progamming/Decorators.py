# ///////////////////////////////////////////////////////////////////
# // DECORETORS:
# //function name:SumThree
# //Input :       function
# //Output:       innerfunction
# //Discription:  it is perform addition of paramiter function result and one other number
# //Date:         24/11/2023
# //Author:       Prajwal pradeep kadam

# ////////////////////////////////////////////////////////////////////



def SumThree(func):
          def inner():
                  iNo3 = int(input("Enter A Third Number : "))

                  result = func()
                  return result+iNo3
          return inner
# decoretors 
@SumThree
def addition():
       iNo1 = int(input("Enter A First Number :"))
       iNo2 = int(input("Enter A Second Number :"))
       result = iNo1+iNo2       
       return result



# iSum = SumThree(addition,iNo1,iNo2)
iResult = addition()
print("Addition of three number is",iResult)

        
                  

