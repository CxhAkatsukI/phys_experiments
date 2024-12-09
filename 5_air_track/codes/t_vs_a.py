import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据：振幅和周期
amplitude = np.array([10, 20, 30, 40])  # 振幅（cm）
T = np.array([1574.076, 1569.916, 1569.204, 1568.395])  # 周期 (ms)

# 拟合线性回归
slope, intercept, r_value, p_value, std_err = linregress(amplitude, T)

# 绘制第一个图（纵坐标尺度较大）
plt.figure(figsize=(8, 6))

# 绘制 T-A 关系图
plt.subplot(2, 1, 1)
plt.plot(amplitude, T, 'bo-', label=r'$\mathbf{T-A}$ Relation')
plt.plot(amplitude, slope * amplitude + intercept, 'r--', label=f'Fit: $T = {slope:.4f}A + {intercept:.4f}$')
plt.title(r'$T-A$ Relation (Larger Scale)', fontsize=14)
plt.xlabel('Amplitude (cm)', fontsize=12)
plt.ylabel('Period $T$ (ms)', fontsize=12)
plt.legend()
plt.grid(True)

# 绘制第二个图（纵坐标尺度较小）
plt.subplot(2, 1, 2)
plt.plot(amplitude, T, 'bo-', label=r'$\mathbf{T-A}$ Relation')
plt.plot(amplitude, slope * amplitude + intercept, 'r--', label=f'Fit: $T = {slope:.4f}A + {intercept:.4f}$')
plt.title(r'$T-A$ Relation (Smaller Scale)', fontsize=14)
plt.xlabel('Amplitude (cm)', fontsize=12)
plt.ylabel('Period $T$ (ms)', fontsize=12)
plt.ylim(0, 1700)  # 设置更小的纵坐标范围
plt.legend()
plt.grid(True)

# 调整布局
plt.tight_layout()

# 显示图像
plt.show()

# 输出拟合结果
print(f"Linear fit equation: $T = {slope:.4f}A + {intercept:.4f}$")
print(f"Regression coefficient (R²): {r_value**2:.4f}")
