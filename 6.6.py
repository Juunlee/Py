favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['jen', 'edward', 'Alex', 'Ian']
for name in favorite_languages.keys():
    if name in friends:
        print(name.title()+", "+"thank you for participating.")
    else:
        print(name.title()+", "+"please take our poll.")
