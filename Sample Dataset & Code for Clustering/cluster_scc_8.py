"""
This edition produces the "correct" data for FORCE LAYOUT
Ok maybe it is not so correct...
TODO: 
  File "C:/Users/PREDATOR/Documents/GitHub/fyp/Sample Dataset & Code for Clustering/cluster_scc_edited7.py", line 242, in <module>
    i[2]=str(int(float(i[2])*20+1))

OverflowError: cannot convert float infinity to integer

"""
import os
import numpy as np
import networkx as nx
import collections, numpy
from random import randint
import time
import pyExcelerator
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
    filename_1='data'
    filename_2='gold_allSports'
    num = raw_input('Pls enter the num of records wanted:')
   
    f = open('./'+filename_1+'.csv', 'r')
    data = []
    max_num = 0
    for line in f.readlines():
        data.append(line.split(','))
        max_num += 1

    temp_data = []
    for i in range(int(num)):
        temp_data.append(data[i])

    next_data = []
    for i in range(100):
        next_data.append(data[i+int(num)])

    f2 = open('./'+filename_2+'.csv', 'r')
    data2 = []
    max_num2 = 0

    for line in f2.readlines():
        data2.append(line.split(','))
        max_num2 += 1

    GTAdict = dict()
    for i in range(max_num2):
        for j in range(len(data2[i])-1):
            key = data2[i][0]
            GTAdict.setdefault(key, [])
            GTAdict[key].append(int(data2[i][j+1])+1)

    cluster_list,time_cost=SCC(temp_data)
    for i in cluster_list:
        for j in range(len(i)):
            i[j]=str(int(i[j]))
    
    # generate CIRCLE PACK node entries in json
    g = open('./circlePack_'+str(num)+".json",'a')
    g.write("{\n"+"    \"name\": \"root\",\n    \"size\": 1,\n    \"children\": [\n")
    for i in range(len(cluster_list)-1):
        g.write("   {\n        \"name\": \"group-"+str(i)+"\",\n        \"size\": 1,\n        \"children\": [\n")
        for j in cluster_list[i][:-1]:
            g.write("            { \"name\": \""+str(j)+"\", \"size\": 1, \"truth\": \"")
            for k,v in GTAdict.iteritems():
                for m,n in enumerate(v):
                    if n == int(j):
                        g.write(k + "\" },\n") # comma
        g.write("            { \"name\": \""+str(cluster_list[i][-1])+"\", \"size\": 1, \"truth\": \"")
        j = cluster_list[i][-1]
        for k,v in GTAdict.iteritems():
            for m,n in enumerate(v):
                if n == int(j):
                    g.write(k + "\" }\n") # no comma
        g.write("        ]},\n")
    g.write("        { \"name\": \"group-"+str(len(cluster_list)-1)+"\",\n        \"size\": 1,\n        \"children\": [\n")
    for j in cluster_list[len(cluster_list)-1][:-1]:
        g.write("            { \"name\": \""+str(j)+"\", \"size\": 1, \"truth\": \"")
        for k,v in GTAdict.iteritems():
            for m,n in enumerate(v):
                if n == int(j):
                    g.write(k + "\" },\n") # comma
    g.write("            { \"name\": \""+str(cluster_list[i][-1])+"\", \"size\": 1, \"truth\": \"")
    j = cluster_list[len(cluster_list)-1][-1]
    for k,v in GTAdict.iteritems():
            for m,n in enumerate(v):
                if n == int(j):
                    g.write(k + "\" }\n") # no comma
    g.write("        ]}\n")
    g.write("]}\n")

    # generate FORCE LAYOUT node entries in json
    g2 = open('./forceLayout_'+str(num)+'.json', 'a')
    g2.write("{\n"+"  \"nodes\": [\n")
    for i in range(len(cluster_list)-1):
        for j in cluster_list[i]:
        		g2.write("    {\"id\": \""+str(j)+"\", \"group\": "+str(i)+"},\n")
    i = len(cluster_list)-1
    for j in cluster_list[i]:
        if j != cluster_list[i][-1]:
            g2.write("    {\"id\": \""+str(j)+"\", \"group\": "+str(i)+"},\n")
        else:
            g2.write("    {\"id\": \""+str(j)+"\", \"group\": "+str(i)+"}\n")
    g2.write("  ],\n")
    
    # generate uncertain graph in json
    g2.write("  \"links\": [\n")
    flag=0
    for i in temp_data:
        if float(i[2])>=0.5:
            i[2]=str(int(float(i[2])*20+1))
            flag+=1
            if flag==1:
                g2.write("    {\"source\": \""+i[0]+"\", \"target\": \""+i[1]+"\", \"value\": "+i[2]+"}")
            else:
                g2.write(",\n    {\"source\": \""+i[0]+"\", \"target\": \""+i[1]+"\", \"value\": "+i[2]+"}")
    g2.write("\n  ],\n")

    # generate next questions in json
    g2.write("  \"link2s\": [\n")
    for i in next_data[:-1]:
    	i[2]="10"
    	# print i
    	g2.write("    {\"source\": \""+i[0]+"\", \"target\": \""+i[1]+"\", \"value\": "+i[2]+"},\n")
    i = next_data[-1]
    i[2] = "10"
    g2.write("    {\"source\": \""+i[0]+"\", \"target\": \""+i[1]+"\", \"value\": "+i[2]+"}\n")
    g2.write("  ]\n}")
             
    # generate TABLE DATA uncertain graph in csv
    g3 = open('./uncertain_'+str(num)+'.csv', 'a')
    for i in temp_data:
        g3.write(i[0]+", "+i[1]+", "+str(float(i[2]))+"\n")

    # generate TABLE DATA cluster list in tsv
    g4 = open('./clusterList_'+str(num)+'.tsv', 'a')
    for i in range(len(cluster_list)):
        g4.write(str(i)+"\t")
        for j in cluster_list[i][:-1]:
    		g4.write(str(j)+", ")
        j = cluster_list[i][-1]
        g4.write(str(j)+"\n")
        
    # generate TABLE DATA next questions in csv
    g5 = open("./nextQn_"+str(num)+".csv", 'a')
    for i in next_data:
    	g5.write(i[0]+", "+i[1]+"\n")
        
    g.close()
    g2.close()
    g3.close()
    g4.close()
    g5.close()
    f.close()
    f2.close()