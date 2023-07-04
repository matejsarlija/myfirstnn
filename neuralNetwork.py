import numpy as np

def softmax(x): #Normalizacija output sloja na 0.0-1.0 - Oduzmemo maksimalnu vrijednost radi stabilnosti / velikih brojeva
    exp = np.exp(x - np.max(x)) 
    return exp / exp.sum(axis=0)

def normalSoftmax(x):
    return (np.exp(x)/np.exp(x).sum())

def oneHot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y #oneStolenEncoder


def ReLU():
    #TODO: Implementiraj
    return None

def dReLU():
    #TODO: Implementiraj derivaciju od relua
    return None
 
    
def CategoricalCrossEntropy():
    safety = 10**-100 #Sprjecimo nan
    #TODO: Implementiraj
    return None


class NN():
    def __init__(self,X,Y,lr) -> None:
        #TODO: Inicijaliziraj weightove i biase, učitaj dataset i labele, postavi learning rate

        self.X = X
        self.Y = X
        self.learningRate = lr
        self.W1 = None
        self.b1 = None
        self.W2 = None
        self.b2 = None
        
    def forward(self):
        #TODO: Implementiraj forward pass
    
        return None
    
    def backward(self,Z1, A1, Z2, A2, labels, sample):
        m = 1 # Sample size (stohastic u nasem slucaju, inace batch size)
        dZ2 = A2 - labels # Derivacija categorical cross entropy cost funkcije + softmax funkcije 
        
        dW2 = 1/m * dZ2.dot(A1.T) # Derivacija funkcije na matricu weightova
        db2 = 1/m * dZ2 # Derivacija funkcije na matricu biasa
        
        dA1 = self.W2.T.dot(dZ2) # Pošalji gradijent prethodnom layeru
        dZ1 = dA1 * dReLU(Z1) # Derivacija ReLU funkcije
        
        dW1 = 1/m * dZ1.dot(sample.T) # Derivacija funkcije na matricu weightova
        db1 = 1/m * dZ1 # Derivacija funkcije na matricu biasa
        
        return dW1, db1, dW2, db2 # Vrati gradijente matrica
    
    def update(self):
        #TODO: Implementiraj

        return None
    
    def fit(self):
        #TODO : Implementiraj

        return None
    
