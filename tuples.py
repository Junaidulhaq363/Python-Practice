#A tuple is a collection which is ordered and unchangeable.
tuple1=("apple","mango","lichi")
print(tuple1)

#how to change the tuple values
a=("junaid","bhaskar","hasan")
b=list(a)
b[0]="gaurav"
a=tuple(b)
print(a)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#The del keyword can delete the tuple completely:

#Unpacking a tuple and If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Loop Through the Index Numbers of tuples
tuple2=("hasan","bhaskar","gaurav")
for i in range(len(tuple2)):
 print(tuple2[i])

 #If you want to multiply the content of a tuple a given number of times, you can use the * operator:
#  tuple3=("hasan","bhaskar","gaurav")
#  tuple4=tuple3*2
#  print(tuple4)

