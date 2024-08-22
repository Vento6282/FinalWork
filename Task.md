# Задание

1. Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животные (заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).

Вывод команд:
```
student@Ubuntu:~$ nano Pets.txt
student@Ubuntu:~$ nano PackAnimals.txt
student@Ubuntu:~$ cat PackAnimals.txt Pets.txt > HumanFriends.txt
student@Ubuntu:~$ ls
Desktop  Documents  Downloads  HumanFriends.txt  Music  PackAnimals.txt  Pets.txt  Pictures  Public  snap  Templates  Videos
```

2. Создать директорию, переместить файл туда.

Вывод команд:
```
student@Ubuntu:~$ mkdir Animals
student@Ubuntu:~$ mv HumanFriends.txt Animals/
student@Ubuntu:~$ ls Animals/
HumanFriends.txt
```

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория.

Вывод команд:
```
student@Ubuntu:~$ sudo apt-get install mysql-server -y
```

4. Установить и удалить deb-пакет с помощью dpkg.

Вывод команд:
```
student@Ubuntu:~$ curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
student@Ubuntu:~$ echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
student@Ubuntu:~$ sudo apt update
student@Ubuntu:~$ apt download nginx
student@Ubuntu:~$ sudo dpkg -i nginx_1.24.0-1~jammy_amd64.deb
student@Ubuntu:~$ sudo dpkg -r nginx
student@Ubuntu:~$ sudo dpkg -P nginx
```

5. Выложить историю команд в терминале ubuntu

Вывод команд:
```
   46  nano Pets.txt
   47  nano PackAnimals.txt
   48  cat PackAnimals.txt Pets.txt > HumanFriends.txt
   49  ls
   50  mkdir Animals
   51  mv HumanFriends.txt Animals/
   52  ls Animals/
   53  sudo apt-get install mysql-server
   54  sudo service mysql status
   55  mysql -u student -p
   56  sudo mysql_secure_installation
   57  mysql -u student -p
   58  mysql -u root -p
   59  sudo mysql_secure_installation
   60  mysql -u root -p
   61  sudo mysql_secure_installation
   62  mysql -u root -p
   63  sudo mysql
   64  sudo apt install curl
   65  curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | sudo /keyrings/nginx-archive-keyring.gpg >/dev/null
   66  echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx"     | sudo tee /etc/apt/sources.list.d/nginx.list
   67  sudo apt update
   68  apt download nginx
   69  sudo dpkg -i nginx_1.24.0-1~jammy_amd64.deb
   70  sudo dpkg -i nginx_1.26.1-2~jammy_amd64.deb
   71  sudo dpkg -r nginx
   72  sudo dpkg -P nginx
```

6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние
животные и вьючные животные, в составы которых в случае домашних
животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
войдут: Лошади, верблюды и ослы

7. В подключенном MySQL репозитории создать базу данных “Друзья
человека”

Вывод команд:
```
CREATE DATABASE Human_friends;
```

8. Создать таблицы с иерархией из диаграммы в БД

Вывод команд:
```
USE Human_friends;

CREATE TABLE animals
(
	Id INT AUTO_INCREMENT PRIMARY KEY, 
	Name VARCHAR(20)
);

CREATE TABLE pets
(
	Id INT AUTO_INCREMENT PRIMARY KEY,
    Id_animals INT,
    Name VARCHAR (20),
    FOREIGN KEY (Id_animals) REFERENCES animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
 
CREATE TABLE pack_animals
(
	Id INT AUTO_INCREMENT PRIMARY KEY,
    Id_animals INT,
    Name VARCHAR (20),
    FOREIGN KEY (Id_animals) REFERENCES animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE cats 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Id_pets int,
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(50),
    Foreign KEY (Id_pets) REFERENCES pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE dogs 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
	Id_pets int,
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(50),
    Foreign KEY (Id_pets) REFERENCES pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE hamsters 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Id_pets int,
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(50),
    Foreign KEY (Id_pets) REFERENCES pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE horses 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Id_pack_animals int,
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(50),
    Foreign KEY (Id_pack_animals) REFERENCES pack_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE camels 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Id_pack_animals int,
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(50),
    Foreign KEY (Id_pack_animals) REFERENCES pack_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE donkeys 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Id_pack_animals int,
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(50),
    Foreign KEY (Id_pack_animals) REFERENCES pack_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO animals (name) 
VALUES 
	('Pets'),
	('Pack Animals');
	
INSERT INTO pets (Id_animals, name) 
VALUES 
	(1, 'Cats'),
	(1, 'Dogs'),
	(1, 'Hamsters');
	
INSERT INTO pack_animals (Id_animals, name) 
VALUES 
	(2, 'Horses'),
	(2, 'Camels'),
	(2, 'Donkeys');
```

