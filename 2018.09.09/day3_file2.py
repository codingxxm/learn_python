from sys import argv

script , file_name = argv

print(f"We are going to erase {file_name}")
print("if you don't want that , hit CTRL + C (^c).")
print("If you do want do that , hit RETURN.")

input("?")

print("Opening the file ...")
target = open(file_name,'w')

print("Truncating this file, BYE!")
target.truncate()

print("Now i'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm goint to write these on the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close the file")

target.close()
