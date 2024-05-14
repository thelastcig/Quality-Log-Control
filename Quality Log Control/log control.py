from flask import Flask, request, render_template
import logging
import json
from datetime import datetime
import random

app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)


def simulate_api(api_name):
    levels = ['info', 'error', 'success']
    log_strings = ['Received request', 'Failed to connect', 'Query executed successfully']
    
    level = random.choice(levels)
    log_string = random.choice(log_strings)
    
    log_event(api_name, level, log_string)

def log_event(api_name, level, log_string):
    # Create log entry
    log_entry = {
        "level": level,
        "log_string": log_string,
        "timestamp": datetime.utcnow().isoformat(),
        "metadata": {
            "source": f"{api_name}_log.log"
        }
    }
    
    log_file_path = f"{api_name}_log.log"
    with open(log_file_path, "a") as file:
        file.write(json.dumps(log_entry) + "\n")


for i in range(1, 10):
    api_name = f"api_{i}"
    for _ in range(10):  
        simulate_api(api_name)


def search_logs(level=None, log_string=None, timestamp=None, source=None):
    search_results = []
    
    for i in range(1, 10):
        log_file_path = f"api_{i}_log.log"
        try:
            with open(log_file_path, "r") as file:
                
                for line in file:
                    log_entry = json.loads(line)
                    if (not level or log_entry['level'] == level) and \
                       (not log_string or log_entry['log_string'] == log_string) and \
                       (not timestamp or log_entry['timestamp'] == timestamp) and \
                       (not source or log_entry['metadata']['source'] == source):
                        search_results.append(log_entry)
        except FileNotFoundError:
            pass
    return search_results


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        level = request.form.get('level')
        log_string = request.form.get('log_string')
        timestamp = request.form.get('timestamp')
        source = request.form.get('source')
        # Search logs based on filters
        search_results = search_logs(level, log_string, timestamp, source)
        return render_template('results.html', search_results=search_results)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
