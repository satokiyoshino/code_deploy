from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return { 'message': 'Hello World' }

@app.get('member')
def member():
    return { 'message': 'get MEMBER' }