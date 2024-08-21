import os
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
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
    pic_idx=1
    pic_name_full=f'{pic_name}_{pic_idx}.{postfix}'

    while os.path.exists(pic_name_full):
        print(f'File {pic_name_full} already exists.')
        pic_idx += 1
        pic_name_full=f'{pic_name}_{pic_idx}.png'

    plt.savefig(pic_name_full, dpi=300, bbox_inches='tight')

    color_print(f'!!!!! {info} is saved in file {pic_name_full}')

def read_csv_tqdm(path, **kwargs):
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
