import matplotlib.pyplot as plt
import numpy as np

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据：电压 (V) 和 电流 (A)（稳压二极管）
voltage_diode = [
    -0.00161002, 0.0682648, 0.13814, 0.209303, 0.278533, 0.348086,
    0.418605, 0.487514, 0.557711, 0.624044, 0.677818, 0.709053,
    0.726119, 0.738999, 0.747693, 0.754778, 0.762184, 0.766048,
    0.770556, 0.773776, 0.77764, 0.780538, 0.783759, 0.786013,
    0.788267, 0.790843, 0.794063, 0.795995, 0.797605, 0.797927,
    0.796961
]

current_diode = [
    9.71E-06, 1.29E-05, 1.61E-05, 3.27E-06, 9.71E-06, 1.29E-05,
    1.61E-05, 1.61E-05, 2.26E-05, 5.16E-05, 0.000212569, 0.000602194,
    0.00112384, 0.00169057, 0.00229593, 0.0029174, 0.00354209, 0.00419576,
    0.00484621, 0.00550309, 0.00615354, 0.00682009, 0.00748342, 0.00815641,
    0.00882618, 0.00949272, 0.0101625, 0.010829, 0.0113829, 0.0112637,
    0.0111993
]

# 创建一个图形
plt.figure(figsize=(8, 6))

# 绘制伏安特性曲线
plt.plot(voltage_diode, current_diode, marker='o', color='b', label='V-I Curve of Diode')

# 设置标题和标签
plt.title('Voltage-Current Characteristics of Zener Diode', fontsize=14)
plt.xlabel('Voltage (V)', fontsize=12)
plt.ylabel('Current (A)', fontsize=12)

# 添加网格
plt.grid(True)

# 显示图例
plt.legend(loc='best')

# 显示图形
plt.show()
