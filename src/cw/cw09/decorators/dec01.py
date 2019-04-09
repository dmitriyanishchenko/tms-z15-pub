def my_decorator(func):
   def do_some_staff():
       # some action
       func()
       # some action
   return do_some_staff


@my_decorator
def my_func():
   pass

my_new_func = my_decorator(my_func)
my_new_func()