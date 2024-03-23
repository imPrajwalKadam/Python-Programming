
########################################
## -- PROBLEM 4 --                    ##
## -- Date: 23/03/2034 --             ##
## -- Author:Prajwal Kadam            ## 
## -- Function Name :doubleChar --    ##
## -- return Value :String --         ##
########################################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
  result = ''
  for char in str:
    result += char * 2
  return result

sRet = doubleChar('ATHS')
print(sRet)