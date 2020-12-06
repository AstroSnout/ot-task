import os
import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Scraper:

    def __init__(self, *args):
        self.driver = Scraper._get_chrome_driver(*args)

    def __del__(self):
        self.driver.close()

    @staticmethod
    def _get_chrome_driver(*args):
        print(args)
        options = Options()
        for arg in args:
            options.add_argument(arg)
        return webdriver.Chrome(
            options=options,
            executable_path=os.getcwd() + '\\chromedriver.exe'
        )

    def etherscan_historic_balance(self, address, date):
        year, month, day = date.split('-')
        url_to_scrape = 'https://etherscan.io/balancecheck-tool'
        self.driver.get(url_to_scrape)
        # Date first
        date_input = self.driver.find_element_by_id('date')
        date_input.click()
        date_input.send_keys(Keys.CONTROL, 'a')
        date_input.send_keys(f'{month}.{day}.{year}')
        # Address second -> clears focus from Date field, minimizing the calendar popup that obstructs the "Submit" btn
        address_input = self.driver.find_element_by_id('ContentPlaceHolder1_txtAddress')
        address_input.send_keys(address)
        # Submit the form
        submit_btn = self.driver.find_element_by_id('ContentPlaceHolder1_Button1')
        submit_btn.click()
        # Soupify
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # in order: Snapshot Date, Block, Token Quant, Quant Delta
        form_results = soup.find_all('div', {'class': 'media-body'})
        ether_amount = form_results[2].find('span').text
        ether_amount = ether_amount.replace('Ether', '').strip()
        block_number = form_results[1].find('span').text
        date_number = f'{day}-{month}-{year}'
        # UNIX timestamp from submitted DD-MM-YYYY -> int cast since
        timestamp = int(time.mktime(datetime.datetime.strptime(date_number, "%d-%m-%Y").timetuple()))
        return {
            'address': address,
            'ether_balance': ether_amount,
            'block_number': block_number,
            'timestamp': str(timestamp)  # int to str for consistency
        }

    def etherscan_erc20_historic_balance(self, address, date, token):
        year, month, day = date.split('-')
        url_to_scrape = 'https://etherscan.io/tokencheck-tool'
        self.driver.get(url_to_scrape)
        # Date first
        self.driver.maximize_window()
        date_input = self.driver.find_element_by_id('date')
        date_input.click()
        date_input.send_keys(Keys.CONTROL, 'a')
        date_input.send_keys(f'{month}.{day}.{year}')
        # Address second -> clears focus from Date field, minimizing the calendar popup that obstructs the "Submit" btn
        address_input = self.driver.find_element_by_id('ContentPlaceHolder1_txtAccount')
        address_input.send_keys(address)
        # Contract address
        token_input = self.driver.find_element_by_id('ContentPlaceHolder1_txtAddress')
        token_input.send_keys(token)
        # Privacy notification
        privacy_got_it = self.driver.find_element_by_id('btnCookie')
        if privacy_got_it:
            privacy_got_it.click()
        # Submit the form
        submit_btn = self.driver.find_element_by_id('ContentPlaceHolder1_Button1')
        submit_btn.click()
        # Soupify
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # in order: Snapshot Date, Block, Token Quant, Quant Delta
        form_results = soup.find_all('div', {'class': 'media-body'})
        token_amount = form_results[2].find('span').text
        block_number = form_results[1].find('span').text
        date_number = f'{day}-{month}-{year}'
        # UNIX timestamp from submitted DD-MM-YYYY -> int cast since
        timestamp = int(time.mktime(datetime.datetime.strptime(date_number, "%d-%m-%Y").timetuple()))
        return {
            'address': address,
            'token_address': token,
            'token_balance': token_amount,
            'block_number': block_number,
            'timestamp': str(timestamp)  # int to str for consistency
        }