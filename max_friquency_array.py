n=int(input())
t=list(map(int,input().split()))
y=max(t)
def county(t,y):
    count=0
    for ele in t:
        if(ele==y):
            count+=1
    return count
print(county(t,y))