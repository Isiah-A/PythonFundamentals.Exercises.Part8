import os

cwd = os.getcwd()

def list_dir(start, alist):
    dircontents = os.listdir(os.path.realpath(start))
    with open('new_file', 'a') as f:
        f.write(str(os.path.realpath(start)) + "\n")
        f.close()
    for i in dircontents:
        newpath = os.path.join(start, i)
        if os.path.isfile(cwd + '/' + str(newpath)):
            alist.append(newpath)
            with open('new_file', 'a') as f:
                f.write(str(i) + '\n')
                f.close()
        elif os.path.isdir(cwd + '/' + str(newpath)):
            list_dir(newpath, alist)

new_list = []
list_dir("PythonFundamentals.Exercises.Part10", new_list)
