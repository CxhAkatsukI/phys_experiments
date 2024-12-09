import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 数据
L = np.array([640, 480, 320, 240, 160])  # 有效长度 (mm)
f1 = np.array([56.82, 69.44, 104.2, 138.9, 208.4])  # 频率 (Hz)

import pandas as pd

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 定义拟合函数 (假设是幂函数关系：f1 = a * L^b)
def fit_func(L, a, b):
    return a * L**b

# 执行曲线拟合
params, _ = curve_fit(fit_func, L, f1)
a, b = params  # 提取拟合参数

# 生成平滑曲线
L_fit = np.linspace(min(L), max(L), 500)  # 在 L 范围内生成更多点
f1_fit = fit_func(L_fit, a, b)

# 绘图
plt.figure(figsize=(8, 5))
plt.scatter(L, f1, color='blue', label='Data Points')  # 原始数据点
plt.plot(L_fit, f1_fit, color='red', label=f'Fit: $f_1 = {a:.2f}L^{{{b:.2f}}}$')  # 拟合曲线

# 设置标题和标签
plt.title('Relationship between $f_1$ and $L$', fontsize=14)
plt.xlabel('Effective Length $L$ (mm)', fontsize=12)
plt.ylabel('Frequency $f_1$ (Hz)', fontsize=12)

# 添加网格和图例
plt.grid(alpha=0.3)
plt.legend(fontsize=12)

# 反转 x 轴（因为长度 L 通常由大到小）
plt.gca().invert_xaxis()

# 显示图形
plt.tight_layout()
plt.show()
