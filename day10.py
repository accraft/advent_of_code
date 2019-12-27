
import math
import numpy as np
from collections import defaultdict
from collections import OrderedDict
import copy

in_cords = ['......#.#.',
            '#..#.#....',
            '..#######.',
            '.#.#.###..',
            '.#..#.....',
            '..#....#.#',
            '#..#....#.',
            '.##.#..###',
            '##...#..#.',
            '.#....####']

in_cords_listed = [[1 if x == '#' else 0 for x in list(i)] for i in in_cords] 

def count_stroids(in_list,o_num,i_num):
    stroid_counter=0
    badslope = []
    for o2_num,o2 in enumerate(in_list):
        for i2_num,i2 in enumerate(o2):
            if i2_num == i_num and o2_num == o_num:
                badslope=[]
                continue
            elif i2_num == i_num:
                slope = 9999
            else:
                slope = (o_num-o2_num)/(i2_num - i_num)
            if slope in badslope or i2==0:
                continue
            else:
                badslope.append(slope)
                stroid_counter += i2
    return stroid_counter,badslope
#test_count = count_stroids(in_cords_listed,8,5)
#test_count[0]

def find_max_stroids(in_list):
    max_stroid_count = 0
    for o_num,o in enumerate(in_list):
        for i_num,i in enumerate(o):
            if i==1:
                stroid_count = count_stroids(in_list,o_num,i_num)
                if stroid_count[0] > max_stroid_count:
                    max_stroid_count = max(stroid_count[0],max_stroid_count)
                    max_stroid_coords = (i_num,o_num)
    return max_stroid_count, max_stroid_coords
#max_count_test = find_max_stroids(in_cords_listed)


in_cords_final = [
'#.#....#.#......#.....#......####.',
'#....#....##...#..#..##....#.##..#',
'#.#..#....#..#....##...###......##',
'...........##..##..##.####.#......',
'...##..##....##.#.....#.##....#..#',
'..##.....#..#.......#.#.........##',
'...###..##.###.#..................',
'.##...###.#.#.......#.#...##..#.#.',
'...#...##....#....##.#.....#...#.#',
'..##........#.#...#..#...##...##..',
'..#.##.......#..#......#.....##..#',
'....###..#..#...###...#.###...#.##',
'..#........#....#.....##.....#.#.#',
'...#....#.....#..#...###........#.',
'.##...#........#.#...#...##.......',
'.#....#.#.#.#.....#...........#...',
'.......###.##...#..#.#....#..##..#',
'#..#..###.#.......##....##.#..#...',
'..##...#.#.#........##..#..#.#..#.',
'.#.##..#.......#.#.#.........##.##',
'...#.#.....#.#....###.#.........#.',
'.#..#.##...#......#......#..##....',
'.##....#.#......##...#....#.##..#.',
'#..#..#..#...........#......##...#',
'#....##...#......#.###.#..#.#...#.',
'#......#.#.#.#....###..##.##...##.',
'......#.......#.#.#.#...#...##....',
'....##..#.....#.......#....#...#..',
'.#........#....#...#.#..#....#....',
'.#.##.##..##.#.#####..........##..',
'..####...##.#.....##.............#',
'....##......#.#..#....###....##...',
'......#..#.#####.#................',
'.#....#.#..#.###....##.......##.#.']
in_cords_final_listed = [[1 if x == '#' else 0 for x in list(i)] for i in in_cords_final]
max_count = find_max_stroids(in_cords_final_listed)
max_count

in_cords_bigtest = ['.#..##.###...#######',
'##.############..##.',
'.#.######.########.#',
'.###.#######.####.#.',
'#####.##.#.##.###.##',
'..#####..#.#########',
'####################',
'#.####....###.#.#.##',
'##.#################',
'#####.##.###..####..',
'..######..##.#######',
'####.##.####...##..#',
'.#####..#.######.###',
'##...#.##########...',
'#.##########.#######',
'.####.#.###.###.#.##',
'....##.##.###..#####',
'.#.#.###########.###',
'#.#.#.#####.####.###',
'###.##.####.##.#..##']
in_cords_bigtest_listed = [[1 if x == '#' else 0 for x in list(i)] for i in in_cords_bigtest]

def assign_slopes(in_list,o_base,i_base):
    degree_dict = defaultdict(list)
    out_list = in_list.copy()
    hit_origin = 0
    for o_num,o in enumerate(out_list):
        for i_num,i in enumerate(o):
            if i == 0:
                continue
            if i_num == i_base and o_num == o_base:
                hit_origin = 1
                continue
            if i_num == i_base:
                degrees = 0.0001
            else:
                degrees = abs(np.arctan((o_base - o_num) / (i_num - i_base)) - math.pi/2) * (180 / math.pi)
            if i_num < i_base or i_num == i_base and o_num > o_base:
                degrees+=180
            out_list[o_num][i_num] = degrees
            if hit_origin:
                degree_dict[degrees].append([i_num,o_num])
            else:
                degree_dict[degrees].insert(0,[i_num,o_num])
    return out_list,degree_dict

def find_200th_stroid(indict):
    indict_copy = copy.deepcopy(indict)
    degree_dict2 = OrderedDict(sorted(indict_copy.items()))
    blast_count = 0
    for k in degree_dict2.keys():
        blast_count+=1
        to_drop = degree_dict2[k].pop()
        print(str(blast_count) + '  -  ' + str(k) + '  ' + str(to_drop[0]) + ',' + str(to_drop[1]))
        if blast_count == 200:
            print(to_drop)
            break
        if k > 356:
            print(blast_count)
            print(k)


slope_list_test,degree_dict_test = assign_slopes(in_cords_bigtest_listed,13,11)
find_200th_stroid(degree_dict_test)

slope_list,degree_dict = assign_slopes(in_cords_final_listed,20,20)
find_200th_stroid(degree_dict)