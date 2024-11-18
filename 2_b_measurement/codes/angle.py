import numpy as np
import matplotlib.pyplot as plt

# 数据
theta = np.array([
    0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 
    100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 
    200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 
    300, 310, 320, 330, 340, 350, 360
])
u_measured = np.array([
    8.68, 8.52, 8.17, 7.56, 6.75, 5.72, 4.49, 3.11, 1.61, 0.11, 
    1.37, 2.90, 4.31, 5.56, 6.62, 7.52, 8.17, 8.54, 8.62, 8.43, 
    8.04, 7.31, 6.42, 5.34, 3.86, 2.55, 0.94, 0.54, 1.98, 3.38, 
    4.69, 5.81, 6.78, 7.68, 8.24, 8.59, 8.67
])
u_theoretical = np.abs(8.68 * np.cos(np.radians(theta)))  # 理论值取绝对值

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(theta, u_measured, 'o-', label="Measured $U$ (mV)", color='blue', markersize=5)
plt.plot(theta, u_theoretical, '--', label="Theoretical $U = |U_{max}\\cosθ|$", color='red')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')

# 图例、标题和标签
plt.title("Induced Voltage vs Coil Angle")
plt.xlabel("Angle $\\theta$ (degrees)")
plt.ylabel("Voltage $U$ (mV)")
plt.legend()
plt.grid(True)

# 显示图像
plt.tight_layout()
plt.show()
