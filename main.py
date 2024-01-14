from fastapi import FastAPI

app = FastAPI()




# home route
@app.get("/")
def root():
    return {"message": "OK"}