import scrapy
import json


class CompanySp500Spider(scrapy.Spider):
    name = "us-companies-sp500"

    def start_requests(self):
        full_url = "https://www.finhacker.cz/top-20-sp-500-companies-by-market-cap"  # all data is accessible from html with this link
        yield scrapy.Request(url=full_url, callback=self.parse)


    def parse(self, response):
        data = []
        for year in range(1990, 2025):
            year_selector = f'div#{year}y'
            div_year = response.css(f'{year_selector} > div:has(span)')
            year_text = response.css(f'{year_selector} > div.w3-year > h3::text').get()

            for index, div_data in enumerate(div_year, start=1):
                span_value_market_cap = div_data.css('span::text').get()
                div_value_company = div_data.css('::text').getall()[-1].strip()
                data.append({
                    'year': year_text,
                    'rank': index,
                    'company': div_value_company,
                    'market_cap': span_value_market_cap
                })

        with open('scraped_dataset_sp500.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)