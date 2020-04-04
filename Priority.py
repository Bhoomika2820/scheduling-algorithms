#sjf
list1 = []
start = []
que = []
n = int(input("NO of processes : "))
print("Process\tBurst time\tArrival time\tPriority")
for i in range(n):
    input1 = list(map(int, input().split()))
    list1.append(input1)
p=list(list1)
p.sort(key=lambda x: x[3])
for i in range(n):
    start.append(p[i][0])

c = 0
while len(start) != 0:
    for j in start:
        if list1[j-1][2] <= c:
            list1[j-1].append(c - list1[j-1][2])
            list1[j-1].append(c + list1[j-1][1])
            c = c + list1[j-1][1]
            start.remove(j)
            que.append(j)
            break

# c = 0
# seq = []
# for i in range(n):
#     min1 = btl.index(min(btl))
#     btl[min1] = 999999
#     if (list1[min1][2] <= c):
#         seq.append(list1[min1][0])
#         listj = list(list1[min1])
#         listj.append(c)
#         listj.append(c + listj[1])
#         c = c + listj[1]
#         t = tuple(listj)
#         list1[min1] = t

print("Process Sequence : ", end='')
for each in que:
    print("P",each, end='\t')
print("\nProcess Burst time Arrival time Priority Waiting time Completion time")
for each in que:
    print(list1[each-1][0],list1[each-1][1],list1[each-1][2],list1[each-1][3],list1[each-1][4],list1[each-1][5],sep="\t\t\t")
awt = 0
print("\nAverage waiting time : ", end="")
for i in range(n):
    awt += list1[i][4]
print("{:.2f}".format(awt / n))
ct = 0
print("Average Turnaround time : ", end="")
for i in range(n):
    ct += list1[i][5] - list1[i][2]
print("{:.2f}".format(ct / n))
