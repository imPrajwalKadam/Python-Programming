
########################################
## -- PROBLEM 6 --                    ##
## -- Date: 23/03/2034 --             ##
## -- Author:Prajwal Kadam            ## 
## -- Function Name :count_evens --   ##
## -- return Value :Integer --        ##
########################################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3

def count_evens(nums):
  count = 0
  for element in nums:
    if element % 2 == 0:
      count += 1
  return count

evenCnt = count_evens([22, 2, 1,21])
print("addition of even number is:",evenCnt)
