import time
import random

leaves = 0
water = 0
light = 0
day_count = 0

chosen_condition = ["Sunny", "Rainy", "Hot"]
temperature = range(-10, 40)

print("Woah, a new package arrived!")
time.sleep(2)
print("What is that?")
time.sleep(3)
print("No way! It's a plant!")
time.sleep(3)
name = input("How do you want to name your new plant?\n")

def wait():
    time.sleep(2)
    print("waiting for the next day.")
    time.sleep(1)
    print("waiting for the next day..")
    time.sleep(1)
    print("waiting for the next day...")

def weather():
    global water
    global light
    global name
    if condition == "Sunny":
        print("It's chilly outside...")
        time.sleep(2)
        print(f"{name} is enjoying the sunny weather")
        time.sleep(3)
        light = light + 1
        time.sleep(3)
        print(f"{name} has received 1 light")

    elif condition == "Rainy":
        print("It's raining outside!")
        time.sleep(2)
        print(f"{name} is drinking a lot of water, but can't find any light")
        time.sleep(4)
        water = water + 2
        light = light - 1
        time.sleep(3)
        print(f"{name} has received 2 water, but lost 1 light")


    elif condition == "Hot":
        print("It's very hot!")
        time.sleep(2)
        print(f"{name} is getting thirsty fast!")
        time.sleep(3)
        light = light + 2
        water = water - 1
        time.sleep(3)
        print(f"{name} has received 2 light, but lost 1 water")

    if water < 0:
        water = 0
    if light < 0:
        light = 0

    return water, light

def grow():
    global leaves
    global name
    global water
    global light
    if light >=2 and water >= 1:
       print(f"{name} is able to grow leaves")
       time.sleep(3)
       print(f"Do you wish for {name}, to grow 2 leaves?")
       choice = input("yes\nno\n")
       if choice.lower == "yes":
           leaves = leaves + 2
           water = water - 1
           light = light - 2
           time.sleep(3)
           print(f"{name} is using water and light to grow leaves.")
           time.sleep(1)
           print(f"{name} is using water and light to grow leaves..")
           time.sleep(1)
           print(f"{name} is using water and light to grow leaves...")
           time.sleep(3)
           print(f"{name} has grown 2 leaves!")
           time.sleep(4)
           print(f"{name} has now {leaves} leaves!")
           time.sleep(2)
           print(f"{name} has now also only {water} water and {light} light")
           return water, light, leaves
       else:
           print(f"Okay, no leaves for {name}")
           return water, light, leaves

    else:
        print(f"{name} doesn't have enough light and water to grow leaves :(")
        return water, light, leaves

def random_day():
    global condition
    global temperature
    condition = random.choice(chosen_condition)
    temperature = random.randint(-10, 40)
    return condition, temperature

time.sleep(2)
print(f"Let's welcome {name} to the new world!")


while True:
    condition, temperature = random_day()
    time.sleep(3)
    day_count = day_count + 1
    print(f"It's the {day_count}. day!" )
    time.sleep(2)
    print(f"Today's weather forecast is: {condition} and the temperature is {temperature}")
    time.sleep(4)
    print(f"{name} woke up!")
    time.sleep(2)
    weather()
    time.sleep(3)
    print(f"{name} has {water} water and {light} light")
    time.sleep(5)
    print("It's getting dark.")
    time.sleep(1)
    print("It's getting dark..")
    time.sleep(1)
    print("It's getting dark...")
    time.sleep(2)
    print(f"{name} is sleeping")
    time.sleep(3)
    grow()
    time.sleep(3)
    print("The next day is arriving...")
    wait()
    time.sleep(2)







