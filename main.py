import subprocess
from typing import Optional
import json
from fastapi import FastAPI, BackgroundTasks
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI()

project_id = os.getenv('project_id')
service_account_path = os.getenv('service_account_path')

cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred, {
'projectId': project_id,
})

db = firestore.client()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/human-summary/{username}")
async def send_notification(username: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(save_json, username)
    return {"message": "Running slither in the background"}


def save_json(username: str):
    result = subprocess.run(['slither', '.', '--print', 'human-summary', '--json', '-'], stdout=subprocess.PIPE)
    output = json.loads(result.stdout)['results']['printers'][0]
    # output = result.stdout.decode('utf-8')
    doc_ref = db.collection(u'result').document(username)
    doc_ref.set(output)

# def format_data(output):
    

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
