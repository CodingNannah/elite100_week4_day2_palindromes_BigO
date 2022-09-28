# do this in python via venv & pip install: 
# import big_o

# https://medium.com/analytics-vidhya/how-to-find-the-time-complexity-of-a-python-code-95b0237e0f2d
# https://pypi.org/project/big-O/

# do this line by line in python after big_O install:
# 1. run code
# 2. run this:
# positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
# best, others = big_o.big_o(NAME_of_FUNC, positive_int_generator, n_repeats=100)
# print(best)

# will output time



"""
Solve the following problem:
In comments Provide the Time Complexity of your solution.
Your mission is to solve this problem in O(n) time or better

Time Complexity = [ log(n), n, n**2, n**3 ]

A palindrome is if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true or false.
 
s = "A man, a plan, a canal: Panama"
true
"amanaplanacanalpanama" is a palindrome.

s = "race a car"
false
"raceacar" is not a palindrome.

s = " "
true
s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
# # create new string outside the function

# # start the function
# def is_palindrome(astring):
# # sanitize the string:
#     # make lower: .lower()
#     # remove nonalphaneumeric: 
#           # (https://pythonsolved.com/how-to-remove-all-non-alphanumeric-characters-from-string-in-python/)
#           # filter(str.isalnum,the_string)
#     # remove space: .strip()
#     # bring letters together "".join()
#     # ***any work together?
#         # .lower() and .strip()
#         sanitize_astring = astring.lower().strip()
#         # "".join() and filter()
#         sanitize_astring2 = ''.join(s for s in sanitize_astring2 if sanitize_astring.isalnum())
#     # save to new string outside the function
# # look at letters in the new string
# # are the letters that are going forward and backward the same?

# # Boolean: if yes (they == ) return True else False
#                 return True
# return sanitize_s2 == sanitize_s2[::-1]

# text multi-strings

# # Describe Time Type

# # sanitized_string = ''.join(filter(str.isalnum,astring.lower().strip()))

#***********************************************************

s = "A man, a plan, a canal: Panama" # = True
# s = ' '                             # = True
# s = "race a car"                    # = False
# s = 'racecar'                       # = True
# s = 'ABBA'                          # = True
# s = 'Abab'                          # = True
# s = "433576"                        # = False
# s = "801-753-1736_6371357-108"      # = True


def is_palindrome(s):
    sanitize_s = s.lower().strip()
    # return (sanitize_s)
    sanitize_s2 = ''.join(filter(str.isalnum, sanitize_s))
    # return (sanitize_s2)
    return sanitize_s2 == sanitize_s2[::-1]
   
print(is_palindrome(s))
