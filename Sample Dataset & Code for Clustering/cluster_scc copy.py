import os
import numpy as np
import networkx as nx
import collections, numpy
from random import randint
import time
from pyExcelerator import *

def SCC(data):
    blan = np.empty(shape=[0, 2])
    b = np.array(data)
    # b1 = b
    # bas = []
    list2 = []
    clust = []
    array1 = np.zeros(shape=(len(b), 3))
    for i in range(0, len(b)):
        for j in range(len(b[i])):
            p = float(b[i][j])
            array1[i][j] = p
        list2.append(array1[i, :])
    tempdel = b
    tempdel = np.unique(tempdel[:, 0:2])
    myarray = np.asarray(list2)
    b = np.array(myarray)
    index = np.where(b[:, 2] == 1)
    b[index[0], 2] = 0.95
    index = np.where(b[:, 2] == 0)
    b[index[0], 2] = 0.05
    checkval = 0
    checkval1 = 0
    checkval2 = 0
    checkval3 = 0
    b = np.matrix(b)
    time_start = time.clock()
    while True:
        index = np.where(b[:, 2] == b[:, 2].max())
        # k = b[:,2].max()
        # [(index, row.index(k)) for index, row in enumerate(b[:,2]) if k in row]
        idx = np.random.randint(len(index[0]), size=1)
        temp = index[0]
        if b[temp[idx[0]], 2] < 0.5:
            b = np.array(b)
            # blan = np.array(blan)
            datanew2 = np.unique(b[:, 0:2])
            blan = np.unique(blan)
            datanew2 = np.setdiff1d(datanew2, blan)
            for i in range(len(datanew2)):
                clust.append([datanew2[i]])
            break
        a = b[temp[idx[0]], 0:2]
        a = a.tolist()
        b = np.delete(b, temp[idx[0]], axis=0)
        clustsize = len(clust)
        if clustsize > 0:
            for i in range(0, clustsize):
                # r1 = np.where(clust[i]==a[0][0])
                if a[0][0] in clust[i]:
                    checkval1 = 1;
                    break
                    # if len(r1[0])>0:
                    #    checkval1=1;
                    #    break
            for j in range(0, clustsize):
                if a[0][1] in clust[j]:
                    checkval2 = 1;
                    break
                    # c1 = np.where(clust[i]==a[0][1])
                    # if len(c1[0])>0:
                    #    checkval2=1;
                    #    break
            if (checkval1 == 1) & (checkval2 == 1):
                clust[i].extend(clust[j])
                # clust[j] = []
                clust.remove(clust[j])
                checkval3 = 1
                checkval = 1
            if (checkval1 == 1) & (checkval2 != 1):
                clust[i].extend([a[0][1]]);
                checkval = 1;
            if (checkval1 != 1) & (checkval2 == 1):
                clust[j].extend([a[0][0]]);
                checkval = 1
        if (clustsize == 0) or (checkval == 0):
            # k = a.tolist()
            clust.append(a[0]);
            checkval = 1
        if checkval == 1:
            r = np.where(b[:, 0:1] == a[0][0])
            # np.put(b[:,0], r[0], int(a[1]))
            b[r[0], 0] = a[0][1]
            c = np.where(b[:, 1:2] == a[0][0])
            b[c[0], 1] = a[0][1]
            r = np.where(b[:, 0:1] == a[0][1])
            temp1 = b[r[0], 0:3]
            b = np.delete(b, r[0], axis=0)
            c = np.where(b[:, 1:2] == a[0][1])
            temp2 = b[c[0], 0:3]
            b = np.delete(b, c[0], axis=0)
            temp1 = numpy.vstack((temp1, temp2))
            temp1[:, 0:2].sort(axis=1)
            # datatemp[:,0:1].sort(axis=1)
            # b = datatemp
            datatemp = np.empty(shape=[0, 3])
            while True:
                if len(temp1) == 0:
                    break
                x = temp1[0, :]
                temp1 = np.delete(temp1, 0, axis=0)
                indx = np.where(np.all(temp1[:, 0:2] == x[0, 0:2], axis=1))
                if len(indx[0]) == 1:
                    x[0, 2] = x[0, 2] * temp1[indx[0], 2] / (
                    x[0, 2] * temp1[indx[0], 2] + (1 - x[0, 2]) * (1 - temp1[indx[0], 2]))
                    temp1 = np.delete(temp1, indx[0], axis=0)
                datatemp = numpy.vstack((datatemp, x))
                if len(temp1) == 0:
                    break
            b = numpy.vstack((b, datatemp))
        checkval = 0
        checkval1 = 0
        checkval2 = 0
        checkval3 = 0
        a = np.array(a)
        blan = numpy.vstack([blan, a])
    time_elapsed = (time.clock() - time_start)
    # print time_elapsed
    return clust,time_elapsed

if __name__ == "__main__":
    # filename_1 = raw_input('Please enter the standard crowd answer input filename:')
    filename_1='data_landmark_cleaned'
#    num = raw_input('Pls enter the num of records wanted:')

    num = 22050
    f = open('./'+filename_1+'.csv', 'r')
    data = []
    max_num = 0
    for line in f.readlines():
        data.append(line.split(','))
        max_num = max_num + 1
    # print data


    temp_data = []
    for i in range(int(num)):
    	# print i
    	temp_data.append(data[i])

    next_data = []
    for i in range(100):
    	next_data.append(data[i+int(num)])


    cluster_list,time_cost=SCC(temp_data)
    for i in cluster_list:
        for j in range(len(i)):
            i[j]=str(int(i[j]))
    # print cluster_list
    # print len(cluster_list)
    
    # generate nodes entries in json
    g = open('./origEdit1_'+str(num)+".json",'a')
    g.write("{\n"+"  \"nodes\": [\n")
    for i in range(len(cluster_list)):
    	for j in cluster_list[i]:
    		g.write("    {\"id\": \""+str(j)+"\", \"group\": "+str(i)+"},\n")
    g.write("  ],\n")

    # generate uncertain graph in json
    g.write("  \"link1s\": [\n")
    for i in temp_data:
        if float(i[2])<0.5:
             continue
        else:
             i[2]=str(int(float(i[2])*20+1))
             g.write("    {\"source\": \""+i[0]+"\", \"target\": \""+i[1]+"\", \"value\": "+i[2]+"},\n")
    g.write("  ],\n")

    # generate next questions in json
    g.write("  \"link2s\": [\n")
    for i in next_data:
    	i[2]="10"
    	# print i
    	g.write("    {\"source\": \""+i[0]+"\", \"target\": \""+i[1]+"\", \"value\": "+i[2]+"},\n")
    g.write("  ]\n}")
    g.close()