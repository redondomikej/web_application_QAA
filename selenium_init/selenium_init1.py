import os
import subprocess

# Define project structure
directories = [
    ".venv",
    "config",
    "features",
    "features/steps",
    "features/pages",
    "reports",
    "test_evidence/screenshots",
    "test_evidence/videos",
    "utils"
]

# Files and their default content
files = {
    "config/config.json": """{
    "browser": "chrome",
    "base_url": "https://example.com"
}""",
    
    "features/environment.py": """from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()
    
def after_all(context):
    context.browser.quit()""",

    "features/example.feature": """Feature: Example Feature
  Scenario: Open website
    Given I open the browser
    When I enter the username "testuser"
    And I enter the password "testpass"
    And I click the login button
    Then I should see the success message "Logged In Successfully"
""",

    "features/steps/example_steps.py": """from behave import given, when, then

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
""",

    "features/pages/example_page.py": """class ExamplePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
""",

    "utils/webdriver_manager.py": """from selenium import webdriver

def get_driver():
    return webdriver.Chrome()
""",

    "utils/test_data.py": """TEST_USER = {
    "username": "testuser",
    "password": "testpass"
}""",

    "requirements.txt": """selenium
behave
webdriver-manager
""",

    "behave.ini": """[behave]
default_format = pretty
show_skipped = false
logging_level = INFO
""",

    ".gitignore": """.venv/
reports/
test_evidence/
__pycache__/
*.pyc
"""
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files with content
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

# Set up virtual environment
print("📌 Setting up virtual environment (.venv)...")
subprocess.run(["python", "-m", "venv", ".venv"], check=True)

print("✅ Selenium + Behave project initialized successfully! 🎯")
print("👉 Next steps:")
print("1️⃣ Activate the virtual environment:")
print("   - Windows: `.venv\\Scripts\\activate`")
print("   - Mac/Linux: `source .venv/bin/activate`")
print("2️⃣ Install dependencies: `pip install -r requirements.txt`")
print("3️⃣ Run tests: `behave`")
