import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from scipy.interpolate import UnivariateSpline

# 设置字体为 SimSun（宋体）
font_path = '/usr/share/fonts/TTF/simsun.ttc'  # 请根据实际路径调整
my_font = fm.FontProperties(fname=font_path)

# 定义读取数据的函数，假设每行有两列数据
def read_data(file_path):
    x_data = []
    y_data = []
    
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():  # 跳过空行
                values = line.split()
                if len(values) == 2:  # 每行应有2列数据
                    x, y = map(float, values)
                    x_data.append(x)
                    y_data.append(y)
                    
    return x_data, y_data

# 定义绘制图像的函数，使用平滑拟合
def plot_fitted_curve(x_data, y_data):
    plt.figure(figsize=(8, 6))

    # 使用 UnivariateSpline 进行平滑拟合，s 控制光滑程度
    spline = UnivariateSpline(x_data, y_data, s=500000)  # s=1 表示平滑因子，值越大越平滑
    
    # 绘制原始数据点
    plt.plot(x_data, y_data, 'ro', label="数据点")

    # 在 x 轴生成更多的点，得到平滑曲线
    x_new = np.linspace(min(x_data), max(x_data), 500)
    y_smooth = spline(x_new)

    # 绘制平滑曲线
    plt.plot(x_new, y_smooth, 'b-', label="平滑拟合曲线")

    # 设置图像标题和标签
    plt.xlabel("$H(A/m)$")
    plt.ylabel("$\mu_m$")
    
    # 添加图例
    plt.legend(prop=my_font)

    # 显示图像并保存为PDF
    plt.grid(True)
    plt.savefig(output_file, format='pdf', bbox_inches='tight')

# 主程序
if __name__ == "__main__":
    # 假设输入文件名为 "data.txt"，里面有两列数据
    file_path = 'data.txt'
    output_file = 'table4_2_fitted.pdf'  # 输出文件名
    
    # 读取数据
    x_data, y_data = read_data(file_path)
    
    # 画出平滑的拟合曲线
    plot_fitted_curve(x_data, y_data)

