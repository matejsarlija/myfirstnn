# xor = (not a and b) or (a and not b)

# nand actually
import random

class Model():
    def __init__(self) -> None:
        #PRVI LAYER
        self.w1_1 = random.random() - 0.5
        self.w2_1 = random.random() - 0.5
        self.b1 = random.random() - 0.5

        self.w1_2 = random.random() - 0.5
        self.w2_2 = random.random() - 0.5
        self.b2 = random.random() - 0.5

        #DRUGI LAYER
        self.w1_3 = random.random() - 0.5
        self.w2_3 = random.random() - 0.5
        self.b3 = random.random() - 0.5

X_TRAIN = [
    [0,0],
    [0,1],
    [1,0],
    [1,1],
]

Y_TRAIN = [
    1,
    1,
    1,
    0
]

model = Model()

def leakyRelu(val):
    return max(0.01*val, val)

def sigmoidf(val):
    e = 2.71828
    return 1/(1+e**-(val))


def forward(model, point):
    a = leakyRelu(model.w1_1 * point[0] + model.w2_1 * point[1]  + model.b1)

    b = leakyRelu(model.w1_2 * point[0] + model.w2_2 * point[1] + model.b2)

    return sigmoidf(model.w1_3 * a + model.w2_3 * b + model.b3)

def calculateCost(model):
    cost = 0

    for idx,point in enumerate(X_TRAIN):
        pred = forward(model,point)

        cost += (pred - Y_TRAIN[idx])**2

    return cost

def calculateGradient(model):
    gradient = Model()
    costStart = calculateCost(model)
    eps = 1e-3
    learningRate = 0.5

    #Calculate gradient
    model.w1_1 += eps
    gradient.w1_1 = (calculateCost(model) - costStart)/eps
    model.w1_1 -= eps

    model.w2_1 += eps
    gradient.w2_1 = (calculateCost(model) - costStart)/eps
    model.w2_1 -= eps

    model.b1 += eps
    gradient.b1 = (calculateCost(model) - costStart)/eps
    model.b1 -= eps

    model.w1_2 += eps
    gradient.w1_2 = (calculateCost(model) - costStart)/eps
    model.w1_2 -= eps

    model.w2_2 += eps
    gradient.w2_2 = (calculateCost(model) - costStart)/eps
    model.w2_2 -= eps

    model.b2 += eps
    gradient.b2 = (calculateCost(model) - costStart)/eps
    model.b2 -= eps

    model.w1_3 += eps
    gradient.w1_3 = (calculateCost(model) - costStart)/eps
    model.w1_3 -= eps

    model.w2_3 += eps
    gradient.w2_3 = (calculateCost(model) - costStart)/eps
    model.w2_3 -= eps

    model.b3 += eps
    gradient.b3 = (calculateCost(model) - costStart)/eps
    model.b3 -= eps

    #Apply gradient
    model.w1_1 -= gradient.w1_1 * learningRate
    model.w2_1 -= gradient.w2_1 * learningRate
    model.b1 -= gradient.b1 * learningRate
    model.w1_2 -= gradient.w1_2 * learningRate
    model.w2_2 -= gradient.w2_2 * learningRate
    model.b2 -= gradient.b2 * learningRate
    model.w1_3 -= gradient.w1_3 * learningRate
    model.w2_3 -= gradient.w2_3 * learningRate
    model.b3 -= gradient.b3 * learningRate

def predict(model):
    print("Prediction :")
    for idx, point in enumerate(X_TRAIN):
        print(f"{point[0]} xor {point[1]} = {forward(model,point)}")

    print("----------------------------")

for i in range(10000):
    calculateGradient(model)
    #print(calculateCost(model))

predict(model)

for idx, point in enumerate(X_TRAIN):
    pred = sigmoidf(model.w1_2 * point[0] + model.w2_2 * point[1] + model.b2)
    print(f"{point[0]} && {not bool(point[1])} = {pred}")




# print(f"Starting cost = {c} \ncost = {calculateCost(model)}")
