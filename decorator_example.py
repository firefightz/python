class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in == True:
            print(f"{args[0].name} is logged in")
        else:
            print(f"{args[0].name} is NOT logged in")
    return wrapper_function

@is_authenticated_decorator
def create_blog_post(user):
    print(f"this is {user.name}'s new blog post")

new_user = User("warren")
new_user.is_logged_in = True

create_blog_post(new_user)

########################################################
# def logging_decorator(func):
#     def wrapper(*args):
#         print(f"You called {func.__name__}{args}")
#         result = func(*args)
#         print(f"It returned: {result}")
#         return result
#     return wrapper

# @logging_decorator
# def a_function(*args):
#     return sum(args)
    
# a_function(1,2,3)



