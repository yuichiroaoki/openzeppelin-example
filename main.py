import subprocess
from typing import Optional
import json
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/human-summary/{filename}")
async def send_notification(filename: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(save_json, filename)
    return {"message": "Command sent in the background"}


def save_json(filename: str):
    result = subprocess.run(['slither', '.', '--print', 'human-summary', '--json', f'data/{filename}.json'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)

@app.get("/data/{filename}/json")
def view_data(filename: str, description: Optional[bool] = False, other: Optional[str] = None):
    with open(f'data/{filename}.json', 'r', encoding='utf-8') as f:
        raw_json_data = json.load(f)
        printers = raw_json_data['results']['printers'][0]
        if description:
            return printers['description']
        if other:
            return printers['additional_fields'][other]
        return printers 

# breakpoint()
