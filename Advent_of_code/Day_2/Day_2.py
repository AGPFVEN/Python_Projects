import sys
sys.path.append("D:\\python_agpfven\\lib\\site-packages")

with open ("D:\\Users\\Usuario\\Python_Projects\\Advent_of_code\\Day_2\\Input.txt", "r") as myfile:
    data = myfile.read()

lines = data.splitlines()
count = 0

#6-10 s: sssssssss
#6-7 b: bbbbbxkb

def check_password(word):
    policy, password = word.split(": ")
    min_max, letter = policy.split(" ")
    mininum, maximum = map(int, min_max.split("-"))
    if password.count(letter) >= mininum and password.count(letter) <= maximum:
        return True
    else:
        return False

for passwords in lines:
    if (check_password(passwords) == True):
        count += 1
        print (count)