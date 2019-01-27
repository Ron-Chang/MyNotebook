times_table = lambda i, j: "\n".join("{} X {} = {:>2}".format(x, y, x*y) for x in range(2,i+1) for y in range(2,j+1))

print(times_table(9,9))


# Explain: How is this statement executed ?

