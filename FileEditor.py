from os.path import exists as file_exists

if file_exists('fileSave.txt'):
    f = open("fileSave.txt", "a")
else:
    f = open("fileSave.txt", "x")
f.write("This will write as a save\n")
print("Send = 0 Success!")
