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
