import re
import functions

filename = input("Enter which example you'd like to test: (example1.txt or example2.txt): ") # the user can run it and decide from which example text file to run
text= functions.no_comments(filename) #makes the file easier to call in functions under a different name.
nw = functions.no_whitespace(filename) # same thing but this is with no whitespaces compared to no comments from above
print(functions.no_comments(filename))
print("\nTokens: \n")
functions.tokenlist(text)
functions.comments(nw)
print("Total: ",functions.count(text))