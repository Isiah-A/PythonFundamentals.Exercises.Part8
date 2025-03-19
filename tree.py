import os

# x = open('new_file', 'w')
# x.write("Hello \n")
# x.close()
# x = open('new_file', 'r')
# for line in x:
#     print(line)
# x.close()


# def tree(dir_path, file):
#     with open(file, 'w') as f:
#         for root, directories, files in os.walk(dir_path):
#             for file in files:
#                 f.write()


dir = str(input("Insert your file path: "))
find_directory = os.walk(dir)
print(find_directory)

# if is_directory:
#     print(f"The path '{dir}' is a directory.")
# else:
#     print(f"The path '{dir}' is not a directory or does not exist.")