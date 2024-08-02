from methods import *

def menu_main():
    command = '-1'
    while command != '0':

        print('-' * 60)
        print('Главное меню:\n'
            '1. Добавить новое животное\n'
            '2. Вывести всех животных\n'
            '3. Обучить животное новой команде\n'
            '4. Удалить животное из списка\n'
            '0. Выход из программы')
        
        command = input('Введите пункт меню: ')
        
        if (command not in ('1', '2', '3', '4', '0')):
            print('Пункта с таким номером нет!')

        match command:
            case '1':   
                menu_add_animal()
            case '2':    
                #show_animals()
                print(2)          
            case '3':   
                #to_teach_animal_to_commands()
                print(3)            
            case '4':   
                #remove_animal()
                print(4)
            case '0':   
                print('-' * 60)
                print('До новых встреч!')
                print('-' * 60)

def menu_add_animal():

    animal_type = '-1'
    while animal_type < '0' or animal_type > str(len(animal_types)):
        print('-' * 60)
        print('Выберите вид животного:')
        for key in animal_types:
            print(f"{key}. {animal_types[key][1]}")
        print('0. В главное меню')
        animal_type = input('Введите пункт меню: ')
        if(animal_type == '0'):
            menu_main()
        if animal_type < '0' or animal_type > str(len(animal_types)):
            print('Пункта с таким номером нет!')
    
    print('-' * 60)
    animal_name = input('Введите имя животного: ')
    while not check_animal_name(animal_name):
        print('-' * 60)
        animal_name = input('Введите имя животного: ').strip()
    
    print('-' * 60)
    animal_birth_day = input('Введите дату рождения животного в формате 2024-07-15: ')
    while not check_date(animal_birth_day):
        print('-' * 60)
        animal_birth_day = input('Введите дату рождения животного в формате 2024-07-15: ')

    if not check_duplicate_animal(animal_name, animal_types[animal_type][1], animal_birth_day):
         menu_add_animal()

    question = ''
    answer = ''
    while answer !='yes':
        print('-' * 60) 
        animal_commands = input(f'Введите команды, которые {animal_name} уже знает: ')     
        commands_str = extract_animal_commands(animal_commands)
        if commands_str == '':
            answer = input('Оставить поле с командами пустым? "yes" или "no": ')
        else:
            answer = input(f'Оставить эти команды: {commands_str}? "yes" или "no": ')
        if answer not in ('yes', 'no'):
            print('Введён некорретный ответ!')
            
    question = f'{animal_types[animal_type][2].lower()} {animal_types[animal_type][1].lower()} с именем {animal_name} и датой рождения {animal_birth_day}'
    print(question)
    answer = ''
    while answer not in ('yes','no'):
        print('-' * 60)
        answer = input(f'Добавить {question}? "yes" или "no": ')
        if answer == 'yes':
            create_animal(animal_name,animal_types[animal_type][1],animal_birth_day,commands_str)
        elif answer == 'no':
            menu_main()
        else:
            print('Введён некорретный ответ!')
    menu_main()