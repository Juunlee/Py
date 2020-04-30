adult = True
numTimes = 0
while adult and numTimes<10:
    prompt = 'How old are you?'
    age = input(prompt)
    if age=='quit':
        break
    age = int(age)
    print(age)
    if age<18:
        adult = False
    numTimes+=1
