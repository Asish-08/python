#Write a Python program to count the number of even and odd numbers from a series of numbers
print('write the number of digits you want to analyze')
i=int(input())
my_list = []
while i!=0:
    my_list.append(int(input()))
    i=i-1
odd = 0
even = 0
for x in my_list:
    x=int(x)
        if x % 2 ==0:
    	     even+=1
        else:
    	     odd+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
