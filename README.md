### Telethon Helper `[version 1.0]` — лучший способ использовать библеотеку Telethon

##### Пример использования

```python
from src import init

api_id = 0
api_hash = '<api hash>'
phone = '<phone>'


# use this if you don't have 2-step auth:
# client = init.Client(api_id=api_id, api_hash=api_hash, phone=phone).safety_connect()

# use second method if you have 2-step auth
# client = init.Client(api_id=api_id, api_hash=api_hash, phone=phone).safety_connect("password")

def with_2fa(password):
    auth = init.Client(api_id=api_id, api_hash=api_hash, phone=phone).safety_connect(password)
    return auth


def without_2fa():
    auth = init.Client(api_id=api_id, api_hash=api_hash, phone=phone).safety_connect()
    # or client = init.Client(api_id=api_id, api_hash=api_hash, phone=phone).my_client
    return auth


client = without_2fa()

client.send_message('cazqev', 'Привет! Я подключился')
```

##### Порядок установки

1. `git clone https://github.com/frymex/telethon-helper.git`
2. `cd telethon-helper`

##### Зависимости

| Модуль   | Windows                        | Ubuntu/Linux                    |
| -------- | ------------------------------ | ------------------------------- |
| telethon | `pip install Telethon==1.24.0` | `pip3 install Telethon==1.24.0` |

##### FaQ

Telethon Helper  создан для того что бы упростить и обезопасить работу с telethon, собой эта система представляет вспомогательное дополнение к оффициальной [библиотеке](https://telethonn.readthedocs.io/)

