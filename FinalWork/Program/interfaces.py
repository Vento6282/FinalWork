from methods import *
import datetime

def menu_main():

    command = '-1'
    while command != '0':
        print('-' * 100)
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
                show_animals()       
            case '3':   
                add_new_commands()          
            case '4':   
                menu_remove_animal()
            case '0':   
                print('-' * 100)
                print('До новых встреч!')
                print('-' * 100)

def menu_add_animal():

    # Выбор типа животного
    animal_type = '0'
    # while int(animal_type) <= 0 or int(animal_type) > len(animal_types):
    while int(animal_type) <= 0 or int(animal_type) > len(animal_types):
        print('-' * 100)
        print('Выберите вид животного:')
        for key in animal_types:
            print(f"{key}. {animal_types[key][1]}")
        print('0. В главное меню')
        animal_type = input('Введите пункт меню: ')
        if animal_type in ('','0'):
            menu_main()
        if animal_type.isdigit():
            if int(animal_type) < 0 or int(animal_type) > len(animal_types):
                print(f'Пункта с номером "{animal_type}" нет!')
        else:
            print(f'Пункта с номером "{animal_type}" нет!')
            animal_type = '0'

    flag = True
    while flag:
        print('-' * 100)
        animal_name = input('Введите имя животного: ')
        if is_name(animal_name):
            if animal_name =='0':
                menu_main()
            flag = False

    flag = True
    while flag:
        print('-' * 100)
        animal_birth_day = input('Введите дату рождения животного в формате 2024-07-15: ')
        if is_date(animal_birth_day):
            if animal_birth_day =='0':
                menu_main()
            animal_birth_day = datetime.datetime.strptime(animal_birth_day, "%Y-%m-%d")
            flag = False

    if is_duplicate_animal(animal_types[animal_type][1], animal_name, animal_birth_day):
         menu_add_animal()

    flag = True
    while flag:
        print('-' * 100) 
        animal_commands = input(f'Введите команды, которые {animal_name} уже знает, разделяя их запятой: ')
        if is_correct_commands(animal_commands):
            animal_commands = extract_animal_commands(animal_commands)
            flag = False
            
    animal = f'{animal_types[animal_type][2].lower()} {animal_types[animal_type][1].lower()} с именем {animal_name} и датой рождения {animal_birth_day}'
    answer = ''
    while answer.lower() != 'да':
        print('-' * 100)
        answer = input(f'Добавить {animal}? "да" или "нет": ')
        if answer.lower() == 'да':
            create_animal(animal_name,animal_types[animal_type][1],animal_birth_day,animal_commands)
            print(f'В реестр добавлено {animal}!')
        elif answer.lower() in ('нет'):
            menu_main()
        else:
            print('Введён некорретный ответ!')
    menu_main()

def show_animals():
    show_type = 'Тип: '
    show_animal = 'Животное: '
    show_name = 'Имя: '
    show_date = 'Дата рождения: '
    show_commands = 'Команды: '
    if not is_list_empty():
        print('-' * 100) 
        sizes = show_animal_sizes(show_type, show_animal, show_name, show_date, show_commands)
        print(f'{show_type}{' ' * (sizes[0] - len(show_type))}',
              f'{show_animal}{' ' * (sizes[1] - len(show_animal))}',
              f'{show_name}{' ' * (sizes[2] - len(show_name))}',
              f'{show_date}{' ' * (sizes[3] - len(show_date))}',
              f'{show_commands}{' ' * (sizes[4] - len(show_commands) + 1)}')
        print('-' * 100) 
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().strip().split('\n') 
    for animal_str in animal_list:
        animal = animal_str.split(';')
        print(f'{animal[0]}{' ' * (sizes[0] - len(animal[0]))}',
              f'{animal[1]}{' ' * (sizes[1] - len(animal[1]))}',
              f'{animal[2]}{' ' * (sizes[2] - len(animal[2]))}',
              f'{animal[3]}{' ' * (sizes[3] - len(animal[3]))}',
              f'{animal[4]}{' ' * (sizes[4] - len(animal[4]))}')

