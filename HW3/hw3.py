import numpy as np
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPool2D
from keras.layers import Dropout
from keras.layers import Flatten
from HW3.built import  build_model
import keras




import random
from keras.utils.np_utils import to_categorical



def getdata():
    train_lis=[]
    label_lis=[]
    with open("D:\\data\\hung_lee_HW3\\train.csv") as train_file:
        i=0
        for li in train_file:
            if i==0:
                i=i+1
                continue
            line=li.strip("\n").split(",")
            line_x = line[1].split(" ")
            line0=int(line[0])
            line_y=[0,0,0,0,0,0,0]
            line_y[line0]=1

            x=line_x
            y=line_y
            train_lis.append(x)
            label_lis.append(y)
            i=i+1
    return np.array(train_lis).reshape(-1,48,48,1),np.array(label_lis)    # -1代表不知道多少行


def read_dataset(mode='train', isFeat=True):
    """
    Return:
        # features: (int. list) list
        # labels: int32 2D array
        data_ids: int. list
    """
    # num_data = 0
    datas = []

    with open("D:\\data\\hung_lee_HW3\\train.csv") as file:
        # file = pd.read_csv(os.path.join(data_dir,'{}.csv'.format(mode)), sep=',', header=0)
        # print(file.readlines()[0:1])
        for line_id, line in enumerate(file.readlines()[1:]):
            # print('line : ', line, line_id)
            if isFeat:
                label, feat = line.split(',')
            else:
                _, feat = line.split(',')
            # print(feat)
            feat = np.fromstring(feat, dtype=int, sep=' ')
            # 归一化
            feat = feat / 255
            print(feat)
            feat = np.reshape(feat, (48, 48, 1))

            if isFeat:
                datas.append((feat, int(label), line_id))
            else:
                datas.append(feat)

    random.shuffle(datas)  # shuffle outside
    if isFeat:
        feats, labels, line_ids = zip(*datas)
    else:
        feats = datas
    feats = np.asarray(feats)
    if isFeat:
        labels = to_categorical(np.asarray(labels, dtype=np.int32))
        return feats, labels, line_ids
    else:
        return feats





if __name__ == '__main__':
    # myX,myY=getdata()
    #
    # print(X[0])

    P=read_dataset()
    X=P[0]
    Y=P[1]
    # print(len(P[0][0]))
    # print(len(P[1][1]))
    # print(len(P[2]))
    # print('True： ',P[0][0])

    # print('my: ',myX[0])

    #
    # model=build_model(mode='simple')
    # model.fit(X,Y,batch_size=64,epochs=60)




    model = keras.Sequential()

    # 第一个卷积层，32个卷积核，大小５x5，卷积模式SAME,激活函数relu,输入张量的大小
    model.add(Conv2D(filters=32, kernel_size=(8, 8), padding='Same', activation='relu', input_shape=(48, 48,1)))  ##nput_shape(长，宽，高)

    # 池化层,池化核大小２x2
    model.add(MaxPool2D(pool_size=(2, 2)))
    # 随机丢弃四分之一的网络连接，防止过拟合
    model.add(Dropout(0.25))

    model.add(Conv2D(filters=64, kernel_size=(5, 5), padding='Same', activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(filters=64, kernel_size=(5, 5), padding='Same', activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Dropout(0.25))




    # 全连接层,展开操作，
    model.add(Flatten())
    # 添加隐藏层神经元的数量和激活函数
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.25))
    # 输出层
    model.add(Dense(7, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X,Y,batch_size=100,epochs=50)
