import scrapy
from ..itemsSP500 import TopUsCompaniesSP500Item


class CompanySp500Spider(scrapy.Spider):
    name = "us-companies-sp500"

    def start_requests(self):
        full_url = "https://www.finhacker.cz/top-20-sp-500-companies-by-market-cap"  # all data is accessible from html with this link
        yield scrapy.Request(url=full_url, callback=self.parse)

    def parse(self, response):
        # TODO iterate over all years
        div_1990 = response.css('div#2024y > div:has(span)')
        year = response.css('div#2024y > div.w3-year > h3::text').get()

        with open('output2.html', 'w') as file:
            for index, div_data in enumerate(div_1990, start=1):
                span_value_market_cap = div_data.css('span::text').get()
                div_value_company = div_data.css('::text').getall()[-1].strip()
                file.write(f'{year}, {index}, "{div_value_company}", "{span_value_market_cap}"\n')




