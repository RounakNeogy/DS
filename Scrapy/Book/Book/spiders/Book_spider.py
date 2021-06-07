import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Book_spider"

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for books in response.css('article.product_pod'):
            yield{
                'image_url': books.css('div.image_container a img::attr(src)').get(),
                'book_title': books.css('h3 a::attr(title)').get(),
                'product_price': books.css('div.product_price p.price_color::text').get(),
            }
        
        next_page=response.css('ul.pager li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)