9. Заполнить низкоуровневые таблицы именами(животных), командами
которые они выполняют и датами рождения

Вывод команд:
```
INSERT INTO cats (Id_pets, Name, Birthday, Commands)
VALUES 
	(1, 'Zeus', '2019-07-15', 'Meow, Sit, Jump'),
	(1, 'Maui', '2022-01-09', 'Meow'),  
	(1, 'Loki', '2021-11-02', 'Scratch'); 
	
INSERT INTO dogs (Id_pets, Name, Birthday, Commands)
VALUES 
	(2, 'Max', '2022-10-21', 'Paw'),
	(2, 'Bonnie', '2023-03-11', 'Sit, '),  
	(2, 'Barney', '2021-02-12', 'Paw'); 
	
INSERT INTO hamsters (Id_pets, Name, Birthday, Commands)
VALUES 
	(3, 'Buster ', '2023-12-31', 'Roll'),
	(3, 'Otto', '2024-02-02', 'Roll'),  
	(3, 'Peanut', '2024-01-30', 'Play dead'); 

INSERT INTO horses (Id_pack_animals, Name, Birthday, Commands)
VALUES 
	(1, 'Orion', '2014-09-11', 'Gallop, Paw'),
	(1, 'Mango', '2012-06-21', 'Gallop'),  
	(1, 'Zeus', '2020-05-03', 'Kick'); 
	
INSERT INTO camels (Id_pack_animals, Name, Birthday, Commands)
VALUES 
	(2, 'Lilo', '2004-06-28', 'Sit, Walk'),
	(2, 'Nala', '2018-11-08', 'Sit, Walk'),  
	(2, 'Archie', '2010-04-10', 'Sit, Walk, Carry Load'); 
	
INSERT INTO donkeys (Id_pack_animals, Name, Birthday, Commands)
VALUES 
	(3, 'Nacho', '2017-10-02', 'Walk, Stay, Carry Load '),
	(3, 'Olaf', '2016-01-01', 'Walk, Stay, Carry Load '),  
	(3, 'Archie', '2024-03-08', 'Walk, Carry Load '); 
```

10. Удалите из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. 

Вывод команд:
```
DELETE FROM camels;
```

Объединить таблицы лошади и ослы в одну таблицу.\
Вывод команд:
```
SELECT Id, Id_pack_animals, Name, Birthday, Commands 
FROM horses 
UNION 
SELECT Id, Id_pack_animals, Name, Birthday, Commands 
FROM donkeys;
```
Результат:
```
+----+-----------------+--------+------------+-------------------------+
| Id | Id_pack_animals | Name   | Birthday   | Commands                |
+----+-----------------+--------+------------+-------------------------+
|  1 |               1 | Orion  | 2014-09-11 | Gallop, Paw             |
|  2 |               1 | Mango  | 2012-06-21 | Gallop                  |
|  3 |               1 | Zeus   | 2020-05-03 | Kick                    |
|  1 |               3 | Nacho  | 2017-10-02 | Walk, Stay, Carry Load  |
|  2 |               3 | Olaf   | 2016-01-01 | Walk, Stay, Carry Load  |
|  3 |               3 | Archie | 2024-03-08 | Walk, Carry Load        |
+----+-----------------+--------+------------+-------------------------+
```
11. Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице

