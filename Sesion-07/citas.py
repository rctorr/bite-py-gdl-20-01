"""
Script araña para el módulo scrapy
"""

import scrapy

class CitasArania(scrapy.Spider):
    name = "citas"
    start_urls = [
        "http://quotes.toscrape.com/",
    ]
    
    def parse(self, respuesta):        
        # Obtener cita y autor para todas la citas en la pagina
        for cita in respuesta.css("div.quote"):
            yield {
                "texto":cita.css("span.text::text").get(),
                "autor":cita.xpath("span/small/text()").get()
            }
        # Navegación al resto de las páginas
        pagsig = respuesta.css('li.next a::attr("href")').get()
        if pagsig is not None:  # hay pagina siguiente?
            yield respuesta.follow(pagsig, self.parse)
