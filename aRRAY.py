import array as arr
a = arr.array('i', [2,4,6,8])
                   #o 1 2 3
print("First element:", a[0])
print("Second element:", a[1])
print("Third element:", a[-2])
print("Last element:", a[-1])

import array as arr
a = arr.array('i', [1,8,12,10,7])
                   #0,1,2,3,4
                   #0,-4,-3,-2,-1

print("First array:", a[0])
print("Second array:",a[1])
print("Third array:",a[-3])

a = input("Print Full Array In Reverse Order?")
if a == "Yes":
    arr = [1, 8, 12, 10,10, 7];
    print("Array In Reverse Order = ");
for i in range(len(arr)-1, -1, -1):
    print(arr[i]),

b = input("Print Duplicated Array?")
if b == "Yes":
    arr=[1,8,12,10,10,7];
    print("Duplicated Array = ")
    def checkIfDuplicates_1(listOfElems):
        if len(listOfElems) == len(set(listOfElems)):
            return False
        else:
            return True
listOfElems = a
result = checkIfDuplicates_1(listOfElems)

if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')








