import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据：位置 (cm) 和速度 V (cm/s)
position = np.array([10, 15, 20, 25, 30])  # 位置 (cm)
velocity = np.array([143.890, 139.977, 128.99, 116.313, 93.357])  # 速度 (cm/s)

# 计算 v^2 和 x^2
v_squared = velocity**2
x_squared = position**2

# 线性拟合：v^2 与 x^2 的关系
slope, intercept, r_value, p_value, std_err = linregress(x_squared, v_squared)

# 绘图
plt.figure(figsize=(8, 6))

# 绘制 v^2 与 x^2 的关系
plt.plot(x_squared, v_squared, 'bo-', label=r'$\mathbf{v^2}$ vs $x^2$')
plt.plot(x_squared, slope * x_squared + intercept, 'r--', label=f'Fit: $v^2 = {slope:.4f} x^2 + {intercept:.4f}$')

# 标注拟合方程、斜率和截距
plt.text(100, 13000, r'$\mathbf{v^2} = %.4f x^2 + %.4f$' % (slope, intercept), fontsize=12, color='black')
plt.text(100, 12000, r'$\mathbf{Slope} = %.4f$' % slope, fontsize=12, color='black')
plt.text(100, 11000, r'$\mathbf{Intercept} = %.4f$' % intercept, fontsize=12, color='black')
plt.text(100, 10000, r'$\mathbf{R^2} = %.4f$' % r_value**2, fontsize=12, color='black')

# 标题和标签
plt.title(r'$v^2$ vs $x^2$', fontsize=14)
plt.xlabel(r'$x^2$ (cm$^2$)', fontsize=12)
plt.ylabel(r'$v^2$ (cm$^2$/s$^2$)', fontsize=12)

# 图例
plt.legend(fontsize=10)

# 网格
plt.grid(alpha=0.3)

# 调整布局
plt.tight_layout()

# 显示图像
plt.show()

# 输出拟合结果
print(f"Linear fit equation: $v^2 = {slope:.4f} x^2 + {intercept:.4f}$")
print(f"Regression coefficient (R²): {r_value**2:.4f}")
