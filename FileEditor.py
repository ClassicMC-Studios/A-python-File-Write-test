from os.path import exists as file_exists

if file_exists('fileSave.txt'):
    f = open("fileSave.txt", "a")
else:
    f = open("fileSave.txt", "x")
inpt = input("Write anything for the file\n")
f.write(inpt+"\n")
print("Send = 0 Success!")
