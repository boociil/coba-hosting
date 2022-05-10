#program kalkulator sederhana

a = int(input("Masukan angka pertama:"))
b = int(input("Masukan angka kedua:"))
c = input("Masukan operasi:")

if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="/"):
    print(a/b)
else:
    print(a*b)