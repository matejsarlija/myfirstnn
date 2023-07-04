import numpy as np
from keras.datasets import mnist



def ReLU(x):
    return np.maximum(x,0)

def dReLU(x):
    return x>0

def softmax(x): #Normalizacija output sloja na 0.0-1.0
    exp = np.exp(x - np.max(x))
    return exp / exp.sum(axis=0)

def oneHot(Y):
        one_hot_Y = np.zeros((Y.size, Y.max() + 1))
        one_hot_Y[np.arange(Y.size), Y] = 1
        one_hot_Y = one_hot_Y.T
        return one_hot_Y #oneStolenEncoder

def CategoricalCrossEntropy(y_true,y_pred):
    return -np.sum(y_true * np.log(y_pred + 10**-100))


class NN():
    def __init__(self,X,Y,lr) -> None:
        self.X = X
        self.Y = Y
        self.learningRate = lr

        self.W1 = np.random.random((256,784)) - 0.5
        self.b1 = np.random.random((256,1)) - 0.5
        self.W2 = np.random.random((10,256)) - 0.5
        self.b2 = np.random.random((10,1)) - 0.5

    def forward(self,input):
        Z1 = self.W1.dot(input) + self.b1
        A1 = ReLU(Z1)
        Z2 = self.W2.dot(A1) + self.b2
        A2 = softmax(Z2)

        return Z1, A1, Z2, A2

    def backward(self,Z1, A1, Z2, A2, labels, sample):
        m = 1
        dZ2 = A2 - labels

        dW2 = 1/m * dZ2.dot(A1.T)
        db2 = 1/m * dZ2

        dA1 = self.W2.T.dot(dZ2)
        dZ1 = dA1 * dReLU(Z1)

        dW1 = 1/m * dZ1.dot(sample.T)
        db1 = 1/m * dZ1

        return dW1, db1, dW2, db2

    def update(self,dW1,db1,dW2,db2):
        self.W1 -= dW1 * self.learningRate
        self.b1 -= db1 * self.learningRate
        self.W2 -= dW2 * self.learningRate
        self.b2 -= db2 * self.learningRate



    def fit(self):
        loss = 0
        acc = 1
        for idx,sample in enumerate(self.X):
            sample = np.expand_dims(sample,axis=1)
            Z1, A1, Z2, A2 = self.forward(sample)
            Y = np.expand_dims(self.Y[:,idx],axis=1)
            dW1, db1, dW2, db2 = self.backward(Z1, A1, Z2, A2,Y,sample)
            self.update(dW1, db1, dW2, db2)

            loss += CategoricalCrossEntropy(Y, A2)


            if(np.argmax(A2) == np.argmax(Y)):
                acc += 1

            print(f"Accuracy = {(idx / acc) * 10}%")



        print(loss)



# MNIST training part

(x_train,y_train),(x_test,y_test) = mnist.load_data()

print(x_train.shape)
x_train = x_train.reshape(x_train.shape[0],x_train.shape[1] ** 2)

sample = x_train[0]

sample = np.expand_dims(sample, axis=1) # Sample shape = 784,1

y_train = oneHot(y_train)

y_sample = y_train[:,0]
y_sample = np.expand_dims(y_sample,axis=1)


print(y_sample)


#Inicijalizacija mreže
print(f"X sample shape = {x_train.shape} , Y sample shape = {y_train.shape}")
model = NN(x_train, y_train,0.001)

model.fit()
