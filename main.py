import subprocess
from typing import Optional
import json
from fastapi import FastAPI, BackgroundTasks
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/human-summary/{username}")
async def send_notification(username: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(save_json, username)
    return {"message": "Running slither in the background"}


def save_json(username: str):
    result = subprocess.run(['slither', '.', '--print', 'human-summary', '--json', '-'], stdout=subprocess.PIPE)
    
    if result.returncode != 0:
        logger.error(result.stderr)
    else:
        data = json.loads(result.stdout)
        if not data['success']:
            logger.error(data['error'])
        else:
            with open(f"data/{username}.json", "w", encoding="utf-8") as f:
                json.dump(data['results']['printers'][0], f)

            logger.debug("data saved successfully")

    

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
