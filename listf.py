#program to demonstrate list functions
list1=[10,40,90,200,10]
print(list1)

#appending
list1.append(500)
print("after appending",list1)

#insert
list1.insert(2,100)
print("after inserting at index 2",list1)

#extend
list1.extend([700,800,900])
print("after extending",list1)

#remove
list1.remove(800)
print("after removing 800",list1)

#pop
list1.pop()
print("after poping",list1)

#index
i=list1.index(90)
print("index of 90 is",i)

#count
c=list1.count
print("no of 10's is",c)

#sort
list1.sort()
print("after sorting list1",list1)

#reverse
list1.reverse()
print("after reversing list1",list1)

#sum
total=sum(list1)
print("total of all elements in list1",total)


#ord
val=ord('A')
print("unicode value of A is",val)

#chr
ch=chr(97)
print("character with unicode 97 is",ch)

#any
print(any([True,False]))

#all
print(all([True,False]))


#nested lists
list2=[4,5,6,[8,9],[10,11,12]]
print("nested list",list2[0])
print("nested list",list2[3][1])
print("nested list",list2[4][1])       

































