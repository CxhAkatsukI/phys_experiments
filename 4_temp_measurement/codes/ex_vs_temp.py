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
temperature = np.array([30.9, 35.9, 40.0, 45.1, 50.0])  # 温度 (°C)
electromotive_force = np.array([1.098, 1.350, 1.520, 1.728, 1.930])  # 电动势 (mV)

# 线性拟合
slope, intercept, r_value, p_value, std_err = linregress(temperature, electromotive_force)

# 拟合直线方程
fit_line = slope * temperature + intercept

# 输出拟合结果
print(f"Linear fit equation: E_x = {slope:.4f} * t + {intercept:.4f}")
print(f"Regression coefficient (R^2): {r_value**2:.4f}")
print(f"Thermoelectric coefficient (α): {slope:.4f} mV/°C")

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter(temperature, electromotive_force, color='blue', label='Data points')
plt.plot(temperature, fit_line, color='red', linestyle='--', label=f'Fit: $E_x = {slope:.4f}t + {intercept:.4f}$')
plt.title('Thermocouple Electromotive Force vs Temperature', fontsize=14)
plt.xlabel('Temperature $t$ (°C)', fontsize=12)
plt.ylabel('Electromotive Force $E_x$ (mV)', fontsize=12)

# 在图中添加回归系数 (R²) 和热电偶温差电系数 (α)
plt.text(31, 1.6, f'$\\alpha = {slope:.4f}$ mV/°C', fontsize=12, color='black')
plt.text(31, 1.5, f'$R^2 = {r_value**2:.4f}$', fontsize=12, color='black')

plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()

# 保存图像（可选）
# plt.savefig('thermocouple_curve.png', dpi=300)

plt.show()
