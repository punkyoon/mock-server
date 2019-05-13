from fastapi import FastAPI


mock = FastAPI()

@mock.get('/')
def index():
    return {'message': 'Welcome!'}


@mock.get('/users')
def list_user():
    return {'users': []}


@mock.get('/users/{user_id}')
def get_user(user_id: str):
    return {'user': None}
