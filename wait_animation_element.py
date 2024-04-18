# '''
#   Waiting on a js animation to complete in python selenium
#   - First defined a window.variable at js files and valued it with one of your business logic state.  example : ["opening","opend","closing", "closed"]
#   - Second : At the backend side, wait on that varibale
# '''
#
# from selenium.webdriver.support import expected_conditions as EC
# from web_driver import get_web_driver
#
#
# def wait_for_element(state):
#     driver= get_web_driver()
#     wait = WebDriverWait(driver, timeout=10)
#     wait.until(lambda driver: driver.execute_script("return window.keyboardStatus") == state)
#
#
# wait_for_element(state="opened")
# wait_for_element(state="closed")
#
#
#
#
#
