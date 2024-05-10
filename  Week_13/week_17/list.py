# Aydrean Wheeler
# 9/5/24

# creating an empty list
lst = []

# using a forloop to add the numbers 1-100 to the list
for b in range(1, 101):
    lst.append(b)

# printing the list lst
print(lst)

# creating an empty list named odd
odd = []

# using a forloop to add the odd numbers 1-100 to the list odd
for b in range(1, 100, 2):
    odd.append(b)

# printing the list odd
print(odd)

# creating an empty list named even
even = []

# using a forloop to add the even numbers 1-100 to the list even
for b in range(2, 100, 2):
    even.append(b)

# printing the list even
print(even)

# creat a variable named b that points to the first list you created
b = lst

#creat a variable named joined that joins the even and odd lists using an operator
joined = even+odd

#output the variable joined
print(joined)

#output the type of the joined variable
print(type(joined))

#compair the list b to the list joined using condensationl pairing
b==joined