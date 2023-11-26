from fastapi import FastAPI

app = FastAPI()

@app.get("/") # www.somewebsite.com/
async def root():
    return {"message" : "Wellcome to Our Website"}