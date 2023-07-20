d1 = {'a':155}
d2 = {'b':188}
d1.update(d2) #update() adds one dict item to aniother
print(d1)


dict = {'a':2,'b':3,'c':4,'d':5,'e':6,'f':7}
print(len(dict.keys()))


d11 = {'a':100,'b':200,'c':300}
d22 = {'a':300,'b':200,'d':400}
d33={}
for k1,v1 in d11.items():
    if k1 not in d22.keys():
        d33[k1]=v1
    for k2,v2 in d22.items():
        if k1 == k2:
            d33[k1]=v1+v2
        if k2 not in d11.keys():
            d33[k2]=v2
print(d33)