import numpy as np

w = [0.2, 0.3, 0.9]
b = 0.5

x = [0.5, 0.6, 0.1]

x_times_w = np.dot(w, x)
print(x_times_w)

x_times_w_plus_b = x_times_w + b
print(x_times_w_plus_b)

sigmoid_neurona = 1/(1+np.e**-x_times_w_plus_b)
print(sigmoid_neurona)
