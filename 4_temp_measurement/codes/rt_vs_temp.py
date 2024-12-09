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
temperature_celsius = np.array([30.9, 35.4, 40.0, 45.1, 50.4])  # 摄氏温度 (°C)
resistance_T = np.array([1944.0, 1601.0, 1335.0, 1091.0, 890.0])  # 热敏电阻 (Ω)

# 转换为热力学温度 T (K)
temperature_kelvin = temperature_celsius + 273.15

# 绘制 R_T ~ t 曲线
plt.figure(figsize=(8, 6))

# 绘制电阻 R_T 和温度 t 的关系
plt.subplot(2, 1, 1)
plt.scatter(temperature_celsius, resistance_T, color='blue', label=r'$R_T$ vs $t$')
plt.plot(temperature_celsius, resistance_T, color='red', linestyle='--')
plt.title(r'$\mathbf{R_T}$ vs Temperature', fontsize=14)
plt.xlabel(r'Temperature $t$ (°C)', fontsize=12)
plt.ylabel(r'Resistance $R_T$ ($\Omega$)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=10)

# 计算 ln(R_T) 和 1/T
ln_R_T = np.log(resistance_T)
inverse_temperature = 1 / temperature_kelvin

# 线性拟合 ln(R_T) ~ 1/T
slope, intercept, r_value, p_value, std_err = linregress(inverse_temperature, ln_R_T)

# 拟合直线方程
fit_line = slope * inverse_temperature + intercept

# 计算 A 和 B
A = np.exp(intercept)
B = slope

# 绘制 ln(R_T) ~ 1/T 曲线
plt.subplot(2, 1, 2)
plt.scatter(inverse_temperature, ln_R_T, color='green', label=r'$\ln R_T$ vs $1/T$')
plt.plot(inverse_temperature, fit_line, color='orange', linestyle='--', label=f'Fit: $\ln R_T = {B:.4f} (1/T) + \ln A$')

# 在图中标注回归系数和特性常数 A 和 B
plt.text(0.00309, 7.29, r'$\mathbf{B = %.4f}$' % B, fontsize=12, color='black')
plt.text(0.00309, 7.20, r'$\mathbf{A = %.4f}$' % A, fontsize=12, color='black')

plt.title(r'$\ln R_T$ vs $1/T$', fontsize=14)
plt.xlabel(r'$1/T$ (K$^{-1}$)', fontsize=12)
plt.ylabel(r'$\ln R_T$', fontsize=12)
plt.grid(True)
plt.legend(fontsize=10)

# 调整布局
plt.tight_layout()

# 显示图像
plt.show()

# 输出结果
print(f"Linear fit equation for ln(R_T): ln(R_T) = {B:.4f} (1/T) + ln(A)")
print(f"Regression coefficient (R^2): {r_value**2:.4f}")
print(f"Thermal resistance characteristic constant A: {A:.4f}")
print(f"Thermal resistance characteristic constant B: {B:.4f}")
