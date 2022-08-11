from platform import system
from asyncio import WindowsSelectorEventLoopPolicy, run, set_event_loop_policy

from telethon.errors import SessionPasswordNeededError, FloodWaitError, PasswordHashInvalidError, \
    AuthKeyUnregisteredError

from telethon.sync import TelegramClient

from telethon import TelegramClient as asyncTelegramClient


class Client:
    def __init__(self, api_id: int, api_hash: str, phone: str, **kwargs):
        self.values: dict = {
            'api_id': api_id,
            'api_hash': api_hash,
            'phone': phone
        }
        self.client = TelegramClient(f'src/{phone}', api_id, api_hash,
                                     **kwargs)
        self.client.connect()

    def login(self, password: str):
        client = self.client
        phone = self.values.get('phone')

        try:
            client.send_code_request(phone, force_sms=False)
        except FloodWaitError as err:
            hours = round(int(err.seconds) / 100 / 60)
            exit(f'Вам нужно подождать {hours} часов | Лимиты телеграм [{err.message} | {err.code}]')

        value = input("Enter login code: ")

        try:
            me = client.sign_in(phone, code=value)
        except SessionPasswordNeededError as err:
            try:
                me = client.sign_in(password=password)
            except PasswordHashInvalidError as ex:
                return 'Wrong password'

    @property
    def my_client(self) -> TelegramClient:
        return self.client

    def safety_connect(self, password=None) -> TelegramClient:
        try:
            x = self.client.get_me()
            if not x:
                self.login(
                    password
                )
                return self.client

            return self.client
        except AuthKeyUnregisteredError:
            self.login(
                password
            )
            return self.client


class asyncClient:
    def __init__(self, api_id: int, api_hash: str, phone: str, **kwargs):
        self.values: dict = {
            'api_id': api_id,
            'api_hash': api_hash,
            'phone': phone
        }
        self.client = asyncTelegramClient(f'src/{phone}', api_id, api_hash,**kwargs)

        self.client.connect()

    async def login(self, password: str):
        client = self.client
        phone = self.values.get('phone')

        try:
            await client.send_code_request(phone, force_sms=False)
        except FloodWaitError as err:
            hours = round(int(err.seconds) / 100 / 60)
            exit(f'Вам нужно подождать {hours} часов | Лимиты телеграм [{err.message} | {err.code}]')

        value = input("Enter login code: ")

        try:
            me = await client.sign_in(phone, code=value)
        except SessionPasswordNeededError as err:
            try:
                me = await client.sign_in(password=password)
            except PasswordHashInvalidError as ex:
                return 'Wrong password'

    @property
    def my_client(self) -> asyncTelegramClient:
        return self.client

    async def safety_connect(self, password=None) -> asyncTelegramClient:
        try:
            x = self.client.get_me()
            if not x:
                await self.login(
                    password
                )
                return self.client

            return self.client
        except AuthKeyUnregisteredError:
            await self.login(
                password
            )
            return self.client
