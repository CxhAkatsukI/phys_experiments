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
current = np.array([179.6, 112.2, 59.8, 30.4, 39.8, 21.2, 20.8, 21.0, 22.0, 28.4, 35.8, 76.2, 153.2, 282.0])  # 单位：µA

# 绘制曲线
plt.figure(figsize=(8, 6))
plt.plot(frequency, current, marker='o', linestyle='-', color='b', label=r"$i$")

# 图标题和轴标签
plt.title(r"$i$-$f$ Curve (Parallel Circuit)", fontsize=14)
plt.xlabel(r"$f$ (KHz)", fontsize=12)
plt.ylabel(r"$i$ ($\mu$A)", fontsize=12)

# 网格与图例
plt.grid(alpha=0.3)
plt.legend(fontsize=10)

# 显示图形
plt.tight_layout()
plt.show()
