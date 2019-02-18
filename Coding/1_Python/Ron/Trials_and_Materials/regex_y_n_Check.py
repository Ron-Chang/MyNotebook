import re

userinput = """
y
Y
YES
yes
Yes
!@#$%^&*()_
&3
()
##@

"""

pattern = re.compile(r"data-tooltip-html")

matches = pattern.finditer(userinput)

for match in matches:
    print(match)

illegal = re.compile(r"(\W)+")
matches = illegal.finditer(userinput)
for match in matches:
    if match != None:
        print("{}is illegal!".format(match))
