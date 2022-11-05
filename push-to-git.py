import os

os.system('git add -A')

message = str(input("Type your commit message: "))
os.system('git commit -m {message} ')

os.system('git push')