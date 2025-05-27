# import time


# def timer(func):
#     def wraps_func(*args, **kwargs):
#         st = time.time()
#         func(*args, **kwargs)
#         et = time.time()
#         return et - st
#     return wraps_func


# @timer
# def number_s():
#     return [i ** 2 for i in range(1000000)]

# @timer
# def number_c():
#     return [i ** 3 for i in range(1000000)]

# @timer
# def number_n(n):
#     return [i ** n for i in range(1000000)]



# print(number_s())
# print(number_c())
# print(number_n(5))

# ------------------------------------------------------------------
# def any_dec(func):
#     def wraps_func():
#         print('Hello !!!!')
#         return func()
#     return wraps_func

# @any_dec
# def test():
#     return "Hello bro!!!!"

# print(test())
# ------------------------------------------------------------------
# import time

# def sleep(func):
#     def wraps_func(*args, **kwargs):
#         time.sleep(3)
#         return func(*args, **kwargs)    
#     return wraps_func


# @sleep
# def func1():
#     return "Hello Mish"

# @sleep
# def func2():
#     return "Hello Lusine"

# print(func1())
# print(func2())
# ------------------------------------------------------------------
# import datetime


# def logging(func):
#     def wraps_func(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as ex:
#             with open('error.log', 'a') as file:
#                 file.write(f'{func.__name__}  {ex.__class__.__name__}  {datetime.datetime.now()}\n')
#             return "Open error.log file"
#     return wraps_func

# @logging
# def func1(a, b):
#     return a / b

# @logging
# def func2(a):
#     return a ** 2

# @logging
# def func3():
#     return 'a' + 5

# print(func1(5, 0))
# print(func2(4))
# print(func3())
# ------------------------------------------------------------------
# class Logger:

#     count = 0

#     def __init__(self, func):
#         self.func = func
#         Logger.count += 1

#     def __call__(self, *args, **kwargs):
#         return self.func(*args, **kwargs)
    
# @Logger
# def func1():
#     return 10

# @Logger
# def func2():
#     return 15 * 5

# @Logger
# def func3(a, b):
#     return a + b


# print(func1())
# print(func2())
# print(func3(4, 5))
# print('Count ->', Logger.count)
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# import time

# def sleep_n_second(n):
#     def sleep(func):
#         def wraps_func(*args, **kwargs):
#             time.sleep(n)
#             return func(*args, **kwargs)    
#         return wraps_func
#     return sleep


# @sleep_n_second(4)
# def func1():
#     return "Hello Mish"

# @sleep_n_second(1)
# def func2():
#     return "Hello Lusine"

# print(func1())
# print(func2())

# ------------------------------------------------------------------
# import time
# import functools

# def sleep(func):
#     @functools.wraps(wrapped=func)
#     def wraps_func(*args, **kwargs):
#         '''Wraps function'''
#         time.sleep(3)
#         return func(*args, **kwargs)    
#     return wraps_func

# @sleep
# def func1(a, b):
#     '''Best function'''
#     return a + b

# print(func1.__doc__)
# print(func1.__name__)
# ------------------------------------------------------------------
# try:
#     with open('registration.txt', 'r', encoding='utf-8') as file:
#         info = file.readlines()
#     for i in info:
#         info_list = i.split(' ')
#         if len(info_list) == 3:
#             if info_list[0].isalpha():
#                 if '@' in info_list[1] and '.' in info_list[1]:
#                     if 10 <= int(info_list[2]) <= 99:
#                         print('OK')
#                     else:
#                         raise ValueError('Error')
#                 else:
#                     raise SyntaxError("No @ and . :  ")
#             else:
#                 raise NameError("info list Name Error")
#         else:
#             raise IndexError("Info list index error")

# except FileNotFoundError:
#     print('No File')
# ------------------------------------------------------------------
