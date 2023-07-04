x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

ypred = []
w = 0.3
c = 0

for idx, point in enumerate(x):

    predicted = w * point
    ypred.append(predicted)

    c += (predicted - y[idx])**2

c /= len(x)

print(f"cost = {c}")

print(ypred)
