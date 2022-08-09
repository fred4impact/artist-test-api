from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from uuid import UUID  #uuid4
# from models import Customer, CustomerUpdate

app = FastAPI()

fakedb = []


class Artist(BaseModel):
    id: int
    artist_name: str
    record_sold: float
    year: Optional[str]



@app.get('/')
def root():
    return {"data": "New course front"}


@app.get("/artists")
def get_all_artist():
    return fakedb


@app.get("/artists/{id}")
def get_single_artist(id: int):
    artist = id - 1
    return fakedb(artist)    


@app.post("/artists")
def create_single_artist(artist: Artist):
   fakedb.append(artist.dict())
   return fakedb[- 1] 


@app.delete("/artists/{id}")
def delete_single_artist(id: int):
   fakedb.pop(id-1)
   return {"Details": "artist was deleted successully" }    