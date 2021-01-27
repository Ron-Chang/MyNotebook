"""Write a function that takes a string of braces, and determines if the order of the braces is valid.
It should return true if the string is valid, and false if it's invalid.
This Kata is similar to the Valid Parentheses Kata,
but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""
def isPair(string):

    if string.count("(")%2 == string.count(")")%2:
        pass

def validBraces(string):
    # remove cannot pair
    if string.count("(")%2 == 1 or string.count("{")%2 == 1 or string.count("[")%2 == 1:
            return False

    for s in string:
        try:
            if string.index(")") < string.index("(") or string.index("}") < string.index("{") or string.index("]") < string.index("["):
                return False
        except:
            pass

        print(string)
        # if s == "(" and s != ")" and string[-1] ==")":
        #     string = string.strip("()")
        # elif s == "{" and s != "}":
        #     string = string.strip("{}")
        # elif s == "[" and s != "]":
        #     string = string.strip("[]")
        if s == "(" and string[-1] ==")":
            string = string.strip("()")
        elif s == "{" and string[-1] =="}":
            string = string.strip("{}")
        elif s == "[" and string[-1] =="]":
            string = string.strip("[]")

    if len(string) == 0:
        return True
    else:
        return False


# pattern = '()'#True
# pattern = '(){}[]'#True
# pattern = '[(])'#False
# pattern = '{}({})[]'#True
# pattern = '(((({{'#False

patterns = ['()', '(){}[]', '[(])', '{}({})[]', '(((({{']
for pattern in patterns:
    print(f"{pattern} : {validBraces(pattern)}")

# def validBraces(string):
#     round_l = string.count("(")
#     square_l = string.count("[")
#     curly_l = string.count("{")

#     round_r = string.count(")")
#     square_r = string.count("]")
#     curly_r = string.count("}")

#     S=""

#     if (round_l == round_r) and (square_l == square_r) and (curly_l == curly_r):
#         for i in string:
#             if i == "(" or i == ")":
#                 S+="1"
#             elif i == "[" or i == "]":
#                 S+="2"
#             else:
#                 S+="3"
#         print(S)
#         return True
#     else:
#         return False
