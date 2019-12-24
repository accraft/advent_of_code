import pandas as pd
import numpy as np

def create_df(in_list,dimx_size,dimy_size):
    working_list = in_list.copy()
    dimx = 1
    dimy = 1
    dimz = 1
    df_screen = pd.DataFrame(columns=['dim1','dim2','dim3','value'])
    for i in input_items:
        df_screen = df_screen.append({'dim1':[dimx],'dim2':[dimy],'dim3':[dimz],'value':working_list.pop(0)},ignore_index=True)
        dimx += 1
        if dimx > dimx_size:
            dimx = 1
            dimy += 1
        if dimy > dimy_size
            dimy = 1
            dimz += 1
    return df_screen

sample_list = [1,2,3,4,5,6,7,8,9,0,1,2]
sample_list_df = create_df(sample_lis,3,2)