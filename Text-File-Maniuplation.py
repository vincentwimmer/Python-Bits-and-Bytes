filePath = "C:/Path/To/textFile.txt"

# Write over entire document.
input_file = open(filePath, "w")
input_file.write("Content Overwritten")
input_file.close()

# Append to document.
input_file = open(filePath, "a")
input_file.write("\nContent Appended")
input_file.close()

# Open document and assign to variable.
input_file = open(filePath, "r")
textContent = input_file.read()
print(textContent)

# Print and convert document to manageable array.
items = textContent.splitlines()
for x in range(len(items)):
	print(items[x])
