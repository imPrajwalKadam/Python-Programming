def addition(a,b):
          return a+b

def calculation(func,x,y,z):
        additionTwo =  func(x,y)
        return additionTwo +z

result = calculation(addition,51,21,11)
print(result) 

# output :83

