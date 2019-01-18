import  numpy as np
def maxminnorm(array):
    maxcols=array.max(axis=0)
    mincols=array.min(axis=0)
    data_shape = array.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]
    t=np.empty((data_rows,data_cols))
    for i in range(data_cols):
        t[:,i]=(array[:,i]-mincols[i])/(maxcols[i]-mincols[i])
    return t
def sigmod(x):
    return 1 / (1 + np.e**(-x))

def getset():
    trainfile=open("X_train",'r')
    labelfile = open("Y_train", 'r')
    x=trainfile.readlines()[1:]
    y=labelfile.readlines()[1:]
    trainfile.close()
    labelfile.close()
    x=[ [int(ite) for ite in item.strip('\n').split(',')] for item in x ]
    y=[int(item.strip('\n')) for item in y]

    X=np.array(x)
    Y=np.array(y)
    X=maxminnorm(X)
    return X,Y



if __name__ == '__main__':


    learn_rate=0.00001
    epoch=100000
    batch_size=100

    X,Y=getset()
    w=np.random.rand(len(X[0]))
    b=np.random.rand()

    z = np.dot(X, w)+b
    y=sigmod(z)
    cross_entropy = -(np.dot(Y, np.log(y)) + np.dot((1 - Y), np.log(1 - y)))
    for i in range(epoch):


        w_grad=np.dot((Y-y),X)
        w=w+learn_rate*w_grad
        b_grad=Y-y
        b=b+learn_rate*b_grad

        z = np.dot(X, w)+b
        y = sigmod(z)
        tp=0
        tn=0
        for j in range(len(y)):
            if y[j]>=0.5 and Y[j]==1:
                tp=tp+1
            elif y[j]<0.5 and Y[j]==0:
                tn=tn+1
        acc=(tp+tn)/len(y)





        cross_entropy = -(np.dot(Y, np.log(y)) + np.dot((1 - Y), np.log(1 - y)))/len(Y)
        if i%1000==0:
            print(acc,"\t",cross_entropy)
##min 3158








