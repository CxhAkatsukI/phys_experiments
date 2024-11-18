import numpy as np
import matplotlib.pyplot as plt

# 数据
frequency = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])  # 频率 f (Hz)
magnetic_field = np.array([0.2121, 0.2107, 0.2114, 0.2113, 0.2112, 0.2111, 0.2107, 0.2107, 0.2110, 0.2112, 0.2112])  # 磁场强度 (mT)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(frequency, magnetic_field, 'o-', color='blue', markersize=6, label="Measured Magnetic Field $B$ (mT)")

# 图例、标题和标签
plt.title("$B$ vs $f$: Magnetic Field vs Frequency", fontsize=14)
plt.xlabel("Frequency $f$ (Hz)", fontsize=12)
plt.ylabel("Magnetic Field $B$ (mT)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# 显示图像
plt.tight_layout()
plt.show()
