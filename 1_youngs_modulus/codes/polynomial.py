import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# 数据点
x_L = np.array([0.111, 0.138, 0.167, 0.194, 0.250, 0.278, 0.306, 0.333])
f_1 = np.array([827.100, 826.812, 826.522, 826.362, 826.492, 826.582, 826.682, 827.172])

# 拟合二次多项式（degree 2）
p = Polynomial.fit(x_L, f_1, 2)

# 提取二次函数的系数，用于显示
coefs = p.convert().coef  # 转换为标准多项式基数以获取系数
quadratic_eq = f"fi = {coefs[2]:.3f} * (x/L)^2 + {coefs[1]:.3f} * (x/L) + {coefs[0]:.3f}"

# 生成拟合曲线的点
x_fit = np.linspace(min(x_L), max(x_L), 100)
y_fit = p(x_fit)

# 绘制图形
plt.figure(figsize=(8, 6))
plt.scatter(x_L, f_1, color='blue', label='Data Points')
plt.plot(x_fit, y_fit, color='red', label=f'Quadratic Fit: {quadratic_eq}')
plt.xlabel(r'$x/L$')
plt.ylabel(r'$f_i$ (Hz)')
plt.title('Quadratic Fit of Resonant Frequency vs Position Ratio')
plt.legend()
plt.grid(True)
plt.show()
