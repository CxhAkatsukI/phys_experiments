
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 设置字体为 SimSun（宋体）
font_path = '/usr/share/fonts/TTF/simsun.ttc'
my_font = fm.FontProperties(fname=font_path)

# 定义读取数据的函数
def read_data(file_path):
    x_data = []
    y1_data = []
    y2_data = []
    
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():  # 跳过空行
                values = line.split()
                if len(values) == 3:  # 每行应有3列数据
                    x, y1, y2 = map(float, values)
                    x_data.append(x)
                    y1_data.append(y1)
                    y2_data.append(y2)
                    
    return x_data, y1_data, y2_data

# 定义绘制图像的函数
def plot_closed_curves(x_data, y1_data, y2_data):
    plt.figure(figsize=(2900, 450))

    # 画第一条曲线（第一列 vs 第二列）
    plt.plot(x_data, y1_data, 'bo-', label="第一列 vs 第二列")
    
    # 画第二条曲线（第一列 vs 第三列）
    plt.plot(x_data, y2_data, 'ro-', label="第一列 vs 第三列")

    # 闭合曲线（连接最后一个点和第一个点）
    plt.plot([x_data[0], x_data[-1]], [y1_data[0], y1_data[-1]], 'b-')
    plt.plot([x_data[0], x_data[-1]], [y2_data[0], y2_data[-1]], 'r-')

    # 设置图像标题和标签
    #plt.title("饱和磁滞回线", fontproperties=my_font)
    plt.xlabel("H(A/m)")
    plt.ylabel("B(T)")
    
    # 添加图例并设置字体
    #plt.legend(prop=my_font)

    # 显示图像
    plt.grid(True)
    plt.savefig(output_file, format='pdf', bbox_inches='tight')


# 主程序
if __name__ == "__main__":
    # 假设输入文件名为 "data.txt"，里面有三列数据
    file_path = 'data.txt'
    output_file = 'table1.pdf'  # 输出文件名
    
    # 读取数据
    x_data, y1_data, y2_data = read_data(file_path)
    
    # 画出闭合曲线
    plot_closed_curves(x_data, y1_data, y2_data)

