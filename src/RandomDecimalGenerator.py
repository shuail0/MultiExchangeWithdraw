import pandas as pd
import numpy as np

def generate_random_decimals(min_val, max_val, precision, count):
    # 生成指定数量的随机小数，然后根据精度调整
    random_numbers = np.random.uniform(min_val, max_val, count)
    random_numbers = np.around(random_numbers, decimals=precision)
    return random_numbers

# 设定参数
min_val = 0.0135  # 最小值
max_val = 0.0145  # 最大值
precision = 4  # 小数精度
count = 99  # 生成数量

# 生成随机小数
random_numbers = generate_random_decimals(min_val, max_val, precision, count)

# 将随机小数保存为CSV文件
df = pd.DataFrame(random_numbers, columns=["RandomNumbers"])
df.to_csv("../data/output/random_numbers.csv", index=False)
