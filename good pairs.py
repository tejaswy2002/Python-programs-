def solve(nums):
   count=0
   n=len(nums)
   for i in range(n):
      for j in range(i+1,n):
         if nums[i] == nums[j]:
            count+=1
   return count

a=[]
n=int(input("Enter number of elements:"))
print("Enter elements:")
for i in range(n):
      b=int(input())
      a.append(b)
print("Number of good pairs:",solve(a))
