import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 用户提供的两组数据
x1 = np.array([273.15+30.9, 273.15+35.4, 273.15+40.0, 273.15+45.1, 273.15+50.4])  # 第一组数据
y1 = np.array([1944.0, 1601.0, 1335.0, 1091.0, 890.0])  # 第二组数据

# 对第一组数据取倒数
x_reciprocal = 1 / x1

# 对第二组数据取对数
y_log = np.log(y1)

# 线性拟合
slope, intercept, r_value, p_value, std_err = stats.linregress(x_reciprocal, y_log)

# 拟合曲线
y_fit = slope * x_reciprocal + intercept

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter(x_reciprocal, y_log, label='Data', color='blue')  # 原始数据点
plt.plot(x_reciprocal, y_fit, label=f'Fit: y = {slope:.2f}x + {intercept:.2f}', color='red')  # 拟合曲线

# 图表设置
plt.title('Linear Relationship between 1/x and log(y)')
plt.xlabel('1/x')
plt.ylabel('log(y)')
plt.legend()
plt.grid(True)

# 显示图形
plt.show()
