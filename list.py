# List items are ordered, index, changeable, and allow duplicate values.
my_list=["junaid",24,True,"bhaskar",False,65]
print(my_list[3],my_list[2])
print(len(my_list))
print(type(my_list))

thislist=list(("apple",54,True))
print(thislist[1])


this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list) 

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
a = ["apple", "banana", "cherry"]
a.insert(2, "watermelon")
print(a)

# To add an item to the end of the list, use the append() method:

b=["apple", "banana", "cherry"]
b.append("hasan")
print(b)


#To append elements from another list to the current list, use the extend() method.
list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1)

# The pop() method removes the specified index.
# The remove() method removes the specified item.
#If you do not specify the index, the pop() method removes the last item.
#The del keyword also removes the specified index and The del keyword can also delete the list completely.
#The clear() method empties the list. The list still remains, but it has no content.


#sorting

s=["apple","banana","mango","lichi"]
s.sort(reverse=True)
print(s)

n=[1,9,4,7,2]
n.sort(reverse=True)
print(n)


#reverse a list

list5=["bhaksar","lakshay","hasan","damini"]
list5.reverse()
print(list5)

#copy a list
list3=["bhaksar","lakshay","hasan","damini"]
list4=list3.copy()
print(list4)

list8=["bhaksar","lakshay","hasan","damini"]
list9=list(list8)
print(list8)

# Join list by concatination (+), appned and extend method also



