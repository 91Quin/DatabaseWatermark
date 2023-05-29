# 导入matplotlib.pyplot模块
import matplotlib.pyplot as plt

Num = 5


# 定义一个函数，用于读取csv文件的第三列数据
def read_column(filename):
    data = []  # 创建一个空列表，用于存储数据
    with open(filename, "r") as f:  # 打开文件
        for line in f:  # 遍历每一行
            line = line.strip()  # 去掉行尾的换行符
            if line:  # 如果行不为空
                items = line.split(",")  # 用逗号分隔每一项
                data.append(float(items[Num - 1]))  # 将第三项转换为浮点数，并添加到列表中
    return data  # 返回列表


# 定义四个csv文件的名称
files = [
    "test.csv",
    "test-Marked-Key.233-r.2-LSB.20.csv",
    "test-Marked-Key.12345-r.2-LSB.20.csv",
    "test-Marked-Key.456789-r.2-LSB.20.csv",
]

# 定义四种颜色，用于区分不同的散点图
colors = ["red", "green", "blue", "yellow"]

# 创建一个图形对象，设置大小和分辨率
plt.figure(figsize=(10, 10), dpi=100)

# 遍历每个文件，绘制散点图
for i, file in enumerate(files):
    y = read_column(file)  # 调用函数，读取第三列数据
    x = range(1, len(y) + 1)  # 生成横轴数据，从1开始，与纵轴数据长度相同
    plt.scatter(x, y, c=colors[i], label=file)  # 绘制散点图，设置颜色和标签

# 设置横轴和纵轴的标签
plt.xlabel("Row Number")
plt.ylabel("Attribute " + str(Num))

# 设置标题
plt.title("Different Key")

# 显示图例
plt.legend()

# 保存图形到本地
# plt.savefig('scatter.png')

# 显示图形
plt.show()
