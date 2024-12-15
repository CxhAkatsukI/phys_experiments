import matplotlib.pyplot as plt
import numpy as np

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# 数据
frequency = np.array([2.050, 2.150, 2.200, 2.231, 2.240, 2.247, 2.250, 2.253, 2.256, 2.265, 2.275, 2.320, 2.400, 2.600])  # 单位：KHz
ch1_ch2 = np.array([1.23, 1.45, 1.50, 1.54, 1.54, 1.50, 1.52, 1.51, 1.54, 1.49, 1.54, 1.45, 1.30, 0.915])  # 单位：V

# 绘制曲线
plt.figure(figsize=(8, 6))
plt.plot(frequency, ch1_ch2, marker='o', linestyle='-', color='b', label=r"$U$")

# 图标题和轴标签
plt.title(r"$U$-$f$ Curve (Parallel Circuit)", fontsize=14)
plt.xlabel(r"$f$ (KHz)", fontsize=12)
plt.ylabel(r"$U$ (V)", fontsize=12)

# 网格与图例
plt.grid(alpha=0.3)
plt.legend(fontsize=10)

# 显示图形
plt.tight_layout()
plt.show()
