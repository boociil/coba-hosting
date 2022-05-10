# PROGRAM APPEND AND DELETE
# https://www.hackerrank.com/challenges/append-and-delete/problem
s = input()
t = input()
n = int(input())

def cek(a,b,k):

    batas = min(len(a),len(b))
    potong = False
    for i in range(batas) :
        if (a[i] != b[i]):
            potong = True
            break
    
    if (len(a) >= len(b)):
        if not potong:    
            p = len(a) - (i+1) + len(b) - (i+1) 
        else:
            p = len(a) - i + len(b) - i 
    else:
        p = len(a) + len(b)

    if (k >= p):
        return "Yes"
    else:
        return "No"

    
     

list_string1 = list(s)
list_string2 = list(t)

print(cek(list_string1,list_string2,n))
