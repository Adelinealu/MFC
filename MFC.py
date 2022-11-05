from math import comb
import statistics

print(comb(12, 4))
print(comb(30, 5))
print(comb(15, 5) + comb(25, 5))

# Python code to demonstrate the working of
# mean()

# importing statistics to handle statistical
# operations


# initializing list
list = [1, 2, 2, 3, 2, 4, 3, 1]

# using mean() to calculate average of list
# elements
print("The average of list values is : ", end="")
print(statistics.mean(list))