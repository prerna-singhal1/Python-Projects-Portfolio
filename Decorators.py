
def add_sprinkles(funcn):
    def wrapper(*args, **kwargs):
        print("# You have added sprinkles in your ice cream.🧁")
        funcn(*args, **kwargs)
    return wrapper

def add_fudge(funcn):
    def wrapper(*args, **kwargs):
        print("# You have added fudge in your ice cream.🍫")
        funcn(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream.🍨")

get_ice_cream("chocolate")