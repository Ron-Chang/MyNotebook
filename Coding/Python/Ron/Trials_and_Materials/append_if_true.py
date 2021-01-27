# A
result = list()
result += [temp] if temp is not None else []


# B
result = list()
(result.append(temp) if temp is not None else None)

#C
result = list()
a_list = [0,1,2,{},[],(),False,True,""]
result += filter(None, a_list)
## result:[1, 2, True]

# python 3.8
if a := func(): b.append(a)
