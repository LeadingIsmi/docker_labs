# Docker для компиляции и работы с кирпичным языком

## Команды для сборки и запуска образов

1. **Сборка и запуск образов для компиляции и работы с кирпичным языком**
    ```bash
    docker build . -f DockerfileBuild -t bricklanguagebuild
    docker run --rm -v ./binary_app:/binary_app bricklanguagebuild
    docker rmi bricklanguagebuild

    echo 'FROM scratch' | docker build . -f - -t bricklanguagerun 
    docker run --rm -v ./binary_app:/binary_app -v ./tmp:/tmp --entrypoint /binary_app/brick_language bricklanguagerun
    docker run --rm -v ./binary_app:/binary_app -v ./tmp:/tmp --entrypoint /binary_app/brick_language bricklanguagerun "панама на голову"
    docker rmi bricklanguagerun
    ```

## 1) Работа с Volumes и билдом

### Шаги:

1. **Сборка Docker-образа для компиляции Python приложения**

    Сначала создайте Docker образ для компиляции приложения с помощью Dockerfile:

    ```bash
    docker build . -f DockerfileBuild -t bricklanguagebuild
    ```

2. **Запуск контейнера с монтированием volume**

    Используем флаг `--rm`, чтобы контейнер удалился автоматически после завершения работы. Подключаем volume для папки `binary_app`, чтобы сохранить скомпилированный бинарник:

    ```bash
    docker run --rm -v ./binary_app:/binary_app bricklanguagebuild
    ```

    Этот шаг компилирует и сохраняет скомпилированный файл в папке `binary_app`.

3. **Удаление образа после выполнения**

    После завершения работы удалите образ:

    ```bash
    docker rmi bricklanguagebuild
    ```

## 2) Работа с Scratch

### Шаги:

1. **Сборка Docker-образа для запуска приложения**

    Создайте Docker образ для работы с минимальным образом `scratch`. Дабы не плодить Dockerfile, просто передаем строку "FROM scratch" как входной файл в "-f -" в docker build. Это будет пустой образ 'scratch':

    ```bash
    echo 'FROM scratch' | docker build . -f - -t bricklanguagerun 
    ```

2. **Запуск контейнера с программой**

    С помощью флага `--rm` автоматически удаляйте контейнер после его завершения. Пример запуска программы с различными параметрами:

    ```bash
    docker run --rm -v ./binary_app:/binary_app -v /tmp:/tmp --entrypoint /binary_app/brick_language bricklanguagerun
    docker run --rm -v ./binary_app:/binary_app -v /tmp:/tmp --entrypoint /binary_app/brick_language bricklanguagerun "панама на голову"
    ```

3. **Удаление образа после работы**

    После завершения работы программы не забудьте удалить образ:

    ```bash
    docker rmi bricklanguagerun
    ```

## Примечания:

- `--rm`: флаг для удаления контейнера после его завершения.
- `-v <host-path>:<container-path>`: флаг для монтирования volume из хостовой системы в контейнер.
- `scratch`: это пустой базовый образ, который используется для создания минимальных образов с только необходимыми файлами.

### Примечание о производительности:

Приложение использует минимальные ресурсы после сборки и компиляции, поскольку финальный образ содержит только бинарный файл без лишних зависимостей и инструментов для компиляции.
