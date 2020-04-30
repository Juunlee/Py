filename = 'guest_book.txt'
while True:
    username = input("Enter your name:")
    if username == 'quit':
        break
    print("Welcome.")
    with open(filename, 'a') as file_object:
        file_object.write(username+' ')
       
        
