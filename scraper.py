import requests

from bs4 import BeautifulSoup

class AmazonPriceTracker():
    def __init__(self, URL, target_price):
        self.URL = URL

        self.target_price = target_price

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
        }

        cookies = dict(cookies_are='working')

        page = requests.get(self.URL, headers=headers, cookies=cookies)

        self.content = BeautifulSoup(page.text, 'lxml')

        self.product_name = self.content.find(id='productTitle').getText().strip()

        price_text = self.content.find(id='priceblock_ourprice').getText().strip()
        self.price = float(price_text[1:])

    def send_email(self, email):
        print('email is sent')
        pass

    def check_price(self):
        if self.price < self.target_price:
            self.send_email('')

URL = "https://www.amazon.com/eufy-Fingerprint-Electronic-Touchscreen-Weatherproof/dp/B08HYTGFLR/?_encoding=UTF8&pd_rd_w=uvLmw&pf_rd_p=49ff6d7e-521c-4ccb-9f0a-35346bfc72eb&pf_rd_r=W8S7WBTWNRHZH4MKCF9N&pd_rd_r=b1c915fd-55a0-4e02-b875-5d555e454aa6&pd_rd_wg=phaHd&ref_=pd_gw_ci_mcx_mr_hp_d"
apt = AmazonPriceTracker(URL, 300)
print(apt.product_name)
print(apt.price)
apt.check_price()
