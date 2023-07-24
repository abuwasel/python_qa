import random


def greet_with_name(fname,lname):
    print(f'helloo {fname} {lname}')

greet_with_name('soo','dodo')

def avg(*xargs):
    print(sum(xargs) / len(xargs))

avg(10,20,30)


def foo(name,*args):
    print(name)
    if args:
        for a in args:
            print(a)

foo('ibrahim','adam','sami')


def print_only_id(**kwargs):
    print(kwargs)

print_only_id(name='hodi',id=2)


def gen_list(start: int,end: int = 20):
    l = list(range(start,end+1))
    print(l)

gen_list(5,10)
#gen_list(5)

def get_random():
    return random.randint(0, 100)

print(get_random())


def love_calc(name:str,crush:str):
    love = get_random()
    return f'{name} {love}% {crush}'

print(love_calc('adam','mila'))