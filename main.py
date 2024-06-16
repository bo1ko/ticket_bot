from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from automation.login_automation import LoginAutomation
from automation.navigate_automation import NavigateAutomation
from ticket_finder.ticket_finder import Ticket

from fake_useragent import UserAgent

from config.config import proxy, proxy_login, proxy_password


def main():
    SITE_URL = 'https://eq.hsc.gov.ua/site/index'
    PROFILE_URL = 'https://eq.hsc.gov.ua/step0'

    options = Options()
    options.add_argument(f'user-agent={UserAgent().random}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument("--disable-proxy-certificate-handler")

    proxy_options = {
        'proxy': {
            'http': f'http://{proxy_login}:{proxy_password}@{proxy}',
            'https': f'https://{proxy_login}:{proxy_password}@{proxy}'
        },
    }

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(SITE_URL)
    wait = WebDriverWait(driver, 10)

    try:
        if driver.current_url == SITE_URL:
            LoginAutomation(driver, wait).login('Boyko2004')
        
        if driver.current_url == PROFILE_URL:
            NavigateAutomation(driver, wait).navigate(18)
        
        Ticket(driver, wait).get_ticket(9, 22, first_date=18)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
