Keys = ['Ten','Twenty','Thirty']
Values = [10,20,30]

dic1 = dict(zip(Keys, Values))

print(dic1)


List_1 = ['Kayhan','Tyler', 'Alfred','Jacob']
list_2 = [16,16,16,17]

dic2 =dict(zip(List_1 , list_2))

print(dic2)


sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}


for item in sampleDict:
    print("Key : {} , Value : {}".format(item,sampleDict[item]))



sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

for key, value in sampleDict.items() :
    print (80)