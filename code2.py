#PYTHON3
import time
start_time = time.time()
def knap(v,w,C,list_name):
    N=len(v)
    m={}
    for c in range(C+1):
        m[(0,c)]=0
    for i in range(1,N+1):
        for c in range(C+1):
            if w[i-1]<=c:
                m[(i,c)]=max(m[(i-1,c)],v[i-1]+m[(i-1,c-w[i-1])])
            else:
                m[(i,c)]=m[(i-1,c)]
 
    c = C
    temp=0
    for i in range(N, 0, -1):
        if m[(i,c)] != m[(i-1,c)]:
            print(f'{str(list_name[i-1])}, {w[i-1]}, {v[i-1]}')
            c -= w[i-1]
            temp=temp+w[i-1]
    print("Final weight:",temp)
    print( "Final value:",m[(N,C)] ) #best value
    return ""
#provided format is:
# 120 //total weight of the bag
# name_of_item; weight of item; value of item
iterate = int(input("How many available items are there: "))
list_name=[]
list_weight=[]
list_value=[]
weight=int(input("Enter the capacity of bag: "))
print("Enter the item details in format: ")
print("name;weight;value")
for i in range(0,iterate):
    var=input("")
    raw_list=var.split(";")
    list_name.append(raw_list[0])
    list_weight.append(int(raw_list[1]))
    list_value.append(int(raw_list[2]))
#print(list_name)
#print(list_weight)
#print(list_value)
    # Driver program to test above function
val = list_value
wt = list_weight
W = weight
print("")
print(knap(val,wt,W,list_name))
print("Time take in microseconds:", (time.time() - start_time)/10**6) 
