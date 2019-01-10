import numpy as np
def MaxMinNormalization(x,Max,Min):
    if Max-Min==0:
        return 0
    x = (x - Min) / (Max - Min)
    return x

def getset():
    file=open("test.csv",'r')
    file2 = open("ans.csv", 'r')

    rea=file.readlines()
    total=[]
    for i in range(0,len(rea),18):
        total.append(rea[i:i+18])
    # print(total)
    file.close()

    rea2=file2.readlines()
    label = [item.strip('\n').split(',')[-1] for item in rea2[1:]]
    file2.close()


    x=[]

    ma=[]
    mi=[]
    for item in total:
        for i in range(18):
            if i==10:
                ma.append(0)
                mi.append(0)
                continue
            item[i]=[float(iii) for iii in item[i].strip('\n').split(',')[2:]]

            if len(ma)<=i:
                ma.append(np.max(item[i]))
            else:
                if np.max(item[i])>ma[i]:
                    ma[i]=np.max(item[i])


            if len(mi)<=i:
                mi.append(np.min(item[i]))
            else:
                if np.min(item[i])<mi[i]:
                    mi[i]=np.min(item[i])



    for item in total:
        it=[]
        for i in range(18):
            if i!=10:
                its=item[i]
                its=[float(ite) for ite in its]
                it=it+[MaxMinNormalization(itemits,ma[i],mi[i]) for itemits in  its]
        x.append(it)
    return np.array(x,dtype = float),np.array(label,dtype = float)
# b=np.random.rand()
#w=np.random.rand(153)
w=A=np.zeros(153)
x,label=getset()
print(x.shape)
learn_rate=0.0001
y=np.dot(x,w)
print(y.shape)
loss=sum(pow(label-y,2)/2)

for i in range(9999999999999):
    v=np.dot((label-y),x)

    w=w+learn_rate*v
    y = np.dot(x, w)
    loss = sum(pow(label - y, 2) / 2)
    if i%10000==0:
        print(loss)

#############求导













# y=w*x+b
#loss=(label-y)^2






