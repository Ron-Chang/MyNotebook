alist = 0
blist = ""
clist = None
dlist = []
elist = ()
flist = {}
glist = [eval(f"{chr(i)}list") for i in range(97,102+1)]

lists = [eval(f"{chr(i)}list") for i in range(97,103+1)]

for i, alist in enumerate(lists):
    result = f"if {alist} == True" if alist else f"if {alist} == False"
    print(f"{result}")
# str(eval(f"{lists}[{i}]"))
