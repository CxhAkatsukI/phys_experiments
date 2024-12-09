import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据：周期T和质量m
mass = np.array([217.12, 229.48, 241.95, 251.69, 264.23])  # 质量 (g)
T = np.array([1570.844, 1614.778, 1657.335, 1698.388, 1739.027])  # 周期 (ms)

# 计算 T^2
T_squared = T**2

# 线性拟合：T^2 与 m 的关系
slope, intercept, r_value, p_value, std_err = linregress(mass, T_squared)

# 绘图
plt.figure(figsize=(8, 6))

# 绘制 T^2 与 m 的关系
plt.plot(mass, T_squared, 'bo-', label=r'$\mathbf{T^2}$ vs $m$')
plt.plot(mass, slope * mass + intercept, 'r--', label=f'Fit: $T^2 = {slope:.4f}m + {intercept:.4f}$')

# 标注拟合方程、斜率、截距和回归系数
plt.text(217.22, 2910000, r'$\mathbf{T^2} = %.4f m + %.4f$' % (slope, intercept), fontsize=12, color='black')
plt.text(217.22, 2860000, r'$\mathbf{Slope} = %.4f$' % slope, fontsize=12, color='black')
plt.text(217.22, 2810000, r'$\mathbf{Intercept} = %.4f$' % intercept, fontsize=12, color='black')
plt.text(217.22, 2760000, r'$\mathbf{R^2} = %.4f$' % r_value**2, fontsize=12, color='black')

# 标题和标签
plt.title(r'$T^2$ vs Mass (m)', fontsize=14)
plt.xlabel('Mass $m$ (g)', fontsize=12)
plt.ylabel('$T^2$ (ms$^2$)', fontsize=12)

# 图例
plt.legend(fontsize=10)

# 网格
plt.grid(alpha=0.3)

# 调整布局
plt.tight_layout()

# 显示图像
plt.show()

# 输出拟合结果
print(f"Linear fit equation: $T^2 = {slope:.4f}m + {intercept:.4f}$")
print(f"Regression coefficient (R²): {r_value**2:.4f}")
