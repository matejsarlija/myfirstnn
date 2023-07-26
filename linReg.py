from utils.utils import regplot

X_TRAIN = [1,2,3,4]
Y_TRAIN = [3,5,7,9]


learningRate = 0.1
eps = 0.001
w = 0.2
b = 1


def calculateCost(w,b):
    c = 0
    regplot(w,b,X_TRAIN,Y_TRAIN,pauseDuration=0.0001)
    for idx,point in enumerate(X_TRAIN):

        predicted = w * point + b
        c += (predicted - Y_TRAIN[idx])**2

    c /= len(X_TRAIN)

    return c

def predict(w,b):
    for i in X_TRAIN:
        print(f"{i} * w + b = {w * i + b}")


epochs = 100
for i in range(epochs):
    cost = calculateCost(w,b)

    dw = (calculateCost(w + eps,b) - cost)/eps
    db = (calculateCost(w, b + eps) - cost)/eps

    print(f"dw = {dw}")
    print(f"cost = {cost}")
    w -= dw * learningRate
    b -= db * learningRate
    print(f"cost nakon pomaka = {calculateCost(w,b)}")
    print("-------------")

print(w)

predict(w,b)



