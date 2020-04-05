data = [64,22,75,1,3,67,52,20]
n=len(data)
for z in range(n-1,0,-1):
    for i in range (0,n-1):
            if data[i]>data[i+1]:
                temp=data[i]
                data[i]=data[i+1]
                data[i+1]=temp
            print (data)
