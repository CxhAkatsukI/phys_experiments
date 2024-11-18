import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress



# 假设一些示例数据
m = np.array([1.863, 2.008, 2.175, 2.290, 2.448, 2.582, 2.690, 2.833])  # 横坐标，单位为 mm
li = np.array([31, 60, 91, 119, 150, 179, 208, 238])  # 纵坐标，单位为 g

# 拟合一条直线
slope, intercept, r_value, p_value, std_err = linregress(m, li)

# 打印斜率k
print(f"斜率 k = {slope:.6f}")

# 计算直线上的两点
x1, x2 = m[0], m[-1]  # 使用数据的第一个和最后一个x值
y1, y2 = slope * x1 + intercept, slope * x2 + intercept  # 对应的y值

# 绘图
plt.scatter(m, li, color='blue', label='Data Points')  # 原始数据点
plt.plot([x1, x2], [y1, y2], color='red', label=f'Linear Regression Line (k={slope:.6f})')  # 拟合的直线

# 设置图例和标签
plt.xlabel('$Z_i$ (mm)')
plt.ylabel('$U_i$ (mV)')
plt.legend()
plt.title('Scatter Plot of $U_i$ and $Z_i$ with Fitted Line')

# 显示图形
plt.show()
