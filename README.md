# Проект "ГЕРМЕС"
*Доброго времени суток, коллеги.*
Данное решение представлено в рамках решения кейса *"ИИ проводит таможенный контроль"*, и представляет собой веб-приложение на Django (DRF) + Vue.js.

#### :exclamation: Важно! Поскольку мы не обладаем высокими вычислительными мощностями, для обучения моделей взяли первые 100 тысяч записей из таблицы пользовательского ввода! (Покрывает 1-25 группы)

*Для работы с полной базой, перенесите файл с базой в директорию backend/filter/data, заменив ввод данных в конфиге приложения на* `encoding = 'ANSI', sep = ';'` *либо сохранив в текстовом предствалениис кодировкой Unicode*

## Backend + Machine Learning

В директории backend находится django-приложение, с загруженными данными (`/backend/filter/data`).
Если хотите протестировать на других выборках - сохраните excel-файл в формате текста, юникод (В докере под ubuntu 20.04 не читается кодировкой ansi, mbcs.)
Если хотите запустить backend ручками - нужно изменить пути для файлов и модели .joblib, установить окружение

`python -m venv venv`
`venv\Scripts\activate`
`pip install -r requirements.txt`

Во всех остальных случаях - используйте Docker, либо docker-compose.
Мы использовали следующий подход: preprocessing(tokenization, lemmatization, stemming) - tfidf_Vectorizer - LogisticRegression - train\prediction

В приложении filter находятся векторизаторы, забирающие данные из *csv*, либо из *txt* если вы запускаете через Docker.
Один из векторизаторов преобразует эталонную базу, другой базу пользовательского ввода. 

В конфиге приложения описаны функции для предсказания на основе близости N-мерных векторов. Через APIview поставляется query для определения близости векторов результат возвращается в конечных ТН ВЭД кодах и опианиям к ним, в формате json.

В приложении classificator - пайплайн векторизаторов и логистической регрессии. Отличие этого метода в выводе пользователю вероятностной оценки по каждому разделу и группе (первые две пары чисел)

В приложении main объединены эти два подхода - пользователю выдаются рекомендации по наиболее вероятным группам, которые определяет векторизатор.

## Vue
Frontend запускается командами:

`cd frontend`
`npm install`
`npm run serve`

Vue служит только для визуализации, обработки данных внутри Vue не происходит.
На страничке **"Классификация кода ТН ВЭД"** отображаются 3 таблицы и график.

1. Таблица **"Метод вероятностной оценки"** определяет принадлежность к классу кода (первые две пары чисел), с определенной вероятностью. При этом используем API из приложения classificator.

2. Таблица **"Метод векторизации"** определяет близость векторов из базы пользовательского ввода, и выдает все рекомендации по определенным моделью раздел-группам (первые две пары чисел) в соотсветсвии с эталонной базой. То есть он выводит конкретные ТН ВЭД по самым близким группам

3. Таблица **"Комплексный метод"** учитывает как близость векторов, так и вероятностную оценку. Если пользователь вводит слишком расплывчатый текст, то метож не работает, однако если пользователь конкретизирует запрос, он выводит в уменьшенном объеме все рекомендации по найденным группам.

4. График **"Интерактивная документация в виде дерева"** ещё в разработке - он выводит все возможные группы и подгруппы, в дальнейшем будет выводить только те подгруппы которые определила модель. Для этой реализации потребуются данные по каждой подгруппе и вложениях внутри нее. Так можно будет 1) повысить точность, поскольку граф нагляднее таблицы 2) уменьшить ошибки по определению смежных подгрупп одной группы.

## Docker

Проект запускается 1 командой

`docker-compose up -d`

Либо по отдельности через Dockerfile внутри папок приложений.

## Jupiter

В директории notes находятся наши ноутбуки, если интересно - можете посмотреть, но весь функционал ML перенесен в django.
