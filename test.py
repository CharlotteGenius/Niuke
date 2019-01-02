import bisect
def deal(l,res):
    #每次向b中加一个list中的元素
    b    = [9999]*len(l)
    b[0] = l[0]
    res  = res+[1]
    for i in range(1,len(l)):
        pos =bisect.bisect_left(b,l[i])
        print("pos:",pos)
        res += [pos+1]
        b[pos]=l[i]
    print('res:',res)
    return res
    
while True:
    try:
        n=int(input())
        s=list(map(int,input().split()))
        dp1=[]
        dp2=[]
        dp1 =deal(s,dp1)#正序遍历位置
        print('dp1:',dp1)
        dp2=deal(s[::-1],dp2)[::-1]#逆序遍历位置
        print('dp2:',dp2)
        a=max(dp1[i]+dp2[i] for i in range(n))#两次遍历的结果相加
        print(n-a+1)#a中的那个人多加了一次 故要+1
    except:
        break