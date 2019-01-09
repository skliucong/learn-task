file=open("test.csv",'r')
rea=file.readlines()
total=[]
for i in range(0,len(rea),18):
    total.append(rea[i:i+18])
# print(total)



