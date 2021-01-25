#Сервис запуска выгрузки хранилища 1с при помещении в него доработок.

##Введение

##Установка

```
docker run -p 1542:1542 -e REPOSITORY_ADDR=<Адрес хранилища> -e JENKINS_ID=<ID пользователя> -e JENKINS_TOKEN=<Токен пользователя> -e JENKINS_ADDR=<Адрес сервера Jenkins> -e JENKINS_JOB=<Наименование задачи Jenkins> -e JENKINS_PROTOCOL=<http или https> repository_proxy:latest
```

```
version: "3.9"
services:
  repository-proxy:
    build: .
    environment:
      - REPOSITORY_ADDR=192.168.0.1 #IP адрес хранилища конфигураций
      - JENKINS_ID=user  #ID пользователя Jenkins
      - JENKINS_TOKEN=     #Токен пользователя Jenkins
      - JENKINS_ADDR=192.168.0.2:8080  #IPадрес:Порт сервера Jenkins
      - JENKINS_JOB=sync  #Имя задачи Jenkins
      - JENKINS_PROTOCOL=http #Протокол, http или https
    ports:
      - "1542:1542"
```




