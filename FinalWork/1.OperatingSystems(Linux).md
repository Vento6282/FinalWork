# Операционные системы и виртуализация (Linux)

### Выполнение заданий:

1. Вывод команд:
```
student@Ubuntu:~$ nano Pets.txt
student@Ubuntu:~$ nano PackAnimals.txt
student@Ubuntu:~$ cat PackAnimals.txt Pets.txt > HumanFriends.txt
student@Ubuntu:~$ ls
Desktop  Documents  Downloads  HumanFriends.txt  Music  PackAnimals.txt  Pets.txt  Pictures  Public  snap  Templates  Videos
```
2. Вывод команд:
```
student@Ubuntu:~$ mkdir Animals
student@Ubuntu:~$ mv HumanFriends.txt Animals/
student@Ubuntu:~$ ls Animals/
HumanFriends.txt
```
3. Вывод команд:
```
student@Ubuntu:~$ sudo apt-get install mysql-server -y
```
4. Вывод команд:
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
5. Вывод команд:
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
