filename_1='data'
filename_2='gold_allSports'
#num = raw_input('Pls enter the num of records wanted:')

f = open('./'+filename_2+'.csv', 'r')
data = []
max_num = 0
for line in f.readlines():
    data.append(line.split(','))
    max_num = max_num + 1
# print data

temp_data = []
for i in range(max_num):
    # print i
    temp_data.append(data[i])

GTAdict = dict()
for i in range(max_num):
    for j in range(len(data[i])-1):
        key = temp_data[i][0]
        GTAdict.setdefault(key, [])
        GTAdict[key].append(int(temp_data[i][j+1])+1)

g = open('./hai.json','a')

jare=[2,3,4,5]

for j in jare:
    for k,v in GTAdict.iteritems():
            for m in range(len(v)):
                if v[m] == j:
                    print True
                    print v[m]
                    print k
                    g.write(k+" ya ")
g.close()
