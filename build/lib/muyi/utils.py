import os
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
import sys

def color_print(content):
    print(f'\033[1;46m{content}\033[0m\n')

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

    data = temp[:0].append(df)
    del df            
    return data
