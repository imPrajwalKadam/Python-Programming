l = [11,21,51,101,111,400,121,151,201]
print(l)
if "Atharva" in l:
          print("Yes")
else:
        print("No")
        l.append("Atharva")

l.reverse()
print(l)
print(l.index(21))

# insert method will accept a index to insert a data in first argument
l.insert(0,1)
print(l)

demo = ['prajwal','atharva','viraj','swaraj']

# extend method will add  demo a list at the end of l list 
l.extend(demo)
print(l)