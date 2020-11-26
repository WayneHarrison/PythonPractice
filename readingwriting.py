helloFile = open('D:\\Personal Files\\Documents\\Python Projects\\hello.txt')
helloFile.read()
helloFile = open('D:\\Personal Files\\Documents\\Python Projects\\hello.txt', 'a')
helloFile.write('Appending new content')
helloFile = open('D:\\Personal Files\\Documents\\Python Projects\\hello2.txt', 'w')
helloFile.write('Hello world! \nNewlines.')
shelfFile = shelve.open('D:\\Personal Files\\Documents\\Python Projects\\mydata')
shelfFile['Dogs'] = ['Pippa', 'Milo', 'Bonnie']
shelfFile.close()
