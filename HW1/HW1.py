import numpy as np
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


    pm25=[]
    for item in total:
        pm25.append(item[9].strip('\n').split(',')[2:])
    return np.array(pm25,dtype = float),np.array(label,dtype = float)
# b=np.random.rand()
w=np.random.rand(9)
x,label=getset()
learn_rate=0.0000001
y=np.dot(x,w)
loss=sum(pow(label-y,2)/2)

for i in range(9999999999999):
    v=np.dot((label-y),x)
    # print(w)
    # print(v)
    w=w+learn_rate*v
    # print(w)
    y = np.dot(x, w)
    loss = sum(pow(label - y, 2) / 2)
    if i%10000==0:
        print(loss)

#############求导













# y=w*x+b
#loss=(label-y)^2






