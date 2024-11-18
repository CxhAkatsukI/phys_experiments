import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 设置字体为 SimSun（宋体）
font_path = '/usr/share/fonts/TTF/simsun.ttc'
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

# 定义绘制图像的函数
def plot_closed_curves(x_data, y_data):
    plt.figure(figsize=(8, 6))

    # 绘制曲线
    plt.plot(x_data, y_data, 'bo-', label="H vs B")

    # 闭合曲线（连接最后一个点和第一个点）
    #plt.plot([x_data[0], x_data[-1]], [y_data[0], y_data[-1]], 'b-')

    # 设置图像标题和标签
    plt.xlabel("$H(A/m)$")
    plt.ylabel("$\mu_i$")
    
    # 显示图像并保存为PDF
    plt.grid(True)
    plt.savefig(output_file, format='pdf', bbox_inches='tight')

# 主程序
if __name__ == "__main__":
    # 假设输入文件名为 "data.txt"，里面有两列数据
    file_path = 'data.txt'
    output_file = 'table6.pdf'  # 输出文件名
    
    # 读取数据
    x_data, y_data = read_data(file_path)
    
    # 画出闭合曲线
    plot_closed_curves(x_data, y_data)

