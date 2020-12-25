import sys
sys.path.append("D:\\python_agpfven\\lib\\site-packages")

with open ("D:\\Users\\Usuario\\Python_Projects\\Advent_of_code\\Day_1\\Input.txt", "r") as myfile:
    data = myfile.read()

lines = data.splitlines()

expenses = []
for number in lines:
    expenses.append(int(number))

for number_a in expenses:
    for number_b in expenses:
        for number_c in expenses:
            if number_a + number_b + number_c == 2020:
                print("Numbers:", number_a, number_b, number_c)
                print("Product:", number_a * number_b * number_c)
                exit() #Se podría utilizar break pero habría que hacerlo tres veces