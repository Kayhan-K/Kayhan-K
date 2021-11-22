def check(red, dead):  #This is the inital function that checks if the two words are anagrams or not.
 if(sorted(red)==sorted(dead)):
   print ("The strings are Anagrams.")

 else:
   print("The strings aren't Anagram.")
#If the strings are not anagrams then the else statment will print that they are not anagrams.

check("red", "dead")

# Function that will take two strings and return whether they are anagrams - not boolean 
