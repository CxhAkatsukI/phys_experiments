
import matplotlib.pyplot as plt

# 数据定义
data = [
    [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],  # θ (°)
    [5.7, 11.0, 15.3, 20.1, 23.1, 25.0, 24.8, 22.0, 17.2, 10.5, 5.8]   # U_θ^+ (mV)
]

# 提取横纵坐标
x = data[0]  # 横坐标
y = data[1]  # 纵坐标

# 绘图
plt.figure(figsize=(10, 6))

# 绘制曲线
plt.plot(x, y, marker='o', label=r'$U_\theta^+$ (mV)', color='blue', linestyle='-', markersize=8)

# 设置标题和坐标轴标签
plt.title('Data Points and Curve of $U_\theta^+$')
plt.xlabel(r'$\theta$ (°)')
plt.ylabel(r'$U_\theta^+$ (mV)')

# 添加参考线
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# 设置坐标轴范围
plt.xlim(min(x) - 1, max(x) + 1)
plt.ylim(min(y) - 1, max(y) + 1)

# 设置坐标刻度
plt.xticks(range(min(x), max(x) + 1, 1))  # 横坐标刻度
plt.yticks(range(int(min(y)), int(max(y)) + 1, 1))  # 纵坐标刻度

# 显示网格
plt.grid()

# 设置图例
plt.legend()

# 显示图形
plt.show()
