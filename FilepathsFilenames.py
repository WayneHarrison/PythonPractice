import os
totalSize = 0

for filename in os.listdir('D:\\Personal Files\\Documents\\Python Projects'):
    if not os.path.isfile(os.path.join('D:\\Personal Files\\Documents\\Python Projects', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('D:\\Personal Files\\Documents\\Python Projects', filename))
    print(totalSize)
