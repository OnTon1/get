import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from matplotlib.ticker import MultipleLocator
from scipy.optimize import curve_fit

# Подписываем оси и график
plt.title(r"Зависимость Q(dP) ")
plt.ylabel("Q, мл/с ")
plt.xlabel(r"dP, Па")

# Функция фиттирования
def mapping_lin(values_x, k, b):
    return k * values_x + b

R1 = 1.975
R2 = 2.52
R3 = 1.5   

# d = 3.95 mm
Q1 = np.array([5.78, 15.33, 21.70, 27.53, 38.41, 48.96, 54.54, 66.14, 104.28, 108.77, 113.46, 118.39, 121.85, 129.10, 135.66, 144.51])
dP1 = np.array([9.8, 23.52, 33.32, 43.12, 60.76, 76.44, 88.2, 107.8, 190.12, 209.72, 243.04, 282.24, 317.52, 374.36, 415.52, 472.36])
dP1_lin = np.array([9.8, 23.52, 33.32, 43.12, 60.76, 76.44, 88.2, 107.8, 190.12])
Q1_lin = np.array([5.78, 15.33, 21.70, 27.53, 38.41, 48.96, 54.54, 66.14, 104.28])
plt.errorbar(dP1,Q1, yerr=1.5, xerr=5, fmt='.', color = 'red')


args, _  = curve_fit(mapping_lin, dP1_lin, Q1_lin) 
k1, b1 = args[0], args[1] 
y_fit1 = k1 * dP1_lin + b1

# d = 5.05 mm
Q2 = np.array([28.33, 53.61, 65.27, 77.97, 99.35, 115.42, 118.26, 131.41, 135.44, 156.25, 171.99, 202.33, 228.94, 252.41, 265.19])
dP2 = np.array([13.72, 27.44, 35.28, 39.2, 50.96, 58.8, 64.68, 76.44, 82.32, 119.56, 152.88, 201.88, 254.8, 303.8, 335.16])
dP2_lin = np.array([13.72, 27.44, 35.28, 39.2, 50.96, 58.8, 64.68, 76.44, 82.32])
Q2_lin = np.array([28.33, 53.61, 65.27, 77.97, 99.35, 115.42, 118.26, 131.41, 135.44])
plt.errorbar(dP2,Q2, yerr=1.5, xerr=5, fmt='.', color = 'blue')

args2, _  = curve_fit(mapping_lin, dP2_lin, Q2_lin) 
k2, b2 = args2[0], args2[1] 
y_fit2 = k2 * dP2_lin + b2

# d = 3.00 mm
Q3 = np.array([5.24, 12.44, 20.25, 29.08, 35.60, 46.17, 39.35, 26.06, 90.83, 85.84, 79.18, 97.54, 98.39, 108.85, 109.57])
dP3 = np.array([13.72, 33.32, 54.88, 79.38, 96.04, 137.2, 114.66, 70.56, 366.52, 313.6, 282.24, 403.76, 423.36, 505.68, 519.4])
dP3sort = np.sort(dP3)
Q3sort = np.sort(Q3)
plt.errorbar(dP3,Q3, yerr=1.5, xerr=5, fmt='.', color = 'green')

dP3_lin = dP3sort[0:8]
Q3_lin = Q3sort[0:8]

args3, _  = curve_fit(mapping_lin, dP3_lin, Q3_lin) 
k3, b3 = args3[0], args3[1] 
y_fit3 = k3 * dP3_lin + b3

plt.grid()

#fit d = 3.95 mm
plt.plot(dP1, Q1, color ='red', marker = 's', linestyle='none', label = 'd = 3.95 mm')
plt.plot(dP1_lin , y_fit1, "r--")
#fit d = 5.05 mm
plt.plot(dP2, Q2, color ='blue', marker = 's', linestyle='none', label = 'd = 5.05 mm')
plt.plot(dP2_lin , y_fit2, "b--")
#fit d = 3.00 mm
plt.plot(dP3, Q3, color ='green', marker = 's', linestyle='none', label = 'd = 3 mm')
plt.plot(dP3_lin , y_fit3, "g--")

plt.legend()


plt.show()