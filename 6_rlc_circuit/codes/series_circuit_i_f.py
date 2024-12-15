import matplotlib.pyplot as plt
import numpy as np

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据
frequencies = np.array([1.88, 2.00, 2.08, 2.15, 2.19, 2.22, 2.240, 2.25, 2.26, 2.275, 2.30, 2.36, 2.43, 2.62, 3.18])
currents = np.array([3.13, 5.00, 7.49, 10.2, 12.3, 14.5, 14.6, 15.2, 14.5, 14.7, 13.0, 9.47, 7.79, 3.57, 1.92])

# 绘图
plt.figure(figsize=(8, 6))
plt.plot(frequencies, currents, marker='o', linestyle='-', color='b', label='Current')

# 添加标题和标签
plt.title("$i-f$ Curve for Series Circuit", fontsize=14)
plt.xlabel("$f$ (kHz)", fontsize=12)
plt.ylabel("$i$ (mA)", fontsize=12)

# 添加网格和图例
plt.grid(alpha=0.5)
plt.legend(loc="best", fontsize=10)

# 显示图形
plt.tight_layout()
plt.show()
