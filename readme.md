Прокси-сервер перехвата коммитов в хранилище 1с
=============================================

![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/burevol/repository_proxy)
![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/burevol/repository_proxy)
![GitHub last commit](https://img.shields.io/github/last-commit/burevol/repository_proxy)

Описание
---------------
Предназначен для перехвата обращений в хранилище конфигураций 1c. При помещении кода в хранилище запускается задача Jenkins.

Как запустить
---------------------

Для быстрого тестирования:
```
docker run -p 1542:1542 -e REPOSITORY_ADDR=<Адрес хранилища> -e JENKINS_ID=<ID пользователя> -e JENKINS_TOKEN=<Токен пользователя> -e JENKINS_ADDR=<Адрес сервера Jenkins> -e JENKINS_JOB=<Наименование задачи Jenkins> -e JENKINS_PROTOCOL=<http или https> burevol/repository_proxy:latest
```
Для развертывания в продакшене:
* создать файл .env с содержимым:
```
REPO=    #IP адрес хранилища 1с
ID=          #ID пользователя Jenkins
TOKEN=    #Токен пользователя Jenkins
ADDR=      #адрес сервера Jenkins, в формате ip:порт
JOB=          #Имя задачи
PROTOCOL=        #Протокол подключения к серверу Jenkins, http или https
```
* создать файл docker-compose.yml с содержимым:
```
version: "2.2" 
services:
  repository-proxy:
    build: .
    image: burevol/repository_proxy:latest
    environment:
      - REPOSITORY_ADDR=$REPO
      - JENKINS_ID=$ID
      - JENKINS_TOKEN=$TOKEN
      - JENKINS_ADDR=$ADDR
      - JENKINS_JOB=$JOB 
      - JENKINS_PROTOCOL=$PROTOCOL
    restart: unless-stopped
    ports:
      - "1542:1542"
    container_name: repository_proxy
```

* выполнить команду
```
docker-compose up -d
```
Примечания
-------------
Задача Jenkins получает имя хранилища в параметре extension_name

В разработке использована модифицированная версия [mitm_relay](https://github.com/jrmdev/mitm_relay)




