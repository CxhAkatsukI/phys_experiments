
import matplotlib.pyplot as plt
import numpy as np

# 数据
theta = [21, 22, 23, 24, 25, 26, 27, 28, 29]
U_theta_plus = [0.6, 0.1, 0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.1]

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(theta, U_theta_plus, marker='o', label=r'$U_\theta^+$ (mV)', color='blue', linestyle='-', markersize=8)

# 设置标题和标签
plt.title('Data Points and Curve of $U_\theta^+$')
plt.xlabel(r'$\theta$ (°)')
plt.ylabel(r'$U_\theta^+$ (mV)')

# 添加水平和垂直参考线
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# 设置坐标轴范围
plt.xlim(min(theta) - 1, max(theta) + 1)
plt.ylim(min(U_theta_plus) - 0.5, max(U_theta_plus) + 0.5)

# 设置横纵坐标的刻度
plt.xticks(np.arange(min(theta), max(theta) + 1, 1))  # 横坐标
plt.yticks(np.arange(-0.5, max(U_theta_plus) + 1, 0.5))  # 纵坐标

# 显示网格
plt.grid(which='both')

# 设置图例
plt.legend()

# 显示图形
plt.show()


