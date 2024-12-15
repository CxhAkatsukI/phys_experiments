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
phi = np.array([85.608, 82.044, 71.280, 46.583, 29.030, 9.7070, 0.0000, -9.7330, -17.868, -39.139, -54.054, -78.509, -84.672, -82.368])  # 单位：度

# 绘制曲线
plt.figure(figsize=(8, 6))
plt.plot(frequency, phi, marker='o', linestyle='-', color='b', label="Phase Shift ($\\varphi$)")

# 图标题和轴标签
plt.title(r"$\varphi-f$ Curve (Parallel Circuit)", fontsize=14)
plt.xlabel(r"$f$ (KHz)", fontsize=12)
plt.ylabel(r"$\varphi$ ($^\circ$)", fontsize=12)

# 网格与图例
plt.grid(alpha=0.3)
plt.legend(fontsize=10)

# 显示图形
plt.tight_layout()
plt.show()
