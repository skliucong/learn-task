##有问题 待解决！！！！！！！！！！！！！

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

def gaussian(x,u,Σ):
    D=len(x)
    m1=1/((2*np.pi)**(D/2))
    m2=1/(np.abs(Σ)**(1/2)) ##矩阵
    m3=(-1/2)*(((x-u).T*(Σ**(-1)))*(x-u))
    z=m1*m2*(np.e**m3)
    return z

if __name__=='__main__':
    X, Y = getset()
    XT=[]
    YT=[]
    XF=[]
    YF=[]
    for i in range(len(Y)):
        if Y[i]==1:
            XT.append(X[i])
            YT.append(Y[i])
        elif Y[i]==0:
            XF.append(X[i])
            YF.append(Y[i])
        else:
            print("Fail !!")
            break
    XT=np.array(XT)
    YT=np.array(YT)
    XF=np.array(XF)
    YF=np.array(XF)

    print(len(XT),len(XF))

    T_u =np.mean(XT, axis=0)
    F_u =np.mean(XF, axis=0)

    T_Σ=np.mean(np.dot((XT-T_u).T,(XT-T_u)),axis=0)
    F_Σ=np.mean(np.dot((XF-F_u).T,(XF-F_u)),axis=0)

    Σ=(len(T_Σ)/len(Y))*T_Σ + (len(F_Σ)/len(Y))*F_Σ
    print(len(Σ))

    for kkk in range(len(Σ)):
        if F_Σ[kkk]==0:
            print(kkk)

    ac=0
    wrong=0
    for ppp in range(len(Y)):
        if np.mean(gaussian(X[ppp], T_u, Σ))>=np.mean(gaussian(X[ppp], F_u, Σ)) and Y[ppp]==1:
            ac=ac+1
        elif np.mean(gaussian(X[ppp], T_u, Σ))<np.mean(gaussian(X[ppp], F_u, Σ)) and Y[ppp]==0:
            ac=ac+1
        else:
            wrong=wrong+1
    print("acc : ",ac/len(Y))
    print("wrong : ", wrong / len(Y))






