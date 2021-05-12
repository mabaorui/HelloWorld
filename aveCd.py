# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:16:19 2020

@author: Administrator
"""



files = []

f = open(test_list,'r')
for index,line in enumerate(f):
    files.append(line.strip().split('/')[1])

#            print(files[i])
#        cd2 = cd2 + load_data['cd2']
#        nc = nc + load_data['nc']
#        cd = cd + load_data['cd']
#        num = num + 1

#print('mean_f:',f/len(file_test))
print('thresh:',thresh,'files:',num, 'cd2:',cd2/num, 'nc:',nc/num, 'cd:',cd/num)
#print('files:',len(files), 'cd2:',cd2/len(files), 'nc:',nc/len(files), 'cd:',cd/len(files))

##################24个里挑最好一个视角
#for j in range(24):
#    cd2 = 0
#    nc = 0
#    cd = 0
#    num = 0
#    for i in range(len(files)):
#        #print(OUTPUT_DIR + files[i] + '_0.0'+ '_{}.npz'.format(j))
#        if(os.path.exists(OUTPUT_DIR + files[i] + thresh + '_{}.npz'.format(j))):
#            load_data = np.load(OUTPUT_DIR + files[i] + thresh +  '_{}.npz'.format(j))
#            cd2 = cd2 + load_data['cd2']
#            nc = nc + load_data['nc']
#            cd = cd + load_data['cd']
#            num = num + 1
#    
#
#
#    print('thresh:',thresh,'files:',len(files), 'num:',num,'cd2:',cd2/num, 'nc:',nc/num, 'cd:',cd/num)
###############每个模型都选不同的最好的一个视角  
#cd2 = 0
#nc = 0
#cd = 0
#num = 0
#for i in range(len(files)):  
#    nct = 0
#    for j in range(24):
#        #print(OUTPUT_DIR + files[i] + '_0.0'+ '_{}.npz'.format(j))
#        if(os.path.exists(OUTPUT_DIR + files[i] + thresh + '_{}.npz'.format(j))):
#            load_data = np.load(OUTPUT_DIR + files[i] + thresh +  '_{}.npz'.format(j))
#            if(load_data['nc']>nct):
#                nct = load_data['nc']
#                cd2t = load_data['cd2']
#                cdt = load_data['cd']
#    
#    nc = nc + nct
#    cd = cd + cdt
#    cd2 = cd2 + cd2t
#
#print('thresh:',thresh,'files:',len(files),'cd2:',cd2/len(files), 'nc:',nc/len(files), 'cd:',cd/len(files))