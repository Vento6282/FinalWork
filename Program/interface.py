from methods import *
import datetime

# визуализация и реализация пунктов основного меню
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

# визуализация и реализация пункта "Добавить животное"
def menu_add_animal():

    # Выбор типа животного
    animal_type = '0'
    while int(animal_type) <= 0 or int(animal_type) > len(animal_types):
        print('-' * 100)
        print('Выберите вид животного:')
        for key in animal_types:
            print(f"{key}. {animal_types[key][1]}")
        print('0. В главное меню')
        animal_type = input('Введите пункт меню: ')
        if animal_type in ('0'):
            menu_main()
        if animal_type.isdigit():
            if int(animal_type) < 0 or int(animal_type) > len(animal_types):
                print(f'Пункта с номером "{animal_type}" нет!')
        else:
            print(f'Пункта с номером "{animal_type}" нет!')
            animal_type = '0'

    # Ввод имени животного
    flag = True
    while flag:
        print('-' * 100)
        animal_name = input('Введите имя животного: ')
        if is_name(animal_name):
            if animal_name =='0':
                menu_main()
            flag = False
    animal_name = animal_name.strip()

    # Ввод даты рожденяи животного
    flag = True
    while flag:
        print('-' * 100)
        animal_birth_day = input('Введите дату рождения животного в формате 2024-07-15: ')
        if is_date(animal_birth_day):
            if animal_birth_day =='0':
                menu_main()
            animal_birth_day = datetime.datetime.strptime(animal_birth_day, "%Y-%m-%d")
            flag = False

    # Проверка, есть ли уже животное с указанными типом, именем и датой рождения
    if is_duplicate_animal(animal_types[animal_type][1], animal_name, animal_birth_day):
         menu_add_animal()

    # Ввод команд животного
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
        print(f'Добавить {animal}?')
        answer = input('Введите "да" или "нет": ')
        if answer.lower() == 'да':
            new_animal = create_animal(animal_name,animal_types[animal_type][1],animal_birth_day,animal_commands)
            write_to_file(f'{animal_classes[new_animal.get_parent_type()]};{new_animal.get_type()};{new_animal.get_name()};{new_animal.get_birth_day()};{new_animal.commands}')
            print('-' * 100)
            print(f'В реестр добавлено {animal}!')
        elif answer.lower() =='нет':
            menu_main()
        else:
            print('Введён некорретный ответ!')
    menu_main()

# визуализация и реализация вывода таблицы с животными
def show_animals():
    show_type = 'Тип: '
    show_animal = 'Животное: '
    show_name = 'Имя: '
    show_date = 'Дата рождения: '
    show_commands = 'Команды: '
    if not is_list_empty():
        print('-' * 100) 
        sizes = show_animal_sizes(show_type, show_animal, show_name, show_date, show_commands)
        print(f'{show_type}{' ' * (sizes[0] - len(show_type)+ 1)}',
              f'{show_animal}{' ' * (sizes[1] - len(show_animal)+ 1)}',
              f'{show_name}{' ' * (sizes[2] - len(show_name)+ 1)}',
              f'{show_date}{' '}',
              f'{show_commands}{' ' * (sizes[4] - len(show_commands)+ 1)}')
        print('-' * 100) 
    with open('FinalWork\Program\List of animals.csv', 'r', encoding='UTF-8') as file:
        animal_list = file.read().strip().split('\n') 
    for animal_str in animal_list:
        animal = animal_str.split(';')
        print(f'{animal[0]}{' ' * (sizes[0] - len(animal[0])+ 1)}',
              f'{animal[1]}{' ' * (sizes[1] - len(animal[1])+ 1)}',
              f'{animal[2]}{' ' * (sizes[2] - len(animal[2])+ 1)}',
              f'{animal[3][:-9]}{' ' * 6}',
              f'{animal[4]}{' ' * (sizes[4] - len(animal[4])+ 1)}')

