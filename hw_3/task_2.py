# Author: Viktor Mamontov
# Функция принимает и возвращает данные пользователя

def new_person(name, surname, b_date, city, email, phone):
    new_contact = [name, surname, b_date, city, email, phone]
    return print(new_contact)


new_name = input("Введите имя: ")
new_surname = input('Введите фамилию: ')
new_b_date = input('Введите год рождения: ')
new_city = input('Введите город проживания: ')
new_email = input("Введите ваш email адрес: ")
new_phone = input('Введите номер телефона: ')
new_person(name=new_name, surname=new_surname, b_date=new_b_date, city=new_city, email=new_email, phone=new_phone)
