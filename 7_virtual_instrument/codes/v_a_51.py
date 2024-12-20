import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据：电压 (V) 和 电流 (A)
voltage = [
    -0.000322004, 0.0164222, 0.0338104, 0.0499106, 0.0669768, 0.083721,
    0.0998212, 0.117209, 0.134598, 0.150698, 0.168086, 0.184508,
    0.200931, 0.217031, 0.234419, 0.251485, 0.268873, 0.284974,
    0.301074, 0.31814, 0.335528
]

current = [
    3.27E-06, 0.00032849, 0.000650494, 0.000988598, 0.00131704, 0.00163905,
    0.00198037, 0.00229915, 0.00263082, 0.00295926, 0.00328449, 0.00362259,
    0.00394781, 0.00427948, 0.00460792, 0.00493315, 0.00525837, 0.00559003,
    0.00592492, 0.00625658, 0.00657859
]

# 使用线性回归计算电压和电流之间的关系（即计算斜率）
slope, intercept, r_value, p_value, std_err = linregress(voltage, current)

# 计算电阻（电阻 = 斜率的倒数）
resistance = 1 / slope

# 创建一个图形
plt.figure(figsize=(8, 6))

# 绘制伏安特性曲线
plt.plot(voltage, current, marker='o', color='b', label='V-I Curve')

# 绘制线性回归直线
plt.plot(voltage, slope * np.array(voltage) + intercept, color='r', linestyle='--', label=f'Linear Fit: Slope = {slope:.2f} $\\Omega ^{-1}$')

# 设置标题和标签
plt.title('Voltage-Current Characteristics of 51 Ohm Resistor', fontsize=14)
plt.xlabel('Voltage (V)', fontsize=12)
plt.ylabel('Current (A)', fontsize=12)

# 添加网格
plt.grid(True)

# 显示图例
plt.legend(loc='best')

# 在图中添加电阻值 (即斜率的倒数)，使用LaTeX格式并保留五位小数
text_str = r'$\mathrm{Resistance\ (R)} \approx ' + f'{resistance:.5f} \, \\Omega$'
plt.text(-0.012, 0.0055, text_str, fontsize=12, color='black', backgroundcolor='white')

# 显示图形
plt.show()
