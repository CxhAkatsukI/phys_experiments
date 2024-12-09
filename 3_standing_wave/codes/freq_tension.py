import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据
T = np.array([13.34, 26.68, 40.02, 53.37, 66.71])  # T (N)
f1 = np.array([65.79, 83.3, 98.4, 111.1, 135.1])  # f1 (Hz)

# 计算 ln T 和 ln f
ln_T = np.log(T)
ln_f = np.log(f1)

# 线性拟合
slope, intercept, r_value, p_value, std_err = stats.linregress(ln_T, ln_f)

# 绘图
plt.figure(figsize=(8, 6))
plt.plot(ln_T, ln_f, 'o', label="Data points")  # 绘制原始数据点
plt.plot(ln_T, slope * ln_T + intercept, 'r-', label=f"Fit: ln(f) = {slope:.2f} ln(T) + {intercept:.2f}")  # 拟合线

# 添加图例和标签
plt.xlabel(r'$\ln T$ (N)', fontsize=14)
plt.ylabel(r'$\ln f$ (Hz)', fontsize=14)
plt.title('Linear Fit of $\ln f$ vs. $\ln T$', fontsize=16)
plt.legend()

# 显示拟合的斜率和截距
plt.text(0.1, 0.9, f"Fit slope: {slope:.2f}\nFit intercept: {intercept:.2f}", transform=plt.gca().transAxes)

# 显示图形
plt.grid(True)
plt.show()

# 对比理论值
theoretical_slope = 0.5  # 理论斜率
print(f"拟合斜率: {slope:.2f}")
print(f"理论斜率: {theoretical_slope}")
