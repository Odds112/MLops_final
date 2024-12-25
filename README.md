# MLops_final

Этот проект демонстрирует классификацию изображений размером 32x32 с использованием CNN.

## Содержание

- [Описание](#описание)
- [Структура проекта](#структура-проекта)
- [Docker Hub](#Ссылка-на-DockerHub)


## Описание

Проект включает в себя полный цикл разработки модели машинного обучения с использованием современных практик MLOps, включая контейнеризацию с Docker и автоматизацию с Jenkins.

## Структура проекта

- `src/`: Исходный код проекта.
- `tests/`: Тесты для проверки корректности работы кода.
- `.gitignore`: Файл, определяющий файлы и папки, игнорируемые Git.
- `Dockerfile`: Скрипт для создания Docker-образа.
- `Jenkinsfile`: Скрипт для настройки пайплайна в Jenkins.
- `model.h5`: Сохраненная модель машинного обучения.
- `requirements.txt`: Список зависимостей Python.
- `test_image.png`: Тестовое изображение для проверки модели.

## Ссылка на DockerHub

https://hub.docker.com/repository/docker/odds112/mlops_final