import re
def no_whitespace(filename):
    with open(filename, 'r') as file:
        content = file.read()
    content = "".join(content.split(' ')) #gets rid of whitespaces
    return content

def no_comments(filename):
    with open(filename, 'r') as file:
        code = file.read()
    code = re.sub(r'#.*', '',code) #gets rid of any strings after # so comments

    code = re.sub(r'""".*?"""','', code, flags=re.DOTALL) #gets rid of any strings after """ and returns the file with no comments.
    return code
def tokenlist(text):
    #keyword,idenitfier, literals, operators, seperators, comments
    keyword = re.findall(r'def|\bin\b|for|print|range|elif|else|except|\bis\b|while|try', text) #re allows for a find all function that will find all words imbedded in the list.
    unique_keyword = list(set(keyword)) #this allows for the print out to not have duplicates but one unique keyword
    print("keyword: ", unique_keyword)


    identifier = []
    identifier.extend(re.findall(r'greet|count', text)) # for identifiers the find all function will find any letters the user decides to put down as identifiers like x and words counting as identifiers.
    identifier.extend(re.findall(r'\b[a-zA-Z]\s', text))
    u_identifier = list(set(identifier))# this allows for no duplicates
    print("identifiers: ", u_identifier)

    literals = []
    literals.extend(re.findall(r'"(.*?)"', text)) #literals needed a list to find any string embedded between quotation marks to be found and printed out as well as any numbers a user would have as a set number like x = 0
    literals.extend(re.findall(r'[0-9]+', text))
    print("literals: ", literals)

    operators = re.findall(r'[+][-][*][/]|[=]', text)# the findall function can find all special characters as accounted for in the list.
    u_operators = list(set(operators)) #in cases of duplicates this will only print out once
    print("operators: ", u_operators)

    seperator = re.findall(r'[()]|[:]|[;]|[{}]',text) # find all will find any seperators that are accounted for in the list through the files
    u_seperator = list(set(seperator)) #prints out every unique seperator
    print("seperators: ", u_seperator)

def comments(nw):
    comments = []
    comments.extend(re.findall(r"#.*", nw)) # had a seperate function to find the comments that were ereased from before 
    comments.extend(re.findall(r"'''.*?'''", nw, re.DOTALL)) # to find all comments made through # or triple quotation marks
    comments.extend(re.findall(r'""".*?"""', nw, re.DOTALL))
    print("comments: ", comments)

def count(text):
    token = re.findall(r'".*"|\w+|[^\w+\s]', text) #searches for all words or special characters and counts any string imbedding in quotation marks as one in the len feature.
    return len(token)