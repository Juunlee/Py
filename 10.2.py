filename = 'learning_python.txt'
with open(filename) as file_object:
    content = file_object.read()
print(content)
content2 = content.replace('Python', 'c')
print(content2)


