import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


def create_df(in_list,dimx_size,dimy_size):
    dimx = 1
    dimy = 1
    dimz = 1
    df_screen = pd.DataFrame(columns=['dim1','dim2','dim3','value'])
    for i in in_list:
        df_screen = df_screen.append({'dim1':dimx,'dim2':dimy,'dim3':dimz,'value':i},ignore_index=True)
        dimx += 1
        if dimx > dimx_size:
            dimx = 1
            dimy += 1
        if dimy > dimy_size:
            dimy = 1
            dimz += 1
    return df_screen
#sample_list = [1,2,3,4,5,6,7,8,9,0,1,2]
#sample_list_df = create_df(sample_list,3,2)
#sample_list_df

f = open(os.path.join(os.path.expanduser('~'),'Projects/advent_of_code/day08_input.txt'),'r')
input_list_raw = f.read()
input_list = [int(x) for x in list(input_list_raw) if x != '\n']
input_df = create_df(input_list,25,6)

def get_min_xy(input_df):
    input_df_stats = input_df.groupby(['dim3','value']).size().reset_index(name='counts')
    min_count = input_df_stats[input_df_stats['value']==0].loc[:,'counts'].min()
    dim3_final = input_df_stats[input_df_stats['counts']==min_count].loc[:,'dim3'].values[0]
    total1 = input_df_stats[(input_df_stats['dim3']==dim3_final) & (input_df_stats['value']==1)].loc[:,'counts'].values[0]
    total2 = input_df_stats[(input_df_stats['dim3']==dim3_final) & (input_df_stats['value']==2)].loc[:,'counts'].values[0]
    return total1 * total2

get_min_xy(input_df)

#part 2

def get_pixel(input_df,x,y):
    check_series = input_df[(input_df['dim1'] == x) & (input_df['dim2'] == y)].loc[:,'value']
    check_series_list = check_series.tolist()
    i = 2
    for i in check_series:
        if i != 2:
            return i 

def create_xy_map(input_df):
    df_xy = input_df.loc[:,['dim1','dim2']].drop_duplicates()
    df_xy['dim1_neg'] = df_xy.apply(lambda x: x.loc['dim1'] * -1,axis=1)
    df_xy['dim2_neg'] = df_xy.apply(lambda x: x.loc['dim2'] * -1,axis=1)
    df_xy['minvalue'] = df_xy.apply(lambda x: get_pixel(input_df,x['dim1'],x['dim2']),axis=1)
    return df_xy
df_xy = create_xy_map(input_df)

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(df_xy[df_xy['minvalue']==0].loc[:,'dim1'], df_xy[df_xy['minvalue']==0].loc[:,'dim2_neg'],marker='s',s=360, color='black')
ax.scatter(df_xy[df_xy['minvalue']==1].loc[:,'dim1'], df_xy[df_xy['minvalue']==1].loc[:,'dim2_neg'],marker='s',s=360, color='white')
plt.show()