number = 5
factorial_num = 1

# for num in range(1, number + 1):
#     factorial_num *= num
#     num-=1
#     print(factorial_num)

while number > 0:
    factorial_num *= number
    number -= 1
    
    print(factorial_num)