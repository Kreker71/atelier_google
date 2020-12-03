print("Curs3")
#
# myvar = 3
# if myvar < 5:
#     print("variabila este mai mica decat 5")
# elif myvar < 10:
#     print("Variabila mea este mai mica si decat 10")
#
# def my_function(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     for arg in args:
#         print(f'arg is {arg}')
#     for key in kwargs.keys():
#         print(f'key {key} has value {kwargs[key]}')
#
#
#     print("-" * 50)
#
# my_function('ana', 'are', 'mere')
# my_function(1, 2, 3, name='ana', verb='are', complement='mare')

# while True:
#     myvar = input("Introduceti un nr: ")
#     try:
#         myint = int(myvar)
#         print(myint)
#     except ValueError as e:
#         print('va rog introduceti un nr intreg', e)
#     except NameError as e:
#         print("ai folosti o variabila nedefinita")
#         pass
#     else:
#         print("nicio exceptie")
#     finally:
#         print("se executa tot timpul")
#
def my_func():
    def my_sec_func():
        print(f'my second functions {msg}')

    my_sec_func()

my_func()