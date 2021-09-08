#first practice - Hello World!

print('Hello World!')
print(2 + 2)
print(10/3)

#second practice - variables
name = input("What's your name? ")
print("Hi", name)

#third practice - simple type of data
a = 2
b = 0.5
print(a + b)

name = input("What's your name? ")
print(f"hi, {name}.".capitalize())

name = input('Введите Ваше имя: ').upper()
print(f"Привет, {name}! Как дела?")

v = int(input('Введите число от 1 до 10: '))
print(v + 10)

print(float('1'))
print(int(2.5))
print(bool('1'))
print(bool(''))
print(bool(0))

#fourth task - lists
mylist = [3, 5, 7, 9, 10.5]
print(mylist)
mylist.append("Python")
print(mylist)
print(len(mylist))
print(mylist[0])
print(mylist[-1])
print(mylist[1:4])
mylist.remove("Python")
print(mylist)

#fifth task - dictionaries
mydict = {
    "city": "Moscow",
    "temperature": "20"
    }
print(mydict["city"])

mydict["temperature"] = int(mydict["temperature"]) - 5
print(mydict)
print(mydict.get("country", "Russia"))
mydict["date"] = "27.05.2019"
print(mydict)
print(len(mydict))

#sixth task - functions
def get_summ(one, two, delimiter="&"):
    summ = one + delimiter + two
    return summ.upper()

print(get_summ('Learn', 'python'))

#file price.py
def format_price(price):
    price = int(price)
    total_price = f'Cost: {price} rub.'
    return(total_price)

print(format_price(56.24))