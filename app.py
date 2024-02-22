from utils.funcs import wiki_summary
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()

class wiki_search(BaseModel):
    page_name: str



@app.get("/")
async def root():
    return {"message": {"Hello Model"}}

@app.post("/get-info")
async def get_info(search_query : wiki_search):
    result = wiki_summary(name = search_query.page_name)
    payload = {"wikipage" : result}
    json_compatible_data = jsonable_encoder(payload)
    return JSONResponse(content = json_compatible_data)

