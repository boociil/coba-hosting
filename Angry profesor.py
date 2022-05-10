def angry(murid,batas):
    tptwaktu = 0
    for i in murid:
        if i <= 0:
            tptwaktu += 1
    
    if tptwaktu < batas:
        return "YES"
    else:
        return "NO"

t = int(input())
ans = []

for i in range(t):
    n , k = map(int,input().split())
    st = map(int,input().split())
    student = list(st)
    ans.append(angry(student,k))

for i in ans:
    print(i)
    