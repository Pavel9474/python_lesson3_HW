# Задача 1. Создайте файл. Запишите в него N первых
# элементов последовательности Фибоначчи.

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Введите число членов последовательности:"))
data = open('fibonachi.txt', 'a') 
for i in range(n+1):
    data.write((str(fibonacci(i))))
data.write('\n')
data.close()

# Задача 2. В файле находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на
# заданную букву.

def list_on_the_letter(list):
    list_on_letter=[]
    letter=input('Введите первую букву из названия фрукта: ')
    for i in range(len(list)):
        for j in list[i]:
            if j[0]==letter:
                list_on_letter.append(list[i].replace('\n',''))
    print(list_on_letter)

data = open('fruits.txt', encoding='utf8') 
fruits=data.readlines()
data.close()
list_on_the_letter(fruits)

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, 
# отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.


script_bot={'Привет':'Здарова!','как тебя зовут?':'Меня зовут дед Евстахий! а вас?', 'Что ты умеешь?':'Говорить как дед, ','Это как?':'Ну ты и фронтель!'}
answer_user=input ('Введите сообщение ')
if answer_user in script_bot:
    print(script_bot[answer_user])
else:
    print('Не ведаю что молвишь! Скажи что молвить я должен')
    answer_bot=input('Введите что бот должен ответить на ваш вопрос ')
    script_bot[answer_user]=answer_bot