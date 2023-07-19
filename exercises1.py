#1


#2
print(list(range(0,10,2)))
lists = list(range(10))
lists.reverse()
print(lists)

#3
print(list(range(1,10)))

#4
#5
#6
#7

#8
list_down = list(range(2,201))
list_down.reverse()
print(list_down)

#9
for x in range(1,101):
    print(f'{x} x 7 = {x*7}')

#10
sum=0
while True:
    number = int(input('Please Enter Number: '))
    if number < 0:
        break
    sum += number
print(f'The sum of the numbers is: {sum}')

#11
number = int(input('Please Enter Number: '))
multi = 1
for num in range(1,number+1):
    multi = multi*num
    if num == number:
        break
print(f'The assembly of number {number} is: {multi}')


#12 - The code is inside the lucky_numbers.py file
