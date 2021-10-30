from selenium import webdriver
from selenium.webdriver.chrome.options import Options

resolution = "fullscreen"
close_browser_after_test =  1


def get_remote_web_driver(remote_uri, chrome_options):
    driver = webdriver.Remote(remote_uri, options=chrome_options)
    return driver


def get_local_web_driver(driver_path, chrome_options):
    driver_path = Path(driver_path)
    if not driver_path.is_absolute():
        driver_path = Path(__file__).resolve().parent / driver_path
    driver = webdriver.Chrome(executable_path=str(driver_path), options=chrome_options)
    return driver

def get_web_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    if resolution == "fullscreen":
        chrome_options.add_argument("--start-fullscreen")
    elif isinstance(resolution, list) and len(resolution) == 2:
        width, height = resolution
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option(
            "mobileEmulation",
            dict(
                deviceMetrics=dict(width=int(width), height=int(height), touch=False),
            ),
        )
    else:
        raise ValueError("invalid `resolution` config")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--no-sandbox")
    if web_driver_uri.startswith("http://"):
        driver = get_remote_web_driver(web_driver_uri, chrome_options)
    else:
        driver = get_local_web_driver(web_driver_uri, chrome_options)
    # When an element is not found, driver implicitly waits for it
    # to become available. But we have explicit waits for elements
    # to become available as implemented in the :py:meth:`wait_for_element`
    # and so do not need implicit waiting.
    # It also slows down the invisibility checks.
    driver.implicitly_wait(0)
    yield driver
    if close_browser_after_test:
        driver.quit()
