Log Control System with Query Interface
Description
This project implements a Log Control System with a Query Interface using Flask, Python's lightweight web framework. The system allows for logging events at different stages and provides a user interface for searching through the logs based on various criteria such as log level, log message, timestamp, and source.

Features
Log Ingestor: Captures logs from multiple APIs and stores them in separate log files.
Logging Configuration: Supports configuration of logging levels and file paths for each API.
Error Handling: Implements robust error handling to prevent disruptions in logging functionality.
Query Interface: Offers a user-friendly web interface for searching through logs.
Search Filters: Provides filters based on log level, log string, timestamp, and source.
Efficient Search: Aims for quick and efficient search results.
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/log-control-system.git
cd log-control-system
Install dependencies:

bash

pip install -r requirements.txt
Run the application:

bash
Copy code
python your_script.py
Access the application:

Open your web browser and go to http://localhost:5000 to access the Query Interface.

Usage
Home Page: Upon accessing the application, you'll see a search form where you can enter search queries and filters.
Search Results: After submitting the form, the search results will be displayed below the form.
