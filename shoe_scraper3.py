import scrapy

class ShoeSpider(scrapy.Spider):
    name = 'shoespider'
    start_urls = ['https://undefeated.com/collections/all']

    def parse(self, response):
        for div in response.css('div.product_wrap '):

            yield {
                # 'price': article.css(".price_color::text").extract_first(),
                # 'title': article.css("h3 > a::attr(title)").extract_first()
                'name': div.css(".grid-product__title::text").extract_first(),
                'price': div.css(".money::text").extract_first()
            }

            next = response.css('#AjaxinatePagination > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)
