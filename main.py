from bs4 import BeautifulSoup
import requests
import logging
from math import *
import pandas as pd
import urllib.parse
import sys

logging.basicConfig(level=logging.INFO)

url = [
    {'website':'https://www.fye.com/toys-collectibles/action-figures/funko/?sz=60', 'bloc_item':'st-tile-grid__wrapper', 'item':'st-tile-grid__item'}
]



class PopScrapper:
    headers = {"User-Agent": "Chrome/5.0"}
    parser = 'html.parser'


    def __init__(self, url):
        self.url = url


    def request_url(self):
        response = requests.get(self.url)
        html = response.content
        return BeautifulSoup(requests.get(self.url, headers=self.headers).text,self.parser)


    @staticmethod
    def get_website_domaine(url):
        '''
        Returns domain name from an url.

        Returns:
            string:Domain name.
        '''
        parsed_url = urllib.parse.urlparse(url)
        return parsed_url.netloc


    def get_nb_total_elem(self):
        response = requests.get(self.url)
        html = response.content
        soup = BeautifulSoup(requests.get(self.url, headers=self.headers).text,self.parser)
        if soup.title.text == 'Queue-it':
            logging.warning('page {} - not available for the function {}'.format(self.url, 'get_nb_total_elem'))
            return None
        else:
            return int(soup.find('p', attrs={'id' : 'toolbar-amount'}).find('span', attrs={'class' : 'toolbar-number'}).text)


    def get_nb_elem_by_page(self):
        response = requests.get(self.url)
        html = response.content
        soup = BeautifulSoup(requests.get(self.url, headers=self.headers).text,self.parser)
        if soup.title.text == 'Queue-it':
            logging.warning('page {} - not available for the function {}'.format(self.url, 'get_nb_elem_by_page'))
            return None
        else:
            return int(soup.find('select', attrs={'id' : 'limiter'}).find('option', attrs={'selected' : 'selected'}).text)










