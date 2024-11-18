
import matplotlib.pyplot as plt
import numpy as np  # 导入NumPy库

# 数据定义
theta = [21, 22, 23, 24, 25, 26, 27, 28, 29]  # 第一列
U_theta_plus = [0.6, 0.1, 0.0, 0.0, 0.1, 0.2, 0.1, 0.1, 0.1]  # 第二列
U_theta_minus = [0.2, 0.0, 0.0, 0.1, 0.2, 0.2, 0.3, 0.5, 1.9]  # 第三列

# 计算点的坐标
x = [-t for t in theta]  # 第一列取负作为横坐标
y = U_theta_minus  # 第三列作为纵坐标

# 绘图
plt.figure(figsize=(10, 6))

# 绘制曲线
plt.plot(x, y, marker='o', label=r'$U_\theta^-$ (mV)', color='blue', linestyle='-', markersize=8)

# 设置标题和坐标轴标签
plt.title('Data Points and Curve of $U_\theta^-$')
plt.xlabel(r'$-\theta$ (°)')
plt.ylabel(r'$U_\theta^-$ (mV)')

# 添加参考线
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# 设置坐标轴范围
plt.xlim(-30, -20)  # 横坐标范围从-30到-20
plt.ylim(min(U_theta_minus) - 0.5, max(U_theta_minus) + 0.5)

# 设置坐标刻度
plt.xticks(range(-30, -19, 1))  # 横坐标刻度从-30到-20
plt.yticks(np.arange(0, max(U_theta_minus) + 1, 0.5))  # 纵坐标刻度

# 显示网格
plt.grid()

# 设置图例
plt.legend()

# 显示图形
plt.show()

