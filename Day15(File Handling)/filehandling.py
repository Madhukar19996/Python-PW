# Example 1 : Create/ writing a file

#Approach 1 :

# file=open("D:\\Madhukar_Pandey\\SSC\\Automationfile.txt",'w')
# file.write("Welcome to Python \n File handling")
# file.close()


#Approach 2 :

# with open("D:\\Madhukar_Pandey\\SSC\\myfile.txt",'w') as file :
#     file.write("Welcome to Python \nFile handling 1 ")
#     file.close()


#Example 2 : Appending the data into file

# with open("D:\\Madhukar_Pandey\\SSC\\myfile.txt",'a') as file :
#     file.write("\nThis line is appended...")
#     file.close()


#Example 3 : Reading the data from text file

#read() --> reads entire data
#readline() --> read single line
#readlines() --> read all the lines into the list format


# with open("D:\\Madhukar_Pandey\\SSC\\myfile.txt",'r') as file :
    #content=file.read()
    #print(content)

"""
    Welcome to Python 
    File handling 1 
    This line is appended...
    
"""
    # content=file.readline()
    # print(content) # Welcome to Python

    # content=file.readlines() #['Welcome to Python \n', 'File handling 1 \n', 'This line is appended...']
    # print(content)
    #
    # file.close()

#Example 4: Renaming the file
# import os
# os.rename("D:\\Madhukar_Pandey\\SSC\\myfile.txt","D:\\Madhukar_Pandey\\SSC\\myfile1.txt")
# print("file renamed")

#Example 5 : Deleting the file
# import os
# file="D:\\Madhukar_Pandey\\SSC\\Automationfile.txt"
#
# if os.path.exists(file):
#     os.remove(file)
# else:
#   print("file does not exist")


#Example 6 : Creating a directory /folder
# import os
# os.mkdir("D:\\Madhukar_Pandey\\SSC\\Automationfile")
# print("Directory created ")

#Example 7 : Check the directory exist or not

# mydir="D:\\Madhukar_Pandey\\SSC\\Automationfile"
#
# import os
#
# if os.path.exists(mydir):
#     print("Directory exists")
# else:
#   print("Directory does not exist")


#Example 8: Renaming the directory

# import os
#
# os.rename("D:\\Madhukar_Pandey\\SSC\\Automationfile","D:\\Madhukar_Pandey\\SSC\\Automationfile1")
# print("Directory renamed....")

#Example 9: Remove/delete the  the directory

# import os
# import shutil
# file="D:\\Madhukar_Pandey\\SSC\\Automationfile1"
#
# if os.path.exists(file):
#     os.rmdir(file) # if folder/directory is empty
#     shutil.rmtree("file")  #if folder/directory contains files.
# else:
#   print("Directory does not exist")


#Example 10 : get the current working directory

# import os
#
# currentworkingdirectory=os.getcwd() #returns current working directory
# print(currentworkingdirectory)

