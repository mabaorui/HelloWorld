# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:16:19 2020

@author: Administrator
"""

#import dist_chamfer_3D as dist_chamfer_3D
#import torch
import numpy as np
import os
#import fscore

#test_list = '/data/mabaorui/AtlasNetOwn/data/shapenetcore_ids/03211117_testids.txt'
#test_list = '/data1/mabaorui/AtlasNetOwn/data/famous/famous_original/testset.txt'
OUTPUT_DIR = '/data1/mabaorui/AtlasNetOwn/04379243_test_0001_sur_val/'
thresh = '0.01'
class_idx = '04379243'


files = []

f = open('/data1/mabaorui/AtlasNetOwn/data/val.txt','r')
for index,line in enumerate(f):
    if(line.strip().split('/')[0]==class_idx):
        #print(line)
        files.append(line.strip().split('/')[1])
f.close()

#device = torch.device("cuda:0")
cd2 = 0
nc = 0
cd = 0
num = 0
num_no = 0
for i in range(len(files)):
    #print(OUTPUT_DIR + files[i] + '_' + str(thresh) + '.npz')
    if(os.path.exists(OUTPUT_DIR + files[i] + '_' + str(thresh) + '.npz')):
        #if(np.load(OUTPUT_DIR + files[i] + '_' + str(thresh) + '.npz')['cd2']>0.01):
            #print('e')
            #continue
        load_data = np.load(OUTPUT_DIR + files[i] + '_' + str(thresh) + '.npz')
        cd2 = cd2 + load_data['cd2']
        nc = nc + load_data['nc']
        cd = cd + load_data['cd']
        num = num + 1
    else:
        #print('exit')
        num_no = num_no + 1
#print('mean_f:',f/len(file_test))
print('files:',len(files),'num:',num, 'num_no:' ,num_no, 'cd2:',cd2/num, 'nc:',nc/num, 'cd:',cd/num)
#print('files:',len(files), 'cd2:',cd2/len(files), 'nc:',nc/len(files), 'cd:',cd/len(files))