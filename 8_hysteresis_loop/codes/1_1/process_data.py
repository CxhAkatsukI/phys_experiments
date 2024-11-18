
def process_data(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # 写入表格开头部分
        outfile.write("\t\\begin{tabularx}{\\textwidth}{|X|X|X|X|}\n")
        outfile.write("\t\\hline\n")
        outfile.write("\t $I(mA)$ & $B(mT)$ & $H(A/m)$ & 修正$H(A/m)$ \\\\\n")
        outfile.write("\t\\hline\n")


        for line in infile:
            # 定义变量
            R1 = 2.0
            R2 = 20000
            C = 2 * 10 ** (-6)
            N = 2000
            N1 = 150
            N2 = 150
            S = 1.24 * 10 ** (-4)
            L = 2.4 * 10 ** (-1)
            
            # 读取每一行，并将数据拆分成三列
            data = line.split()
            if len(data) != 2:
                continue  # 跳过不符合格式的行
            
            # 转换为浮点数
            col1, col2 = map(float, data)

            #通过电流对磁场H进行计算
            H = N * col1 * 10 ** (-3) / L
            H1 = H - (2 * col2 * 10 ** (-6) / (L * 4 * 3.14159 * 10 ** (-7)))
            
            # 对H进行计算
            #col2 = col2 * 10 ** (-3) * N1 / (L * R1)
            
            # 对B进行计算
            #col2 = col2 * 10 ** (-3) * R2 * C / (N2 * S)
            #col3 = col3 * 10 ** (-3) * R2 * C / (N2 * S)
            
            #M = col3 / (col2 * 4 * 3.14159 * 10 ** (-7))

            # 写入处理后的数据到输出文件
            outfile.write(f"\t{col1:.3f} & {col2:.3f} & {H:.3f} & {H1:.3f} \\\\\n")
            outfile.write("\t\\hline\n")

        # 写入表格结束部分
        outfile.write("\t\\end{tabularx}\n")

# 使用方法
input_file = 'input.txt'   # 输入文件路径
output_file = 'output.txt' # 输出文件路径
process_data(input_file, output_file)

