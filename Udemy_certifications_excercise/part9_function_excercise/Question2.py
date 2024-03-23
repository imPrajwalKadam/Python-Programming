
#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  # CODE GOES HERE
  result = ""
  for i in range(len(str)):
    if i%2 == 0:
      result = result + str[i]
  return result
str = stringBits('Hello')
print(str)