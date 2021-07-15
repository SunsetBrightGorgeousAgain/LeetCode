import os

list_dirs = os.walk('E:/Personal/练习/小兴趣/')
for root, dirs, files in list_dirs:
    for d in dirs:
        print(d)
        print(os.path.join(root, d))
    for f in files:
        print(os.path.join(root, f))
