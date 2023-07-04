X_TRAIN = [
    [0,0],
    [0,1],
    [1,0],
    [1,1],
]

# NAND
Y_TRAIN = [
    1,
    1,
    1,
    0
]


w1 = 0.2
w2 = 0.04
b = 0.3
def sigmoidf(val):
    e = 2.71828
    return 1/(1+e**-(val))

def leakyRelu(val):
    return max(0.01*val, val)

def calculateCost(w1,w2,b):
    cost = 0

    for idx,point in enumerate(X_TRAIN):
        y = leakyRelu(w1 * point[0] + w2 * point[1] + b)

        cost += (y - Y_TRAIN[idx])**2

    return cost/len(Y_TRAIN)

def predict(w1,w2,b):
    for idx, point in enumerate(X_TRAIN):
        print(f"{point[0]} || {point[1]} = {leakyRelu(w1 * point[0] + w2 * point[1] + b)}")

eps = 1e-3
learningRate = 0.05
cs = calculateCost(w1,w2,b)

for i in range(10000):
    c = calculateCost(w1,w2,b)

    dw1 = (calculateCost(w1 + eps, w2, b) - c) / eps
    dw2 = (calculateCost(w1, w2 + eps, b) - c) / eps
    db = (calculateCost(w1,w2, b + eps) - c) / eps

    w1 -= dw1 * learningRate
    w2 -= dw2 * learningRate
    b -= db * learningRate

    c = calculateCost(w1,w2,b)
    print(f"cost : {c}")
print(f"starting cost : {cs}")

predict(w1,w2,b)
