# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok that *args is pointless, do This
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#no arguments
def print_none():
    print("I got nothing")

print_two("Daniel", "King")
print_two_again("Daniel", "King")
print_one("Daniel")
print_none()
