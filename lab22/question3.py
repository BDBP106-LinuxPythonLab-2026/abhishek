count = 0
def count_calls(func):
    def wrapper():
        global count
        count += 1
        func()
        print(f"Call count: {count}")
    return wrapper
@count_calls
def say_hi():
        print("Hi!")
say_hi()
say_hi()
say_hi()