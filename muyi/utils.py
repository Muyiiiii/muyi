import os
import csv
import sys

class bcolors:
    HEADER = '\033[95m'    # 紫色，用于标题
    OKBLUE = '\033[94m'    # 蓝色，用于正常或信息性消息
    OKCYAN = '\033[96m'    # 青色（浅蓝色），用于信息性消息
    OKGREEN = '\033[92m'   # 绿色，用于成功或确认的消息
    WARNING = '\033[93m'   # 黄色，用于警告或重要提示
    FAIL = '\033[91m'      # 红色，用于错误或失败的消息
    ENDC = '\033[0m'       # 重置所有样式，回到默认颜色
    BOLD = '\033[1m'       # 粗体文本
    UNDERLINE = '\033[4m'  # 下划线文本
    BLACK = '\033[30m'     # 黑色
    RED = '\033[31m'       # 红色
    GREEN = '\033[32m'     # 绿色
    YELLOW = '\033[33m'    # 黄色
    BLUE = '\033[34m'      # 蓝色
    MAGENTA = '\033[35m'   # 品红色（紫红色）
    CYAN = '\033[36m'      # 青色
    WHITE = '\033[37m'     # 白色
    # 添加背景颜色
    BG_BLACK = '\033[40m'  # 黑色背景
    BG_RED = '\033[41m'    # 红色背景
    BG_GREEN = '\033[42m'  # 绿色背景
    BG_YELLOW = '\033[43m' # 黄色背景
    BG_BLUE = '\033[44m'   # 蓝色背景
    BG_MAGENTA = '\033[45m'# 品红色（紫红色）背景
    BG_CYAN = '\033[46m'   # 青色背景
    BG_WHITE = '\033[47m'  # 白色背景


def color_print(content, font_color='white', bg_color='bg_blue'):
    colors = {
        'header': bcolors.HEADER,
        'okblue': bcolors.OKBLUE,
        'okcyan': bcolors.OKCYAN,
        'okgreen': bcolors.OKGREEN,
        'warning': bcolors.WARNING,
        'fail': bcolors.FAIL,
        'black': bcolors.BLACK,
        'red': bcolors.RED,
        'green': bcolors.GREEN,
        'yellow': bcolors.YELLOW,
        'blue': bcolors.BLUE,
        'magenta': bcolors.MAGENTA,
        'cyan': bcolors.CYAN,
        'white': bcolors.WHITE,
        'bg_black': bcolors.BG_BLACK,
        'bg_red': bcolors.BG_RED,
        'bg_green': bcolors.BG_GREEN,
        'bg_yellow': bcolors.BG_YELLOW,
        'bg_blue': bcolors.BG_BLUE,
        'bg_magenta': bcolors.BG_MAGENTA,
        'bg_cyan': bcolors.BG_CYAN,
        'bg_white': bcolors.BG_WHITE,
        'end': bcolors.ENDC,
    }

    # Apply the background color first, then the font color
    print(f'{colors[bg_color]}{colors[font_color]}{content}{colors["end"]}\n')

def save_pic_iterly(pic_name, postfix, info):
    import matplotlib.pyplot as plt

    pic_idx=1
    pic_name_full=f'{pic_name}_{pic_idx}.{postfix}'

    while os.path.exists(pic_name_full):
        print(f'File {pic_name_full} already exists.')
        pic_idx += 1
        pic_name_full=f'{pic_name}_{pic_idx}.png'

    plt.savefig(pic_name_full, dpi=300, bbox_inches='tight')

    color_print(f'!!!!! {info} is saved in file {pic_name_full}')

def read_csv_tqdm(path, **kwargs):
    import pandas as pd
    from tqdm import tqdm

    INPUT_FILENAME = path
    LINES_TO_READ_FOR_ESTIMATION = 20
    CHUNK_SIZE_PER_ITERATION = 10**5


    temp = pd.read_csv(INPUT_FILENAME,
                    nrows=LINES_TO_READ_FOR_ESTIMATION, **kwargs)
    N = len(temp.to_csv(index=False))
    df = [temp[:0]]
    t = int(os.path.getsize(INPUT_FILENAME)/N*LINES_TO_READ_FOR_ESTIMATION/CHUNK_SIZE_PER_ITERATION) + 1


    with tqdm(total = t, file = sys.stdout) as pbar:
        for i,chunk in enumerate(pd.read_csv(INPUT_FILENAME, chunksize=CHUNK_SIZE_PER_ITERATION, low_memory=False, **kwargs)):
            df.append(chunk)
            pbar.set_description('Importing: %d' % (1 + i))
            pbar.update(1)

    # data = temp[:0].append(df)
    data = pd.concat(df)
    
    del df            
    return data

def save_result_csv(csv_path, data):
    """保存结果到CSV文件（通用型）

    Args:
        csv_path: CSV文件路径
        data: dict, 包含要保存的数据，key为列名，value为对应的值
    """
    file_exists = os.path.exists(csv_path)
    headers = list(data.keys())
    values = list(data.values())

    with open(csv_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(values)

    print(f"Results saved to {csv_path}")

def get_unique_save_path(folder_path, base_name_pattern, start_no=1):
    """生成不重复的保存路径，自动递增版本号。

    通过检查文件是否存在，自动递增编号直到找到一个不存在的文件路径。
    如果目标文件夹不存在，会自动创建。

    Args:
        folder_path: 目标文件夹路径
        base_name_pattern: 文件名模板，必须包含 {no} 占位符用于插入编号
            例如: "result_{no}.csv", "model_v{no}.pt"
        start_no: 起始编号，默认为 1

    Returns:
        str: 不重复的完整文件路径

    Examples:
        >>> get_unique_save_path("./output", "result_{no}.csv")
        './output/result_1.csv'  # 如果不存在

        >>> get_unique_save_path("./output", "result_{no}.csv")
        './output/result_2.csv'  # 如果 result_1.csv 已存在

        >>> get_unique_save_path("./models", "checkpoint_v{no}.pt", start_no=10)
        './models/checkpoint_v10.pt'  # 从编号 10 开始

        # 使用 f-string 动态构建模板（注意 {no} 需要用双花括号转义）
        >>> model_name = "transformer"
        >>> dataset = "ETTh1"
        >>> get_unique_save_path("./results", f"{model_name}_{dataset}_{{no}}.csv")
        './results/transformer_ETTh1_1.csv'

        >>> pred_len = 96
        >>> get_unique_save_path("./output", f"pred{pred_len}_exp{{no}}.npy")
        './output/pred96_exp1.npy'
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    no = start_no
    while True:
        filename = base_name_pattern.format(no=no)
        full_path = os.path.join(folder_path, filename)
        if not os.path.exists(full_path):
            return full_path
        no += 1