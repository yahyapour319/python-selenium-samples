from web_driver import get_web_driver
from selenium.webdriver.support.ui import WebDriverWait



driver = get_web_driver()

driver.execute_script(
    """
        window.url_fragment_identifier =[];
        window.addEventListener('hashchange', function() {
                 window.url_fragment_identifier.push(location.hash);
                 console.log(window.url_fragment_identifier);
        }, false);
                                    
    """
)

# check specific url fragment 
wait = WebDriverWait(driver, 60)    
def execute_js_script(web_driver):
    return  driver.execute_script("return window.url_fragment_identifier;")==["#/usb/find"])

wait.until(execute_js_script)

# or check if specific url fragment is in return list
assert "#/usb/find" not in web_driver.execute_script("return window.url_fragment_identifier;")


