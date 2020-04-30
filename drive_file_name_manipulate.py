
#Connect to drive and copy the path value by right clicking on the drive object
 
 import os
 arr = os.listdir('directory_path/')
 renameString = "rename_string"
 
 #type(arr[0])

 print("Total index: ",len(arr))

"""
#Uncomment to print the list of files

 for i in range(len(arr)):
  print("File Name: ",arr[i])
"""

""" 
#Uncomment to to rename huge number of files based on some common pattern

for i in range(len(arr)):
  if renameString in arr[i]:
    h=arr[i]
    h=h.replace(renameString,'')
    print("File Name: ",h)
    os.rename("directory_path/"+arr[i],'directory_path/'+h)
"""

"""
#Uncomment to print the list of files based on search result

searchString="enter_something"
for i in range(len(arr)):
  if searchString in arr[i]:
    print(arr[i])
"""
