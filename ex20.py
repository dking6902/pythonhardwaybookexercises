from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

prompt = '> '
current_file = open(input_file)

print("Let's print the whole file:\n")

print_all(current_file)

print("Now let's do it in rewind.")

rewind(current_file)

# print("Let's print three lines:")
#
# current_line = 1
# print_a_line(current_line, current_file)
#
# current_line = current_line + 1
# print_a_line(current_line, current_file)
#
# current_line = current_line + 1
# print_a_line(current_line, current_file)
#


# This point onwards is me experimenting

print("What line would you like to print out?")
user_choice = input(prompt)
# print(user_choice)
current_line = int(user_choice)
print(current_line)
print_a_line(current_line, current_file)
