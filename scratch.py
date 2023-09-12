import math

pop = [16, 10, 5, 7, 13]

pop_mean = sum(pop) / len(pop)

print(pop_mean)


std_var = [(x - pop_mean)**2 for x in pop]

#print("cijela pop je", math.sqrt(sum(std_var) / len(pop)))

print("sample pop je", math.sqrt(sum(std_var) / (len(pop)-1)))
