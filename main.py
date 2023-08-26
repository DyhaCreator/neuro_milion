import random

ob = 0.00001
out = 0
w = random.random()

for x in range(0, 100000):
    milion = 1
    speed = 0

    for i in range(0, 100):
        out = milion * w
        speed += out
        milion += speed
    #print(milion)
    #print(w)
    err = 1000000 - milion
    if(err > 0):
        w += ob
    elif(err < 0):
        w -= ob


milion = 1
speed = 0

for i in range(0, 100):
    out = milion * w
    speed += out
    milion += speed
print(milion)
print(w)