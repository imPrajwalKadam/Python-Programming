
#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  # CODE GOES HERE
  a = a.lower()
  b = b.lower()

  return(b.endswith(a) or a.endswith(b))
#   return a[-(len(b)):]==b or a == b[-len(a):]
bret = end_other('Hiabx', 'abc')
print(bret)