def menu_remove_animal():
    if not is_list_empty():
        flag = True
        while flag:
            print('-' * 100) 
            name_for_delete = input('Введите имя животного, которое необходимо удалить из реестра: ')
            
            if name_for_delete == '':
                print('Удаление отменено!')
                menu_main()
            animal_list = search_name(name_for_delete)
            if animal_list == 0:
                menu_main()
            if len(animal_list) == 1:
                flag = False
                answer = ''
                while answer.lower() not in ('да', 'нет'):
                    print('-' * 100) 
                    answer = input(f'Удалить животное {animal_list[0][1].lower()} с именем {animal_list[0][2]} и датой рождения {animal_list[0][3]}? "да" или "нет": ')
                    if answer.lower() == 'да':
                        delete_animal(animal_list[0][5])
                        print('-' * 100) 
                        print(f'Животное {animal_list[0][1].lower()} с именем {animal_list[0][2]} и датой рождения {animal_list[0][3]} удалено!')
                    elif answer.lower() == 'нет':
                        menu_main()
                    else:
                        print('Введён некорретный ответ!')
            else:

                # if animal_type.isdigit():
                #     if int(animal_type) < 0 or int(animal_type) > len(animal_types):
                #         print(f'Пункта с номером "{animal_type}" нет!')


                answer = '0'
                while answer < '1' or answer > str(len(animal_list)):
                    print('-' * 100) 
                    print(f'С именем {name_for_delete} найдено несколько животных: ')
                    for animal in animal_list:
                        print(f'{animal[0]}. Удалить животное {animal[1].lower()} и датой рождения {animal[3]}')
                    print('0. В главное меню')
                    answer = input('Введите пункт меню: ')
                    if answer == '0':
                        menu_main()
                    if answer > '0' and answer <= str(len(animal_list)):
                        answer_yn = ''
                        while answer_yn.lower() not in ('да','нет'):
                            print('-' * 100) 
                            answer_yn = input(f'Удалить животное {animal_list[int(answer)-1][1].lower()} с именем {animal_list[int(answer)-1][2]} и датой рождения {animal_list[int(answer)-1][3]}? "да" или "нет": ')
                            if answer_yn.lower() == 'да':
                                delete_animal(animal_list[int(answer)-1][5])
                                print('-' * 100) 
                                print(f'Животное {animal_list[int(answer)-1][1].lower()} с именем {animal_list[int(answer)-1][2]} и датой рождения {animal_list[int(answer)-1][3]} удалено!')
                            elif answer_yn.lower() == 'нет':
                                menu_main()
                            else:
                                print('Введён некорретный ответ!')
                    else:
                        print('Введён некорретный ответ!')
                flag = False
                
def add_new_commands():
    if not is_list_empty():
        flag = True
        while flag:
            print('-' * 100) 
            name_for_learning = input('Введите имя животного, которого необходимо обучить новым командам: ')
            
            if name_for_learning == '':
                print('Обучение отменено!')
                menu_main()
            animal_list = search_name(name_for_learning)
            if animal_list == 0:
                menu_main()
            if len(animal_list) == 1:
                flag = False
                answer = ''
                while answer.lower() not in ('да', 'нет'):

                    if animal_list[0][4] =='':
                        new_command = ''
                        if is_correct_commands(new_command):
                            print('-' * 100) 
                            print(f'{animal_list[0][1]} {animal_list[0][2]} пока не знает ни одной команды.')
                            new_command = input('Введите через запятую команды , которые нужно добавить : ')
                            new_command = extract_animal_commands(new_command)
                            print(new_command)

                    print('-' * 100) 
                    answer = input(f'Обучить животное {animal_list[0][1].lower()} с именем {animal_list[0][2]} и датой рождения {animal_list[0][3]}? "да" или "нет": ')
                    if answer.lower() == 'да':
                        pass
                    elif answer.lower() == 'нет':
                        menu_main()
                    else:
                        print('Введён некорретный ответ!')
            else:
                answer = '0'
                while answer < '1' or answer > str(len(animal_list)):
                    print('-' * 100) 
                    print(f'С именем {name_for_learning} найдено несколько животных: ')
                    for animal in animal_list:
                        print(f'{animal[0]}. Удалить животное {animal[1].lower()} и датой рождения {animal[3]}')
                    print('0. В главное меню')
                    answer = input('Введите пункт меню: ')
                    if answer == '0':
                        menu_main()
                    if answer > '0' and answer <= str(len(animal_list)):
                        answer_yn = ''
                        while answer_yn.lower() not in ('да','нет'):
                            print('-' * 100) 
                            answer_yn = input(f'Удалить животное {animal_list[int(answer)-1][1].lower()} с именем {animal_list[int(answer)-1][2]} и датой рождения {animal_list[int(answer)-1][3]}? "да" или "нет": ')
                            if answer_yn.lower() == 'да':
                                delete_animal(animal_list[int(answer)-1][5])
                                print('-' * 100) 
                                print(f'Животное {animal_list[int(answer)-1][1].lower()} с именем {animal_list[int(answer)-1][2]} и датой рождения {animal_list[int(answer)-1][3]} удалено!')
                            elif answer_yn.lower() == 'нет':
                                menu_main()
                            else:
                                print('Введён некорретный ответ!')
                    else:
                        print('Введён некорретный ответ!')
                flag = False