class Arithmetic:
    def __init__(self, no1, no2):
        self.ino1 = no1
        self.ino2 = no2
        self.ans = 0

    def addition(self):
        self.ans = self.ino1 + self.ino2
        return self.ans

    def subtraction(self):
        self.ans = self.ino1 - self.ino2
        return self.ans

class Stringopt(Arithmetic):
    def __init__(self, no1, no2):
        super().__init__(no1, no2)
        print("String Opt Class")

# Object Creation
obj1 = Stringopt(10, 11)
# obj2 = Stringopt(21, 11)

iret = obj1.addition()
print("Addition of obj1 is:", iret)

iret = obj1.subtraction()
print("Subtraction of obj2 is:", iret)
