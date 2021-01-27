import time

t1 = time.time()
players = [["james",202],["curry",193],["durant",205],["jordan",199],["david",211]]
i=0
while i != len(players):
    player = players[i]
    if player[1]>200:
        print(player)
    i+=1
t2 = time.time()
print("{:.10f}".format(t2-t1))
    # len(players) == 5
    # once i == 5 break

t1 = time.time()
players = [["james",202],["curry",193],["durant",205],["jordan",199],["david",211]]
for player in players:
    if player[1]<200:
        continue
    print(player)
t2 = time.time()
print("{:.10f}".format(t2-t1))


t1 = time.time()
players = [["james",202],["curry",193],["durant",205],["jordan",199],["david",211]]
print(" \n".join(str(player) for player in players if player[1] > 200))
t2 = time.time()
print("{:.10f}".format(t2-t1))



