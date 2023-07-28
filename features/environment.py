from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app1.application import Application
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def browser_init(context):
    """
    :param context: Behave context
     """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # Allure command:
    # python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/amazon_sign_in.feature

    ## Crossbrowser:

    # context.driver = webdriver.Firefox()

    ## Mobile Emulator:

    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    ## Headless Browser:
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service)

    #### BROWSERSTACK ####

    # options = FirefoxOptions()
    # bs_user = 'mounikajothi_O89pfG'
    # bs_key = '4uSCyMyVv3Bu2kSjjqmA'

    # # Setting the capabilities
    # caps = {
    #     "os": "OS X",
    #     "osVersion": "Catalina",
    #     # "sessionName": context.scenario.name
    # }
    #
    # options.set_capability('bstack:options', caps)
    # options.set_capability('browserVersion', '95')
    # options.set_capability('browserName', 'Firefox')

    # connecting the test to Browserstack
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(
    #     command_executor=url,
    #     options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 5)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
    # context.driver.execute_script(
    #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Validation  passed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
