import matplotlib.pyplot as plt

# 数据
theta = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
U_theta_plus = [24.3, 35.5, 26.7, 19.5, 3.4, 0.2, 0.1, 0.8, 2.8, 11.9, 20.4, 25.1, 21.0, 9.8, 2.3, 0.9, 0.6, 0.4, 0.6, 1.2, 1.1, 0.5, 0.3, 2.0, 6.2, 4.0]
U_theta_minus = [24.3, 22.5, 16.9, 7.8, 1.3, 0.1, 0.4, 1.3, 3.9, 13.4, 24.5, 27.5, 17.4, 6.2, 1.7, 0.9, 0.8, 0.8, 1.5, 1.5, 0.7, 0.3, 1.0, 3.9, 4.7, 1.2]

# 创建图表
plt.figure(figsize=(8, 8))

# 画第一组点：{以第一列为横坐标，以第二列为纵坐标}
plt.plot(theta, U_theta_plus, 'o-', label=r'$(\theta, U_\theta^+)$')

# 画第二组点：{以第一列取负值后为横坐标，以第三列为纵坐标}
neg_theta = [-x for x in theta]
plt.plot(neg_theta, U_theta_minus, 's-', label=r'$(-\theta, U_\theta^-)$')

# 设置坐标轴标签
plt.xlabel(r'$\theta$ (°)', fontsize=12)
plt.ylabel(r'$U_\theta$ (mV)', fontsize=12)

# 添加图例
plt.legend()

# 添加网格
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 显示网格
plt.grid(True)

# 显示图表
plt.title('点图及曲线')
plt.show()
plt.savefig(output_file, format='pdf', bbox_inches='tight')

