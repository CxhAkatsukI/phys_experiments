
import matplotlib.pyplot as plt

# 数据定义
data = [
    [8, 9, 10, 11, 12, 13, 14, 15, 16],  # θ (°)
    [22.3, 2.6, 0.5, 0.1, 0.4, 1.3, 3.1, 7.1, 15.3]  # U_θ^+ (mV)
]

# 提取横纵坐标
x = data[0]  # 横坐标 θ (°)
y = data[1]  # 纵坐标 U_θ^+ (mV)

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
