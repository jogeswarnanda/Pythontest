
#with open ("test.txt") as file:
#    content = file.read()
#    print(content)

#Example of absolute path to read a file located on Desktop folder
with open ("/Users/jogeswarnanda/Desktop/test1.txt") as file:
    content = file.read()
    print(content)


# My file is under the current working dir /Users/jogeswarnanda/Pythontest/Pythontest/Files Handling
# Below code is to use relative path to read a file located on Desktop folder
# with open ("../../../Desktop/test1.txt") as file:
#     content = file.read()
#     print(content)


#with open ("test.txt", mode="a") as file:
#    file.write("\nNew line.")