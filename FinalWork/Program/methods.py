import csv

from classes.Animal import Animal

def write_to_file(animal):
    with open("List of animals.csv", 'w', encoding='utf-8') as file:
        columns=['Тип', 'Подтип','Имя животного', 'Дата рождения', 'Команды, которые умеет выполнять животное']
        writer = csv.writer(file)
        writer.writerow(columns)     
        writer.writerow(animal)
