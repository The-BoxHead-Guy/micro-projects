from random import randint

counter = int(input("From where do you want to start? "))

while counter < randint(a=1, b=10):
    print(f"Counter: {counter}")
    counter += 1

print("Counter has finished")
