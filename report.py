from files import create_folder_if_not_exist
import subprocess
from logging import getLogger, StreamHandler, DEBUG
import json


logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


FILENAME = 'results.sarif'

def security_check(username):
    data = run_slither()
    if data:
        save_data(data, username)


def run_slither():
    result = subprocess.run(
        ['slither', '.','--json', '-', '--sarif', FILENAME], stdout=subprocess.PIPE)
        # ['slither', '.', '--print', 'human-summary', '--json', '-'], stdout=subprocess.PIPE)

    if result.returncode != 0:
        logger.error(result.stderr)
    else:
        data = json.loads(result.stdout)
        return data


def save_data(data, filename: str):

    if not data['success']:
        logger.error(data['error'])
    else:
        create_folder_if_not_exist(".", "data")
        with open(f"data/{filename}", "w", encoding="utf-8") as f:
            json.dump(data['results']['printers'][0], f)

        logger.debug("data saved successfully")

data = run_slither()
save_data(data, FILENAME)
