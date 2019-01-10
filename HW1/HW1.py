import numpy as np
def MaxMinNormalization(x,Max,Min):
    if Max-Min==0:
        return 0
    x = (x - Min) / (Max - Min)
    return x
def GetMaxMin(total):
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
    return ma,mi

def getset():
    trainfile=open("test.csv",'r')
    labelfile = open("ans.csv", 'r')

    rea=trainfile.readlines()
    total=[]
    for i in range(0,len(rea),18):
        total.append(rea[i:i+18])
    trainfile.close()

    rea2=labelfile.readlines()
    label = [item.strip('\n').split(',')[-1] for item in rea2[1:]]
    labelfile.close()


    x=[]
    ma,mi=GetMaxMin(total)

    for item in total:
        it=[]
        for i in range(18):
            if i!=10:
                its=item[i]
                its=[float(ite) for ite in its]
                it=it+[MaxMinNormalization(itemits,ma[i],mi[i]) for itemits in  its]
        x.append(it)
    return np.array(x,dtype = float),np.array(label,dtype = float)


if __name__ == '__main__':

    learn_rate=0.0001
    epoch=1000000

    x,label=getset()
    w=np.random.rand(len(x[0]))

    y=np.dot(x,w)
    loss=sum(pow(label-y,2)/2)

    for i in range(epoch):

        v=np.dot((label-y),x)
        w=w+learn_rate*v

        y = np.dot(x, w)

        loss = sum(pow(label - y, 2) / 2)/len(label)
        if i%10000==0:
            print(loss)





