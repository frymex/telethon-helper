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


async def async_connect():
    auth = init.asyncClient(api_id=api_id, api_hash=api_hash, phone=phone)
    my_client = await auth.safety_connect()
    return my_client


client = without_2fa()

client.send_message('cazqev', 'Привет! Я подключился')
