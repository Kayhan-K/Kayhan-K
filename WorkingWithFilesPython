file=open("WorkingWithFiles.txt" ,'w')
file.write("This is an append")
file.close()

file=open("WorkingWithFiles.txt" ,'r')
content=file.read()
print(content)
file.close

file=open("demo.txt",'a')
file.write("This is going to be 2nd Append")
file.close

data = 'some data to save'

def read():
  with open('data.txt','r') as file:
    file.close()

def write():
  with open('data.txt','w') as file:
    file.write(data + '\n')
    file.close()


def append():
  with open('data.txt', 'a') as file:
    file.write(data + '\n')
    file.close()

#difference between write and append ~ append = adding information on to the end of the existing text.With write all previous work will be overwritten.

#a+ = Both writing and reading file in append mode , it adds a reading file to the existing a . a = writing file here it is in append mode.


