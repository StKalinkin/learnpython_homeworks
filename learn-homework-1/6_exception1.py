"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():
    hello = input("How are you? ")
    while True:
        try:
            hello == "Fine"
            print("Ok, I'm glad")

        except KeyboardInterrupt:
            print("Bye!")
        break

hello_user()