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


@app.get("/data/{filename}/json")
def view_data(filename: str):
    with open(f'data/{filename}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data 

def save_json(filename: str):
    result = subprocess.run(['slither', '.', '--print', 'human-summary', '--json', f'data/{filename}.json'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)


# breakpoint()
