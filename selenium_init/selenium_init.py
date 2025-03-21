import os
import json

# Define the project structure
directories = [
    ".venv",  # Virtual environment
    "features",
    "features/steps",
    "features/pages",
    "config",
    "reports",
    "utils"
]

# Create directories if they don't exist
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create config.json with default settings
config_data = {
    "browser": "chrome",
    "base_url": "https://example.com",
    "headless": False
}
with open("config/config.json", "w") as f:
    json.dump(config_data, f, indent=4)

# Create behave.ini
behave_ini_content = """\
[behave]
default_format = pretty
show_skipped = false
logging_level = INFO
"""
with open("behave.ini", "w") as f:
    f.write(behave_ini_content)

# Create example.feature file
feature_content = """\
Feature: Example Feature
  Scenario: Open website
    Given I open the browser
    When I enter the username "testuser"
    And I enter the password "testpass"
    And I click the login button
    Then I should see the success message "Logged In Successfully"
"""
with open("features/example.feature", "w") as f:
    f.write(feature_content)

# Create environment.py
open("features/environment.py", "w").close()

# Create example_steps.py file
steps_content = """\
from behave import given, when, then

@given("I open the browser")
def open_browser(context):
    print("Opening browser")

@when('I enter the username "{username}"')
def enter_username(context, username):
    print(f"Entering username: {username}")

@when('I enter the password "{password}"')
def enter_password(context, password):
    print(f"Entering password: {password}")

@when("I click the login button")
def click_login(context):
    print("Clicking login button")

@then('I should see the success message "{message}"')
def check_success_message(context, message):
    print(f"Expected message: {message}")
"""
with open("features/steps/example_steps.py", "w") as f:
    f.write(steps_content)

# Create example_page.py (Page Object Model)
page_content = """\
class ExamplePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        print(f"Entering username: {username}")

    def enter_password(self, password):
        print(f"Entering password: {password}")

    def click_login(self):
        print("Clicking login button")
"""
with open("features/pages/example_page.py", "w") as f:
    f.write(page_content)

# Create utility files
utils_files = {
    "utils/webdriver_manager.py": "def setup_driver():\n    print('Setting up WebDriver')\n",
    "utils/test_data.py": "TEST_USER = {'username': 'testuser', 'password': 'testpass'}\n",
    "utils/reporter.py": "def generate_report():\n    print('Generating test report')\n",
    "utils/screenshot.py": "def capture_screenshot():\n    print('Capturing screenshot')\n",
    "utils/video_recorder.py": "def start_recording():\n    print('Starting video recording')\n"
}

for filepath, content in utils_files.items():
    with open(filepath, "w") as f:
        f.write(content)

# Create report placeholder files
open("reports/results.csv", "w").close()
open("reports/results.html", "w").close()

# Create .gitignore
gitignore_content = """\
.venv/
__pycache__/
*.log
*.png
*.mp4
"""
with open(".gitignore", "w") as f:
    f.write(gitignore_content)
import os

# Define the README content
readme_content = """ 

# 🚀 Selenium + Behave Automation Framework

## 📌 Project Overview  
This project is a **Selenium + Behave automation framework** for UI testing.  
It follows **Behavior-Driven Development (BDD)** using **Gherkin syntax** and generates reports using **Allure**.  

---

## ⚙️ Features  
✅ **BDD with Behave & Gherkin** – Easily write human-readable test cases  
✅ **Selenium WebDriver** – Automate browser interactions  
✅ **Page Object Model (POM)** – Maintain clean and reusable code  
✅ **Allure Reporting** – Generate detailed test reports  
✅ **Headless Mode Support** – Run tests faster without a UI  

---

## 🔧 Setup  
1️⃣ **Create and activate a virtual environment**  
```sh
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows
2️⃣ Install dependencies 
pip install -r requirements.txt
```
---

## 🚀 Running Tests
**behave**
```behave features/example.feature```
**Run tests with Allure reporting:**
```behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results```
**Generate the Allure report:**
```allure serve reports/allure-results```

---

## 📊 Test Reports
Allure Reports – reports/allure-results/
HTML Reports – reports/results.html
CSV Reports – reports/results.csv

---

## 👨‍💻 Author
📌 Mike EJ Redondo
📧 your.email@example.com
🔗 LinkedIn/GitHub (if applicable)"""
# Write README.md file
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
