original_list = [5, 3, 2, 6, 12]
numbers_list = [5, 3, 2, 6, 12]
attempts = 0
while True:
    user_number = int(input('Please Enter Number: '))
    attempts = attempts+1
    if attempts < 20:
        if user_number in range(2,49):
            if user_number in numbers_list:
                numbers_list.remove(user_number)
                print(numbers_list)
                if not numbers_list:
                  print(f'Congratulations!!! Attempts Quantity: {attempts}')
                  break
            else:
                print('The number is incorrect, try again.')
        else:
            continue
    else:
        numbers_list = original_list.copy()
        attempts = 0
        print('You have exceeded the number of attempts, start again!')
        print(numbers_list)
        continue