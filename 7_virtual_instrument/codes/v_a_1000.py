import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据：电压 (V) 和 电流 (A) (1000欧姆电阻)
voltage_1000 = [
    -0.00128802, 0.452094, 0.906763, 1.36079, 1.81482, 2.26917,
    2.72287, 3.17819, 3.63125, 4.08464, 4.53867, 4.99303,
    5.44642, 5.9011, 6.35513, 6.80885, 7.26353, 7.71693,
    8.17098, 8.62438, 9.07875
]

current_1000 = [
    1.29E-05, 0.000466952, 0.000914537, 0.00137178, 0.00182581, 0.00227983,
    0.0027403, 0.0031911, 0.00364835, 0.0041056, 0.00456284, 0.00502009,
    0.00547411, 0.00592814, 0.00638216, 0.00683941, 0.00729022, 0.0077539,
    0.00821115, 0.00866517, 0.00912242
]

# 使用线性回归计算电压和电流之间的关系（即计算斜率）
slope_1000, intercept_1000, r_value_1000, p_value_1000, std_err_1000 = linregress(voltage_1000, current_1000)

# 计算电阻（电阻 = 斜率的倒数）
resistance_1000 = 1 / slope_1000

# 创建一个图形
plt.figure(figsize=(8, 6))

# 绘制伏安特性曲线
plt.plot(voltage_1000, current_1000, marker='o', color='b', label='V-I Curve')

# 绘制线性回归直线
plt.plot(voltage_1000, slope_1000 * np.array(voltage_1000) + intercept_1000, color='r', linestyle='--', label=f'Linear Fit: Slope = {slope_1000:.2f} $\\Omega ^{-1}$')

# 设置标题和标签
plt.title('Voltage-Current Characteristics of 1k Ohm Resistor', fontsize=14)
plt.xlabel('Voltage (V)', fontsize=12)
plt.ylabel('Current (A)', fontsize=12)

# 添加网格
plt.grid(True)

# 显示图例
plt.legend(loc='best')

# 在图中添加电阻值 (即斜率的倒数)，使用LaTeX格式并保留五位小数
text_str_1000 = r'$\mathrm{Resistance\ (R)} \approx ' + f'{resistance_1000:.5f} \, \\Omega$'
plt.text(-0.25, 0.008, text_str_1000, fontsize=12, color='black', backgroundcolor='white')

# 显示图形
plt.show()