# визуализация и реализация пункта "Удалить животное"
def menu_remove_animal():
    if not is_list_empty():
        flag = True
        while flag:

            name_for_delete = ''
            while len(name_for_delete.strip()) == 0:
                print('-' * 100)
                name_for_delete = input('Введите имя животного, которого необходимо удалить из реестра: ') 
                if len(name_for_delete) == 0:
                    print('Удаление отменено!')
                    menu_main()
                if len(name_for_delete.strip()) == 0:
                    print('Имя не может быть пустым или состоять из одних пробелов!')
            animal_list = search_name(name_for_delete)
            if animal_list == 0:
                menu_main()
            print('-' * 100)
            for animal in animal_list:
                print(f'{animal[0]}. Удалить {animal[1].lower()} {animal[2].lower()} по имени {animal[3]} с датой рождения {animal[4][:-9]}.')
            print('0. Выход в главное меню.')
            
            answer = input('Введите пункт меню: ') 
            if answer == '0':
                menu_main()
            if answer.isdigit() and int(answer) > 0 and int(answer) <= len(animal_list):
                index = int(answer) - 1 # Приводим номер нужной записи в соответствеие с индексом массива
                confirm = ''
                while confirm.lower() != 'да':
                    animal = f'{animal_list[index][1].lower()} {animal_list[index][2].lower()} по имени {animal_list[index][3]} с датой рожденяи {animal_list[index][4][:-9]}'
                    print('-' * 100)
                    print(f'Удалить {animal}')
                    confirm = input('Введите "да" или "нет": ')
                    if confirm.lower() == 'нет':
                        menu_main()
                    if confirm.lower() == 'да':
                        delete_animal(animal_list[index][6])
                        print('-' * 100)
                        print(f'Из реестра удалено {animal}')
                        flag = False
                    elif len(confirm.strip()) == 0:
                        print('Необходимо ввести "да" или "нет"!')
                    else:
                        print('Необходимо ввести "да" или "нет"!')
            else:
                print(f'Пункта с номером "{answer}" нет!')

# визуализация и реализация пункта "Обучить животное новым командам"                
def add_new_commands():
    if not is_list_empty():
        flag = True
        while flag:
            name_for_learning = ''
            while len(name_for_learning.strip()) == 0:
                print('-' * 100)
                name_for_learning = input('Введите имя животного, которого необходимо обучить новым командам: ') 
                if len(name_for_learning) == 0:
                    print('Добавление команд отменено!')
                    menu_main()
                if len(name_for_learning.strip()) == 0:
                    print('Имя не может быть пустым или состоять из одних пробелов!')
            animal_list = search_name(name_for_learning)
            if animal_list == 0:
                menu_main()
            print('-' * 100)
            for animal in animal_list:
                print(f'{animal[0]}. Обучить {animal[1].lower()} {animal[2].lower()} по имени {animal[3]} с датой рождения {animal[4][:-9]}.')
            print('0. Выход в главное меню.')
            answer = input('Введите пункт меню: ') 
            if answer == '0':
                menu_main()
            if answer.isdigit() and int(answer) > 0 and int(answer) <= len(animal_list):
                index = int(answer) - 1 # Приводим номер нужной записи в соответствеие с индексом массива
                if animal_list[index][5] =='':
                    print('-' * 100) 
                    print(f'{animal_list[index][2]} {animal_list[index][3]} пока не знает ни одной команды.')
                else:
                    print('-' * 100) 
                    print(f'{animal_list[index][2]} {animal_list[index][3]} уже знает команды: {animal_list[index][5]}.')
                new_command = input('Введите через запятую команды, которые нужно добавить: ')
                if new_command == '':
                    print('Добавление команд отменено!')
                    menu_main()
                if is_correct_commands(new_command):
                    animal_list[index][5] = extract_animal_commands(animal_list[index][5] +','+ new_command)
                    write_to_file(f'{animal_list[index][1]};{animal_list[index][2]};{animal_list[index][3]};{animal_list[index][4]};{animal_list[index][5]}')
                    delete_animal(animal_list[index][6])
                    flag = False
            else:
                print(f'Пункта с номером "{answer}" нет!')