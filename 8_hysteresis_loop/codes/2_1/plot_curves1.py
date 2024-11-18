import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from scipy.interpolate import interp1d

# 设置字体为 SimSun（宋体）
font_path = '/usr/share/fonts/TTF/simsun.ttc'  # 请根据实际路径调整
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
    plt.figure(figsize=(8, 6))

    # 创建插值函数
    x_new = np.linspace(min(x_data), max(x_data), 300)  # 生成更多的x点用于平滑
    y1_interp = interp1d(x_data, y1_data, kind='cubic')  # 立方插值
    y2_interp = interp1d(x_data, y2_data, kind='cubic')  # 立方插值

    # 画第一条平滑曲线（第一列 vs 第二列）
    plt.plot(x_new, y1_interp(x_new), 'b-', label="第一列 vs 第二列")
    
    # 画第二条平滑曲线（第一列 vs 第三列）
    plt.plot(x_new, y2_interp(x_new), 'r-', label="第一列 vs 第三列")

    # 设置图像标题和标签
    plt.title("平滑的磁滞回线", fontproperties=my_font)
    plt.xlabel("第一列 (X)", fontproperties=my_font)
    plt.ylabel("第二列/第三列 (Y)", fontproperties=my_font)
    
    # 添加图例
    plt.legend(prop=my_font)

    # 显示图像
    plt.grid(True)
    plt.savefig(output_file, format='pdf', bbox_inches='tight')

# 主程序
if __name__ == "__main__":
    # 假设输入文件名为 "data.txt"，里面有三列数据
    file_path = 'data.txt'
    output_file = 'magnetic_hysteresis1.pdf'  # 输出文件名
    
    # 读取数据
    x_data, y1_data, y2_data = read_data(file_path)
    
    # 画出平滑的磁滞回线
    plot_closed_curves(x_data, y1_data, y2_data)

