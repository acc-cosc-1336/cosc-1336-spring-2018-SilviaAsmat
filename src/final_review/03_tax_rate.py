RATE = .08
num = 0
index = 0
sum_num = 0

while index < 3:
    num = int(input('enter number: '))
    sum_num += num
    index += 1

print('sum', 'tax', 'total')
print(sum_num, sum_num * RATE, sum_num * RATE + sum_num)
