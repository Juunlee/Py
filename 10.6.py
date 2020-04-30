print("Give me two number, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    fnum= input("First number:")
    if fnum == 'q':
        break
    snum = input("Second number:")
    try:
        answer = int(fnum)+int(snum)
    except ValueError:
        print("You have to type an integer.")
    else:
        print(answer) 
