myList=[]
e=int(input("enter the limit for the list"))
for i in range(0,e):
    z=int(input())
    myList.append(z)
print(myList)
dupItems = []
uniqItems = {}
print("List = ",myList)

for x in myList:
	if x not in uniqItems:
		uniqItems[x] = 1
	else:
		if uniqItems[x] == 1:
			dupItems.append(x)
		uniqItems[x] += 1
print("Duplicate Elements = ",dupItems)
OUTPUT:
  enter the limit for the list7
15
14
25
14
32
14
31
[15, 14, 25, 14, 32, 14, 31]
List =  [15, 14, 25, 14, 32, 14, 31]
Duplicate Elements =  [14]
