import csv
from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

TEST_DATA_PATH = "utils/test_data.csv"  # Update path as needed

@given('I open the browser')
def step_open_browser(context):
    context.driver.get("https://practicetestautomation.com/practice-test-login/")
    context.driver.maximize_window()
    sleep(2)

@when('I enter login credentials from "{csv_file}"')
def step_enter_credentials(context, csv_file):
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        context.test_cases = list(reader)  # Store all test cases

    # Run the first test case
    test_case = context.test_cases[0]
    username_input = context.driver.find_element(By.ID, "username")
    password_input = context.driver.find_element(By.ID, "password")

    username_input.clear()
    username_input.send_keys(test_case["username"])

    password_input.clear()
    password_input.send_keys(test_case["password"])

    login_button = context.driver.find_element(By.ID, "submit")
    login_button.click()
    sleep(2)

@then('I should see the correct success message')
def step_verify_message(context):
    expected_message = context.test_cases[0]["message"]
    success_message = context.driver.find_element(By.XPATH, "//h1")
    assert success_message.text == expected_message, f"Expected '{expected_message}' but got '{success_message.text}'"
