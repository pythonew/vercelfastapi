from fastapi import FastAPI

app = FastAPI()

@app.get("/example/{parameter}")
def example(parameter: str):
    data = {'Nagad-01874706405':'agant2'}
    agant = data[parameter]
    return {
        "bankcode": parameter,
        "agant": agant
    }

@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }
