# Rap-Paraphraser backend
Бекенд сервиса для перефразирования текста любого типа (в том числе и одного слова) в семантическом поле русского репа с добавлением реп-сленга

Автор основного кода - Никита Северин ([Nikis14](https://github.com/Nikis14))

Представляет собой веб-сервер на Python, принимающий 2 типа запросов:
* `GET /associate?word=<word>` - найти близкие слова в `<word>` в семантическом поле русского репа
* `POST /rephrase?` с параметром `text=<text>` - перефразировать `<text>` в семантическом поле русского репа

Зависимости:
```
gensim==3.7.2
pymorphy2==0.8
pymorphy2-dicts==2.4.393442.3710985
```

## Демо
Бекенд сервиса развернут на Heroku по адресу https://rap-paraphraser-backend.herokuapp.com/

Фронтенд сервиса расположен в отдельном [репозитории](https://github.com/nikitaodnorob/rap-paraphraser), который развернут на Heroku по адресу https://rap-paraphraser.herokuapp.com/

## Пример работы

#### Отрывок из "Мастер и Маргарита"

_**Оригинал**_

Никогда не разговаривайте с неизвестными. Однажды весною, в час небывало жаркого заката, в Москве, 
на Патриарших прудах, появились два гражданина.

_**Результат**_

Никогда не **заведёмтесь** с неизвестными. Однажды весною, в **да-да-да-да-да-да-да-да-д кокаииииинннннного** жаркого **рассвета**, в **столице**, 
на Патриарших **вхламах**, появились два **артефакта**.
