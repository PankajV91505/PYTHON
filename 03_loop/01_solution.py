numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_count = 0
negative_num_count = 0
for number in numbers:
    if number > 0:
        positive_num_count += 1
    elif number < 0:
        negative_num_count += 1
print(negative_num_count)
print(positive_num_count)
