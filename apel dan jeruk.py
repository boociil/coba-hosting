s , t = map(int,input().split())
a , b = map(int,input().split())
na , nj = map(int,input().split())
ap = map(int,input().split())
je = map(int,input().split())

aple = list(ap)
jruk = list(je)

ans_aple = 0
ans_jruk = 0

for i in aple:
    if (a + i >= s) and (a + i <= t):
        ans_aple += 1

for i in jruk:
    if (b + i >= s) and (b + i <= t):
        ans_jruk += 1

print(ans_aple)
print(ans_jruk)