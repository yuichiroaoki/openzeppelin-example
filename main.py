from report import security_check
from typing import Optional
import json
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/human-summary/{username}")
async def send_notification(username: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(security_check, username)
    return {"message": "Running slither in the background"}


@app.get("/data/{username}/json")
def view_data(username: str, description: Optional[bool] = False, other: Optional[str] = None):
    with open(f'data/{username}.json', 'r', encoding='utf-8') as f:
        printers = json.load(f)
        if description:
            return printers['description']
        if other:
            return printers['additional_fields'][other]
        return printers 
