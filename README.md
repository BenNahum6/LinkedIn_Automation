# LinkedIn Automation Project

## Overview
This project is an automation tool for LinkedIn, built using Selenium and pytest. The goal of this project is to automate various LinkedIn tasks, saving time and increasing efficiency.

## Features
Automated Connection Requests Approval:
Automatically scans pending connection requests on LinkedIn and accepts them to save manual effort.

## Extendable Automation Tasks:
Additional automation features can be added to streamline other LinkedIn tasks.

## Technology Stack
1. Python.
2. pytest for test management and execution.
3. Selenium for browser automation.


## Installation
1. Clone the repository
```bash
git clone <repository-url>  
cd linkedin-automation
```

2. Create a virtual environment (optional)
```bash
python -m venv venv  
source venv/bin/activate   # On Windows: venv\Scripts\activate  
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add necessary environment variables (such as LinkedIn login credentials, if needed). You can create a .env file with the following variables:
```bash
LINKEDIN_USERNAME=<your_username>  
LINKEDIN_PASSWORD=<your_password>
```

## How to Run the Automation
Run the pytest tests
```bash
pytest -v --log-cli-level=INFO
```
This command will execute all the automation tasks configured as pytest test cases.

## Project Structure
```bash
LinkedinAutomation/
│
├── .venv/              # Virtual environment directory
│   └── .env            # Environment configuration file
│
├── pages/              # Files representing different LinkedIn pages (Page Object Model)
│   ├── __init__.py     # Initialization file for the directory
│   ├── home_page.py    # Configuration for the home page
│   ├── login_page.py   # Configuration for the login page
│   ├── post_page.py    # Configuration for the posts page
│   └── requests_page.py # Configuration for the connection requests page
│
├── tests/              # Directory containing all the tests
│   ├── test_requests/  # Tests related to connection requests
│   │   ├── conftest.py             # Shared Pytest configuration
│   │   └── test_check_requests.py  # Tests for checking connection requests
│   ├── __init__.py     # Initialization file for the tests directory
│   └── conftest.py     # Additional Pytest configuration
│
├── utils/              # Utility functions and general project tools
│   ├── __init__.py     # Initialization file for the utilities directory
│   ├── config.py       # Configuration file for settings
│   ├── helpers.py      # General helper functions
│   └── logger.py       # Logger settings
│
├── test_logs.log       # Log file for test output
└── External Libraries  # External libraries (not a project file, but an IDE feature)
```

## Contribution
Feel free to contribute by submitting issues or pull requests to improve the automation features or add new ones!
  
