
import matplotlib.pyplot as plt

# 数据提取
phi_I = [
    30, 32, 34, 36, 38, 40, 42, 44, 46,  # 第一行角度数据
    48, 50, 52, 54, 56, 58, 60, 62, 64,  # 第二行角度数据
    66, 68, 70  # 第三行角度数据
]

U = [
    0.0, 0.1, 0.1, 0.1, 0.0, 0.1, 0.0, 0.1, 0.3,  # 第一行电压数据
    0.3, 0.8, 2.1, 4.4, 3.9, 5.6, 3.1, 0.1, 0.6,  # 第二行电压数据
    0.0, 0.0, 0.0  # 第三行电压数据
]

# 绘图
plt.figure(figsize=(10, 6))

# 绘制曲线
plt.plot(phi_I, U, marker='o', label=r'$U$ (mV)', color='blue', linestyle='-', markersize=8)

# 设置标题和坐标轴标签
plt.title('Data Points and Curve of $U$ vs $\\phi_I$')
plt.xlabel(r'$\phi_I$ (°)')
plt.ylabel(r'$U$ (mV)')

# 添加参考线
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# 设置坐标轴范围
plt.xlim(min(phi_I) - 1, max(phi_I) + 1)  # 横坐标范围
plt.ylim(min(U) - 1, max(U) + 1)  # 纵坐标范围

# 设置坐标刻度
plt.xticks(range(min(phi_I), max(phi_I) + 1, 2))  # 横坐标刻度
plt.yticks(range(int(min(U)), int(max(U)) + 1, 1))  # 纵坐标刻度

# 显示网格
plt.grid()

# 设置图例
plt.legend()

# 显示图形
plt.show()
