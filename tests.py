import os
import logging
import sys

from pyvirtualdisplay import Display
from selenium import webdriver

logging.getLogger().setLevel(logging.INFO)


def set_display():
    display = Display(visible=0, size=(800, 600))
    display.start()
    return display


def get_driver_browser(browser):
    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('prefs', {
            'download.default_directory': os.getcwd(),
            'download.prompt_for_download': True,
        })
        logging.info('Prepared chrome options..')

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir', os.getcwd())
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
    logging.info('Prepared firefox profile..')
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver


def login_test(browser, url):
    display = set_display()
    driver = get_driver_browser(browser)
    driver.get(url)
    driver.find_element_by_id("id_username").send_keys('alejandro.betancourt@justo.mx')
    driver.find_element_by_id("id_password").send_keys('12323')
    driver.find_elements_by_class_name("btn-submit__login")[0].click()
    logging.info('Accessed %s ..', url)
    logging.info('Page title: %s', driver.title)
    logging.info('Page URL: %s', driver.current_url)
    assert driver.current_url == url.replace('account/login/', '')
    driver.quit()
    display.stop()


if __name__ == '__main__':
    args = sys.argv
    print(args)
    browser = args[1]
    url = args[2]
    login_test(browser, url)
