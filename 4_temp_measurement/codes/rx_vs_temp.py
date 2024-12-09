import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据
temperature = np.array([30.9, 35.2, 40.0, 45.1, 50.2])  # 温度 (°C)
resistance = np.array([58.8, 59.8, 60.8, 62.0, 63.0])  # 电阻 (Ω)

# 线性拟合
slope, intercept, r_value, p_value, std_err = linregress(temperature, resistance)

# 拟合直线方程
fit_line = slope * temperature + intercept

# 计算温度系数 alpha
alpha = slope / intercept

# 输出拟合结果
print(f"Linear fit equation: $R_x = {slope:.4f} * t + {intercept:.4f}$")
print(f"Regression coefficient (R^2): {r_value**2:.4f}")
print(f"Thermal coefficient of resistance ($\\alpha$): {alpha:.4f} 1/°C")

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter(temperature, resistance, color='blue', label='Data points')
plt.plot(temperature, fit_line, color='red', linestyle='--', label=f'Fit: $R_x = {slope:.4f}t + {intercept:.4f}$')

# 在图中添加截距 R_{x0} 和温度系数 α
plt.text(31, 59.5, r'$R_{x0} = %.4f \, \Omega$' % intercept, fontsize=12, color='black')
plt.text(31, 59.0, r'$\alpha = %.4f \ $' % alpha, fontsize=12, color='black')

# 标题和标签
plt.title(r'Copper Resistance vs Temperature', fontsize=14)
plt.xlabel(r'Temperature $t$ (°C)', fontsize=12)
plt.ylabel(r'Resistance $R_x$ ($\Omega$)', fontsize=12)

# 图例
plt.legend(fontsize=10)

# 网格
plt.grid(alpha=0.3)

# 调整布局
plt.tight_layout()

# 保存图像（可选）
# plt.savefig('copper_resistance_curve.png', dpi=300)

plt.show()