if __name__ == "__main__":


    #############################################################
    #########################  COLEKA  ##########################
    #############################################################


    pop = PopScrapper('https://www.coleka.com/fr/figurines-de-collection/funko/funko-pop-vinyl_r2191')
    html = pop.request_url()
    block_content = html.find('ul', attrs={'class' : 'row img-list list-rub list-item'})


    for content in block_content.findAll('li', attrs={'class' : 'col-sm-3 col-xs-6'}):
        # print(content.find('a', attrs={'class' : ['lib_has_3_lines','defer lib_has_3_lines']})['href'])
        # print(content.find('a', attrs={'class' : ['lib_has_3_lines','defer lib_has_3_lines','  defer lib_has_2_lines']}))
        print(content.find('a', attrs={'class' : ['lib_has_3_lines','defer lib_has_3_lines','  defer lib_has_3_lines']})['href'])

        print()
        print()
        print()























    #############################################################
    ##########################  FYE  ############################
    #############################################################

    # pop = PopScrapper('https://www.fye.com/toys-collectibles/action-figures/funko/?sz=60')
    # # nb_results_total = pop.get_nb_total_elem()
    # # nb_results_by_page = pop.get_nb_elem_by_page()
    # # print(PopScrapper.get_website_domaine('https://www.fye.com/toys-collectibles/action-figures/funko/?sz=60'))
    #
    #
    # response2 = requests.get(pop.url)
    # html2 = response2.content
    # soup2 = BeautifulSoup(requests.get(pop.url, headers=pop.headers).text,pop.parser)
    # nb_results_by_page = int(soup2.find('div', attrs={'class' : 'c-pagination__results-count'}).text.split('of')[0].split('-')[1].strip())
    # nb_results_total = int(soup2.find('div', attrs={'class' : 'c-pagination__results-count'}).text.split('of')[1].strip())
    #
    #
    # if nb_results_total is not None and nb_results_by_page is not None:
    #     nb_page = ceil(nb_results_total / nb_results_by_page)
    #     items = []
    #
    #     for i in range(1,nb_page):
    #         url2="https://www.fye.com/toys-collectibles/action-figures/funko/?start={}&sz=60".format(nb_results_by_page*i)
    #
    #         response = requests.get(url2)
    #         html = response.content
    #         soup = BeautifulSoup(requests.get(url2, headers={"User-Agent": "Chrome/5.0"}).text,'html.parser')
    #         tt = soup.find('div', attrs={'class' : 'st-tile-grid__wrapper'})
    #
    #         for item in tt.findAll('div', attrs={'class' : 'st-tile-grid__item'}):
    #             print(item.find('a', attrs={'class' : 'c-product-tile__product-name-link'}).text)
    #             items.append([item.find('a', attrs={'class' : 'c-product-tile__product-name-link'}).text,item.find('span', attrs={'class' : 'product-sales-price'}).text])
    #
    #     df = pd.DataFrame(items)
    #     df.to_csv("pop.csv")
    #
    #     #
    #     #     for spans in soup.findAll('li', attrs={'class' : 'item product product-item'}) :
    #     #
    #     #         items.append([
    #     #             spans.find('div', attrs={'class' : 'product-item-info'}).find('div', attrs={'class' : 'product details product-item-details'}).find('strong', attrs={'class' : 'product name product-item-name'}).text,
    #     #             spans.find('div', attrs={'class' : 'product-item-info'}).find('div', attrs={'class' : 'product details product-item-details'}).find('div', attrs={'class' : 'price-box price-final_price'}).find('span', attrs={'class' : 'price-container price-final price-final_price price-final_price tax weee'}).find('span', attrs={'class' : 'price-wrapper'}).find('span', attrs={'class' : 'price'}).text
    #     #         ])
    #     #
    #     # df = pd.DataFrame(items)
    #     # df.to_csv("pop.csv")
    # else:
    #     pass
    #     # logging.warning('End of script due to website source {} unavailable(Queue)'.format(pop.get_website_domaine()))


















    # html = pop.request_url()
    # tt = html.find('div', attrs={'class' : 'st-tile-grid__wrapper'})
    #
    #
    # for item in tt.findAll('div', attrs={'class' : 'st-tile-grid__item'}):
    #     print(item.find('a', attrs={'class' : 'c-product-tile__product-name-link'}).text)
    #     print(item.find('span', attrs={'class' : 'product-sales-price'}).text)













    # if nb_results_total is not None and nb_results_by_page is not None:
    #     nb_page = ceil(nb_results_total / nb_results_by_page)
    #     items = []
    #
    #     for i in range(0,nb_page-1):
    #         url2="https://www.popcultcha.com.au/shop-by/manufacturer/funko.html?cat=21974&p={}".format(i)
    #         response = requests.get(url2)
    #         logging.info('page {} - http response :  {}'.format(i, response.status_code))
    #
    #         html = response.content
    #         soup = BeautifulSoup(requests.get(url2, headers={"User-Agent": "Chrome/5.0"}).text, 'html.parser')
    #
    #         for spans in soup.findAll('li', attrs={'class' : 'item product product-item'}) :
    #
    #             items.append([
    #                 spans.find('div', attrs={'class' : 'product-item-info'}).find('div', attrs={'class' : 'product details product-item-details'}).find('strong', attrs={'class' : 'product name product-item-name'}).text,
    #                 spans.find('div', attrs={'class' : 'product-item-info'}).find('div', attrs={'class' : 'product details product-item-details'}).find('div', attrs={'class' : 'price-box price-final_price'}).find('span', attrs={'class' : 'price-container price-final price-final_price price-final_price tax weee'}).find('span', attrs={'class' : 'price-wrapper'}).find('span', attrs={'class' : 'price'}).text
    #             ])
    #
    #     df = pd.DataFrame(items)
    #     df.to_csv("pop.csv")
    # else:
    #     logging.warning('End of script due to website source {} unavailable(Queue)'.format(pop.get_website_domaine()))



    # url="https://www.popcultcha.com.au/shop-by/manuf    def get_nb_total_elem(url):
    # response = requests.get(url)
    # html = response.content
    # headers = {"User-Agent": "Chrome/5.0"}
    # soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    #
    # headers = {"User-Agent": "Chrome/5.0"}
    # items = []
    #
    # for i in range(1,5):
    #     url="https://www.popcultcha.com.au/shop-by/manufacturer/funko.html?p={}&product_list_limit=144".format(i)
    #     response = requests.get(url)
    #     # print('round {} : {}'.format(i, response.status_code))
    #     logging.info('page {} - http response :  {}'.format(i, response.status_code))
    #
    #     html = response.content
    #     soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    #
    #     print(soup.find('p', attrs={'id' : 'toolbar-amount'}).find('span', attrs={'class' : 'toolbar-number'}).text)
    #
    #     print(soup.find('select', attrs={'id' : 'limiter'}).find('option', attrs={'selected' : 'selected'}).text)
    #
    #     nb_results_total = int(soup.find('p', attrs={'id' : 'toolbar-amount'}).find('span', attrs={'class' : 'toolbar-number'}).text)
    #     nb_results_by_page = int(soup.find('select', attrs={'id' : 'limiter'}).find('option', attrs={'selected' : 'selected'}).text)
    #     nb_page = nb_results_total / nb_results_by_page
    #
    #     print(ceil(nb_page))


        # for spans in soup.findAll('li', attrs={'class' : 'item product product-item'}) :
            # print(spans.find('div', attrs={'class' : 'product-item-info'}).find('div', attrs={'class' : 'product details product-item-details'}))
            # print(spans.find('div', attrs={'class' : 'product-item-info'}).find('div', attrs={'class' : 'product details product-item-details'}).find('div', attrs={'class' : 'price-box price-final_price'}).find('span', attrs={'class' : 'price-container price-final price-final_price price-final_price tax weee'}).find('span', attrs={'class' : 'price-wrapper'}).find('span', attrs={'class' : 'price'}).text)
            # print()
            # print()
            # print()

            # items.append([
            #     spans.find('div', attrs={'class' : 'product-item-info'}).find('div', attrs={'class' : 'product details product-item-details'}).find('strong', attrs={'class' : 'product name product-item-name'}).text,
            #     spans.find('div', attrs={'class' : 'product-item-info'}).find('div', attrs={'class' : 'product details product-item-details'}).find('div', attrs={'class' : 'price-box price-final_price'}).find('span', attrs={'class' : 'price-container price-final price-final_price price-final_price tax weee'}).find('span', attrs={'class' : 'price-wrapper'}).find('span', attrs={'class' : 'price'}).text
            # ])

    # print(items)

    # df = pd.DataFrame(items)
    # df.to_csv("pop2.csv")







    # headers = {"User-Agent": "Chrome/5.0"}
    # items = []
    #
    # for i in range(1,8):
    #     print('round {}'.format(i))
    #
    #     url="https://funkoeurope.com/collections/pop?page={}".format(i)
    #     response = requests.get(url)
    #     print(response.status_code)
    #
    #     html = response.content
    #     soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    #
    #     for spans in soup.findAll('div', attrs={'class' : 'product-item product-item--vertical 1/3--tablet 1/4--lap-and-up'}) :
    #         items.append([
    #             spans.find('div', attrs={'class' : 'product-item__info'}).find('div', attrs={'class' : 'product-item__info-inner'}).find('div', attrs={'class' : 'product-meta__vendor'}).text,
    #             spans.find('div', attrs={'class' : 'product-item__info'}).find('div', attrs={'class' : 'product-item__info-inner'}).find('a', attrs={'class' : 'product-item__title text--strong link'}).text,
    #             spans.find('div', attrs={'class' : 'product-item__info'}).find('div', attrs={'class' : 'product-item__info-inner'}).find('div', attrs={'class' : 'product-item__price-list price-list'}).find('span', attrs={'class' : 'price'}).text[1:]
    #         ])
    #
    # # print(items)
    #
    # df = pd.DataFrame(items)
    # df.to_csv("pop.csv")
