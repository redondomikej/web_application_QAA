from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver(browser="chrome", incognito=False, headless=False, additional_args=None):
    """
    Returns a WebDriver instance based on the specified browser.
    
    :param browser: Browser type ("chrome", "firefox", "edge").
    :param incognito: Enable incognito mode.
    :param headless: Run browser in headless mode.
    :param additional_args: List of additional arguments.
    :return: WebDriver instance.
    """
    
    additional_args = additional_args or []  # Default to an empty list if no extra args

    if browser.lower() == "chrome":
        options = ChromeOptions()
        if incognito:
            options.add_argument("--incognito")
        if headless:
            options.add_argument("--headless=new")  # Headless mode (Chrome 109+)
        options.add_argument("--start-maximized")

        for arg in additional_args:
            options.add_argument(arg)

        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        if incognito:
            options.add_argument("-private")
        if headless:
            options.add_argument("--headless")

        for arg in additional_args:
            options.add_argument(arg)

        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    elif browser.lower() == "edge":
        options = EdgeOptions()
        if incognito:
            options.add_argument("--inprivate")
        if headless:
            options.add_argument("--headless")

        for arg in additional_args:
            options.add_argument(arg)

        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")
