j=[]

for i in range(2000, 3201):
    if(i % 7 == 0)and (1 % 5 != 0):
        j.append(str(i))
        print(','.join(j))