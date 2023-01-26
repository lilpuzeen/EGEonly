import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt


def get_data():
	data = pd.read_excel('TaskDataVar1.xls')
	data = data.dropna()
	return data


def std_dev(data):
	# Calculate the standard deviation of the data
	# data: pandas dataframe
	# return: standard deviation
	return np.std(data)


# def f(x)

# def min_bfgs(data):
# 	# Calculate the minimum of the data using BFGS
# 	# data: pandas dataframe
# 	# return: minimum
# 	return opt.minimize(std_dev, data, method='BFGS')

data = get_data()
# read first column to X and second column to Y
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
X = np.array(X)
Y = np.array(Y)
s = 0
arr = [0.99132407, 0.76975029]
for i in range(len(X)):
	s += (Y[i] - arr[0]*np.sin(2*X[i]) - arr[1])**2
print(s)
print(np.sum((Y - (1*np.sin(2*X) + 0.73))**2))
print(sum[(Y - (1*np.sin(2*X) + 0.73))**2])
