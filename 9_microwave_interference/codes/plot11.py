import matplotlib.pyplot as plt

# 数据提取
phi_I = [52, 53, 54, 55, 56, 57, 58, 59, 60, 61]  # 角度数据
U = [14.7, 23.2, 29.2, 30.3, 26.8, 30.5, 38.4, 38.9, 20.8, 3.8]  # 电压数据

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
plt.ylim(min(U) - 5, max(U) + 5)  # 纵坐标范围

# 设置坐标刻度
plt.xticks(range(min(phi_I), max(phi_I) + 1, 1))  # 横坐标刻度
plt.yticks(range(int(min(U)), int(max(U)) + 10, 5))  # 纵坐标刻度

# 显示网格
plt.grid()

# 设置图例
plt.legend()

# 显示图形
plt.show()

