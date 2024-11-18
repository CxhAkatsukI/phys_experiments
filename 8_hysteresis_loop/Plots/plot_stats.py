import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

# 设置 seaborn 风格
sns.set(style="whitegrid")

def load_data(file_path):
    """
    加载 CSV 数据。
    :param file_path: 数据文件路径
    :return: Pandas DataFrame
    """
    try:
        data = pd.read_csv(file_path)
        print(f"数据成功加载：\n{data.head()}")
        return data
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return None

def plot_bar(data, x_column, y_column):
    """
    绘制柱状图。
    :param data: DataFrame 数据
    :param x_column: X 轴数据列名
    :param y_column: Y 轴数据列名
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_column, y=y_column, data=data)
    plt.title(f'{x_column} vs {y_column} 柱状图')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("fig.pdf")

def plot_scatter(data, x_column, y_column):
    """
    绘制散点图。
    :param data: DataFrame 数据
    :param x_column: X 轴数据列名
    :param y_column: Y 轴数据列名
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_column, y=y_column, data=data)
    plt.title(f'{x_column} vs {y_column} 散点图')
    plt.tight_layout()
    plt.show()

def plot_line(data, x_column, y_column):
    """
    绘制折线图。
    :param data: DataFrame 数据
    :param x_column: X 轴数据列名
    :param y_column: Y 轴数据列名
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_column, y=y_column, data=data)
    plt.title(f'{x_column} vs {y_column} 折线图')
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="根据数据绘制统计图")
    parser.add_argument("file", help="CSV 数据文件路径")
    parser.add_argument("x_column", help="X 轴数据列名")
    parser.add_argument("y_column", help="Y 轴数据列名")
    parser.add_argument("--plot_type", choices=["bar", "scatter", "line"], default="bar", help="选择绘图类型")

    args = parser.parse_args()

    data = load_data(args.file)
    if data is None:
        return

    if args.plot_type == "bar":
        plot_bar(data, args.x_column, args.y_column)
    elif args.plot_type == "scatter":
        plot_scatter(data, args.x_column, args.y_column)
    elif args.plot_type == "line":
        plot_line(data, args.x_column, args.y_column)

if __name__ == "__main__":
    main()
