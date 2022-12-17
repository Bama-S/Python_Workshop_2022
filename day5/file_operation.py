#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists

#f = open("sample.txt","w")
#f.write("This is the first line \n")
#print("The first line is written to file")
#f.close()
f = open("sample.txt","r")
print(f.read())
f.close()
f = open("sample.txt","a")
f.write("This is the second line \n")
print("The second line is written to file")
f.close()