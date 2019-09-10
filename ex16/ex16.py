from sys import argv

script , filename = argv

print(f"We are going to earse {filename}.")
print("If you don't want that hit CTRL-C (^C).")
print("If you do wnat that, hit RETURN.")

input("?")

print("Opening the file ...")
target = open(filename, 'w')

print("Truncating the file!  Goodbye.")
target.truncate()

print("Now I am going to ask you for three lines .")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")
line = line1, line2, line3
target.write('\n' .join(line) + "\n")
print("I'm going to write these to the file.")

print("And finaly we close it.")
target.close()
