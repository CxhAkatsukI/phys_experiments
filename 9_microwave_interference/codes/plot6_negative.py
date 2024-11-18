
import matplotlib.pyplot as plt

# 数据定义
data = [
    [30, 31, 32, 33, 34, 35, 36, 37, 38],  # θ (°)
    [5.5, 3.8, 2.8, 2.1, 1.7, 2.0, 2.3, 4.4, 6.7],  # U_θ^+
    [29, 30, 31, 32, 33, 34, 35, 36, 37],  # θ (°)
    [7.2, 4.4, 3.8, 3.7, 4.4, 5.0, 7.6, 9.6, 10.4]   # U_θ^-
]

# 提取横纵坐标
x = [-t for t in data[2]]  # 第三行取负作为横坐标
y = data[3]  # 第四行为纵坐标

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
plt.xlim(-max(data[2]) - 1, -min(data[2]) + 1)  # 横坐标范围
plt.ylim(min(y) - 1, max(y) + 1)  # 纵坐标范围

# 设置坐标刻度
plt.xticks(range(-38, -28, 1))  # 横坐标刻度
plt.yticks(range(int(min(y)), int(max(y)) + 1, 1))  # 纵坐标刻度

# 显示网格
plt.grid()

# 设置图例
plt.legend()

# 显示图形
plt.show()
