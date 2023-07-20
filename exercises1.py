#1 - מתי כדאי להשתמש ב range בלולאת for?


#2 - כיצד אפשר להגדיר range עם קפיצות? כיצד אפשר להגדיר range עם מספרים בסדר יורד?
print(list(range(0,10,2)))
lists = list(range(10))
lists.reverse()
print(lists)

#3 - כיצד אפשר לייצר list מתוך range?
print(list(range(1,10)))

#4 - מדוע יש צורך בלולאות מסוג while ו- while-do?
#5 - מה ההבדל בין לולאת while לבין לולאת while-do?
#6 - כיצד אפשר בפייטון לממש לולאת while-do?
#7 -  מה ההבדל בין break לבין continue ?מדוע כדאי להשתמש ב- continue?

#8 -  כתוב תוכנית המדפיסה את כל המספרים השלמים מ- 200 ועד 2 בסדר יורד
for i in range(200,1, -1):
    print(i)

#9 -  כתוב תוכנית המדפיסה את כל הכפולות של ,7 בטווח שבין 1 ל- 100 (נסה לכתוב בצורה יעילה)
for i in range(0,100, 7):
    print(i)


#10 - כתוב תוכנית הקולטת מספרים עד אשר נקלט מספר שלילי. הדפס את סכום המספרים שנקלט (ללא המספר השלילי)
sum=0
while True:
    number = int(input('Please Enter Number: '))
    if number < 0:
        break
    sum += number
print(f'The sum of the numbers is: {sum}')

#11 - כתוב תוכנית הקולטת מספר ומדפיסה את העצרת שלו.
number = int(input('Please Enter Number: '))
multi = 1
for num in range(1,number+1):
    multi = multi*num
    if num == number:
        break
print(f'The assembly of number {number} is: {multi}')


#12 - The code is inside the lucky_numbers.py file
