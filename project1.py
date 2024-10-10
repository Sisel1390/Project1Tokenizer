import re
import functions
filename = "example1.txt"
text= functions.no_comments(filename) #makes the file easier to call in functions under a different name.
nw = functions.no_whitespace(filename) # same thing but this is with no whitespaces compared to no comments from above
print(functions.no_comments(filename))
print("\nTokens: \n")
functions.tokenlist(text)
functions.comments(nw)
print("Total: ",functions.count(text))