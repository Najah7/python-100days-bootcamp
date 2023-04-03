class User:
    def __init__(self, username):
        self.username = username
        self.is_logged_in = False

    def __repr__(self):
        return f"{self.username}"

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("Please authenticate.")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"{user} is creating a blog post...")

new_user = User("tuser")
create_blog_post(new_user)
    
    