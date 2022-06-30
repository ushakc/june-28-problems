#Closures-Decorators Excercises

from datetime import datetime, timezone

#Closure Excercise
#Using a closure, create a function, multiples_of(n) which we can use to
#create generators that generate multiples of n less than a given number.
def multiples_of(n):
    def under(limit):
        i = 1
        while n*i < limit:
            yield n*i
            i += 1
    return under

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)
# output: 7 14 21 28
#----------------------------------------------------------------------

#Decorators Excercise 1
#@make_upper – make every letter of a string returned from the decorated
#function uppercase.
def make_upper(func):
    def wrap_func():
        return func().upper()
    return wrap_func

@make_upper
def hello_world():
    return 'hello young, good day!!'

print(hello_world()) # output: HELLO YOUNG, GOOD DAY!!
#-----------------------------------------------------------------------

#Decorators Excercise 2
#@print_func_name – print the name of the decorated function before
#executing the function.

def print_func_name(my_func):
    def wrapper():
        print(f"{my_func.__name__} is running...")
        my_func()
    return wrapper


@print_func_name
def my_func():
    print('Python is fun!!')

my_func() # output: my_func is running...
            #Python is fun
#----------------------------------------------------------------------

#Decoratos Excercise 3
#@give_name(name) – concatenate the given name at the end of a string
#returned from the decorated function.
def make_upper(lower_str):
    def str_toupper(*args):
        toupper = lower_str(*args)
        return toupper.upper()
    return str_toupper

@make_upper
def hello_world():
    return 'hello usha, good day!!'
def greeting():
    return 'Hello'

print(greeting()) # output: Hello Theresa
#---------------------------------------------------------------------

#Decorators Excercise 4
#@print_input_type – print a data type of the input argument before
#executing the decorated function.

def square(n):
    return n ** 2

print(square(3.5)) # output: The input data type is <class 'float'>
                    #12.25
#-------------------------------------------------------------------

#Decorators Excercise 5
#@check_return_type(return_type) – check if the return type of the
#decorated function is return_type and print the result before executing
#the function.

#pass in a string
def square(n):
    return n ** 2

print(square(6)) # output: =========Error!!
                    #The return type is NOT <class 'str'>
                    #36

#pass in a float
def square(n):
    return n ** 2

print(square(2.9)) # output: The return type is <class 'float'>
                    #8.41
#------------------------------------------------------------------------

#Decorators Excercise 6
#@execute_log – write a function execution log on the log file. (log below)

def log_file(func):
    def write_to(*args, **kwargs):
        print(f"{datetime.now()} {func.__name__}")
        return func(*args, **kwargs)
    return write_to
@log_file
def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult

def hello_world():
    return 'hello world!!'


print(multiply(6, 2, 3)) # 36
print(hello_world()) # hello world!!
print(multiply(2.2, 4)) # 8.8
print(hello_world()) # hello world!!


#function_execution.log
#2020-05-01 13:55:53.059315 multiply
#2020-05-01 13:55:53.060312 hello_world
#2020-05-01 13:55:53.060314 multiply
#2020-05-01 13:55:53.060323 hello_world