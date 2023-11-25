def Demo(name):
          def message():
                  return "Jay "+name+"!"
          return message

message = Demo("Mahakal")
print(message())
