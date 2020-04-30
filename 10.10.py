with open('Book.txt',encoding='utf-8') as subject:
    content = subject.read()
    content.lower().count('the')

