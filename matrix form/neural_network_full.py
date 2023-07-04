import numpy as np

X_TRAIN = [
    [0,0],
    [0,1],
    [1,0],
    [1,1],
]
X_TRAIN = np.array(X_TRAIN)
Y_TRAIN = [
    0,
    1,
    1,
    0
]

class Model():
    def __init__(self,learningRate) -> None:
        self.learningRate = learningRate
        
        self.W1 = np.random.random((2,2)) - 0.5
        self.b1 = np.random.random((2,1)) - 0.5
        self.W2 = np.random.random((1,2)) - 0.5
        self.b2 = np.random.random((1,1)) - 0.5
        
        self.dW1 = np.zeros_like(self.W1)
        self.db1 = np.zeros_like(self.b1)
        self.dW2 = np.zeros_like(self.W2)
        self.db2 = np.zeros_like(self.b2)

        
    def forward(self,input):
        Z1 = self.W1.dot(input) + self.b1
        Z2 = self.W2.dot(Z1) + self.b2
        
        return Z2
        
    def backward(self):
        pass
    
    def calculateCost(self):
        cost = 0
        
        
        for idx,point in enumerate(X_TRAIN):
            point = np.expand_dims(point, axis = 1)
            pred = self.forward(point)
            
            cost += (pred - Y_TRAIN[idx])**2
            
        return cost
    
    def calculateGradient(self):
        c = self.calculateCost()
        eps = 1e-3
        saved = None
        
        for x in range(self.W1.shape[0]):
            for y in range(self.W1.shape[1]):
                saved = self.W1[x,y] 
                self.W1[x,y] += eps
                costNew = self.calculateCost()
                self.W1[x,y] = saved
                
                self.dW1 = (costNew - c)/ eps
                
        for x in range(self.b1.shape[0]):
            for y in range(self.b1.shape[1]):
                saved = self.b1[x,y] 
                self.b1[x,y] += eps
                costNew = self.calculateCost()
                self.b1[x,y] = saved
                
                self.db1 = (costNew - c)/ eps
                
        for x in range(self.W2.shape[0]):
            for y in range(self.W2.shape[1]):
                saved = self.W2[x,y] 
                self.W2[x,y] += eps
                costNew = self.calculateCost()
                self.W2[x,y] = saved
                
                self.dW2 = (costNew - c)/ eps
                
        for x in range(self.b2.shape[0]):
            for y in range(self.b2.shape[1]):
                saved = self.b2[x,y] 
                self.b2[x,y] += eps
                costNew = self.calculateCost()
                self.b2[x,y] = saved
                
                self.db2 = (costNew - c)/ eps
                
        
    
    def update(self):
        self.W1 -= self.dW1 * self.learningRate
        self.b1 -= self.db1 * self.learningRate
        self.W2 -= self.dW2 * self.learningRate
        self.b2 -= self.db2 * self.learningRate
    
    def fit(self,epochs):
        print(f"cost start = {self.calculateCost()}")
        for i in range(epochs):
            self.calculateGradient()
            self.update()
        
        print(f"cost finish = {self.calculateCost()}")
        
                
                
    
lr = 0.1
model = Model(learningRate=lr)
model.fit(100)

        


