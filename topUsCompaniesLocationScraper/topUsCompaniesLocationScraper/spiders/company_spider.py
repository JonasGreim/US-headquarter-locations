import scrapy
from ..items import TopuscompanieslocationscraperItem


class CompanySpider(scrapy.Spider):
    name = "us-companies"

    def start_requests(self):
        # create array of links that gets scraped
        base_url = "https://money.cnn.com/magazines/fortune/fortune500_archive/full/"
        years = range(1955, 2006)  # Create a range of years (inclusive of 2005)
        urls = [f"{base_url}{year}/" for year in years]

        # urls = [
        #     "https://money.cnn.com/magazines/fortune/fortune500_archive/full/1955/",
        # ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # create item object
        items = TopuscompanieslocationscraperItem()

        year = response.url.split("/")[-2]

        # Select table rows
        table = response.css('table.maglisttable')
        rows = table.css("tr.rowcolor1, tr.rowcolor2")


        # loop through each row and extract data -> save to items
        for row in rows:
            rank = row.css("td.rank::text").get()
            company = row.css("td.company a::text").get()
            first_datacell_value = row.css('td.datacell::text').get()
            second_datacell_value = row.xpath('td[@class="datacell"][2]/text()').extract_first()

            items['rank'] = rank
            items['company'] = company
            items['revenues'] = first_datacell_value
            items['profits'] = second_datacell_value
            items['year'] = year

            yield items



