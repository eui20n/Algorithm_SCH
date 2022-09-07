import matplotlib.pyplot as plt
import numpy as np
import math

# 데이터 정의 -> x는 고정
x = np.arange(0, 5)

"""
  y : 1차 함수
  y_2 : 2차 함수
  y_3 : 3차 함수
  y_log : log 함수
  y_y : 2^x 함수
  y_ylogy : nlogn 함수
"""
y = x
y_2 = x ** 2
y_3 = x ** 3
y_log = np.log(x)
y_y = 2 ** x
y_ylogy = x * np.log(x)
y_fac = [math.factorial(n) for n in x]

plt.plot(y, x, label = "n")
plt.plot(y_2, x, label = "n^2")
plt.plot(y_log, x, label = "logn")
plt.plot(y_y, x, label = "2^n")
plt.plot(y_ylogy, x, label = "nlogn")
plt.plot(y_fac, x, label = "fac")
plt.legend()
plt.show()