Вывод команд:
```
CREATE TABLE animals_young 
(   
    Name VARCHAR(20), 
    Birthday DATE,
    Age_in_months INT
);

INSERT INTO animals_young 
WITH animals_list (Name, Birthday) as
(
	SELECT Name, Birthday
	FROM cats
	UNION
	SELECT Name, Birthday
	FROM dogs
	UNION
	SELECT Name, Birthday
	FROM hamsters
	UNION
	SELECT Name, Birthday
	FROM horses
	UNION
	SELECT Name, Birthday
	FROM camels
	UNION
	SELECT Name, Birthday
	FROM donkeys
)
SELECT Name, Birthday, TIMESTAMPDIFF(MONTH, Birthday, NOW()) 
FROM animals_list
WHERE TIMESTAMPDIFF(MONTH, Birthday, NOW()) BETWEEN 12 AND 36;
```
Результат:
```
+--------+------------+--------------+
| Name   | Birthday   | Age_in_month |
+--------+------------+--------------+
| Maui   | 2022-01-09 |           30 |
| Loki   | 2021-11-02 |           32 |
| Max    | 2022-10-21 |           20 |
| Bonnie | 2023-03-11 |           15 |
+--------+------------+--------------+
```
12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам.

Вывод команд:
```
SELECT a3.name Class, a2.name Animal, a1.name Name,Birthday, Commands 
FROM
(
	SELECT id_pets, name, Birthday, Commands 
	FROM cats
	UNION
	SELECT id_pets, name, Birthday, Commands  
	FROM dogs
	UNION
	SELECT id_pets, name, Birthday, Commands  
	FROM hamsters
) a1
	INNER JOIN pets a2 ON a1.id_pets = a2.id
	INNER JOIN animals a3 ON a2.id_animals = a3.id
UNION
SELECT a3.name Class, a2.name Animal, a1.name Name,Birthday, Commands 
FROM
(
	SELECT id_pack_animals, name, Birthday, Commands 
	FROM horses
	UNION
	SELECT id_pack_animals, name, Birthday, Commands
	FROM camels
	UNION
	SELECT id_pack_animals, name, Birthday, Commands
	FROM donkeys
) a1
	INNER JOIN pack_animals a2 ON a1.id_pack_animals = a2.id
	INNER JOIN animals a3 ON a2.id_animals = a3.id;
```

Результат:
```
+--------------+----------+---------+------------+-------------------------+
| Class        | Animal   | Name    | Birthday   | Commands                |
+--------------+----------+---------+------------+-------------------------+
| Pets         | Hamsters | Buster  | 2023-12-31 | Roll                    |
| Pets         | Hamsters | Otto    | 2024-02-02 | Roll                    |
| Pets         | Hamsters | Peanut  | 2024-01-30 | Play dead               |
| Pets         | Dogs     | Max     | 2022-10-21 | Paw                     |
| Pets         | Dogs     | Bonnie  | 2023-03-11 | Sit                  |
| Pets         | Dogs     | Barney  | 2021-02-12 | Paw                     |
| Pets         | Cats     | Zeus    | 2019-07-15 | Meow, Sit, Jump         |
| Pets         | Cats     | Maui    | 2022-01-09 | Meow                    |
| Pets         | Cats     | Loki    | 2021-11-02 | Scratch                 |
| Pack Animals | Donkeys  | Nacho   | 2017-10-02 | Walk, Stay, Carry Load  |
| Pack Animals | Donkeys  | Olaf    | 2016-01-01 | Walk, Stay, Carry Load  |
| Pack Animals | Donkeys  | Archie  | 2024-03-08 | Walk, Carry Load        |
| Pack Animals | Horses   | Orion   | 2014-09-11 | Gallop, Paw             |
| Pack Animals | Horses   | Mango   | 2012-06-21 | Gallop                  |
| Pack Animals | Horses   | Zeus    | 2020-05-03 | Kick                    |
+--------------+----------+---------+------------+-------------------------+
```

13. Создать класс с Инкапсуляцией методов и наследованием по диаграмме.

14. Написать программу, имитирующую работу реестра домашних животных.
В программе должен быть реализован следующий функционал:

    14.1. Завести новое животное

    14.2. определять животное в правильный класс

    14.3. увидеть список команд, которое выполняет животное

    14.4. обучить животное новым командам

    14.5. Реализовать навигацию по меню

15. Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆
значение внутренней̆int переменной̆на 1 при нажатие “Завести новое
животное” Сделайте так, чтобы с объектом такого типа можно было работать в
блоке try-with-resources. Нужно бросить исключение, если работа с объектом
типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение
считать в ресурсе try, если при заведения животного заполнены все поля.