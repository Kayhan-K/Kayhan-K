#rewrite the following as a ternary operator statement 

# x = 0

#if(x % 2 == 0):
   #print('even')
#else:
   #print('false')

#Answer = 

x = 0

even = 'even' if x % 2 == 0 else "false"
print(even)


# rewrite the following ternary operator as an if statement 

# grade = (mark >= 90) if 'A' else (mark >= 80) if 'B' else 'C'

# Answer = 

mark = 50

if (mark>=90):
   print("A")

if (mark>=80):
  print("B")

else:
   print("C")

# rewrite the following as a ternary operator statement 

#if(bill >= 1000):
   #discount = bill * 10.0/ 100
#else:
#discount = bill * 5.0/ 100

# last one not compelted 

discount = bill * 10.0/ 100 if(bill>= 1000) else * 5.0/ 100