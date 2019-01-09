fo = open("words.txt",'r')
fc = fo.read()
lis=fc.split(" ")
ma={}
for item in lis:
    print(item)
    if ma.get(item):
        ma[item]=ma[item]+1
    else:
        ma[item]=1
fil = open("HW1_Q1.txt", "w")

num=0
for item in ma:
    fil.write("%s %s %s\n"%(item,str(num),str(ma[item])))
    num=int(num)+1
fil.close()