r=int(input("Range of List : "))
l=[]
for i in range(r):
    i=int(input("Enter : "))
    l.append(i)
print("Nums = ",l)
m=l.copy()
def scnum(o):
    c=0
    for i in range(r):
        for j in range (r):
            if(l[i]!=m[j] and m[j]<l[i]):
                c=c+1
        print("[",c,"]")
        c=0    
scnum(r)
OUTPUT:
  Range of List : 5
Enter : 8
Enter : 1
Enter : 2
Enter : 2
Enter : 3
Nums =  [8, 1, 2, 2, 3]
[ 4 ]
[ 0 ]
[ 1 ]
[ 1 ]
[ 3 ]
