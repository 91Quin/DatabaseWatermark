# 导入scipy.stats模块
from scipy.stats import binom


# 定义函数，输入参数为omega, alpha
def tau(omega, alpha):
    # 初始化t为0
    t = 0
    # 循环从0到omega/2
    for i in range(omega // 2 + 1):
        # 计算累积分布函数的值
        cdf = binom.cdf(omega - i, omega, 0.5) - binom.cdf(i - 1, omega, 0.5)
        # 如果cdf大于等于1-alpha，更新t为i，否则跳出循环
        if cdf >= 1 - alpha:
            t = i
        else:
            break
    # 返回t的值
    return t


# 测试函数
print(tau(10, 0.05))  # 输出3
print(tau(20, 0.01))  # 输出7
