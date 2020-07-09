from functools import wraps

def capitalize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        orig_val = func(*args, **kwargs)

        capitalized = orig_val.upper()

        return capitalized

    return wrapper


def destination_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Sure, I\'d love to go "{orig_val}" !!!!!'

    return wrapper


@destination_decorator
@capitalize
def vacation_suggestion(destination):
    return destination

if __name__ == "__main__":
    # print(proclaim('spam is better than eggs'))
    # print(proclaim("Want to go for a walk?"))

    print(vacation_suggestion('China'))
