import easyocr

reader = easyocr.Reader(['pt'], gpu=True)

#resultados = reader.readtext('https://media.smooch.io/apps/600f2a17ea7d03000c058d41/conversations/bea2a54e0c760b907c3b8f4f/xVyoRn0BNDaw1D11qjk-XBcd/uyBHJHAYJtjNgm2ixhEvwDr2.jpeg', detail = 0)
#resultados = reader.readtext('https://jeroen.github.io/images/testocr.png', detail = 0)
resultados = reader.readtext('https://jeroen.github.io/images/testocr.png', detail = 0)
for resultado in resultados:
    print(resultado)

resultados = reader.readtext('https://www.mattmahoney.net/ocr/stock_gs200.jpg', detail = 0)
for resultado in resultados:
    print(resultado)

resultados = reader.readtext('https://www.iri.com/blog/wp-content/uploads/2021/12/darkshield-ocr-image-preprocessing-final-skewed-result.png', detail = 0)
for resultado in resultados:
    print(resultado)

resultados = reader.readtext('https://awardspersonalization.org/portals/0/images/magazine/insight-images/June21_Figure%20C%20-%20a%20fireplace%20document.jpg', detail = 0)
for resultado in resultados:
    print(resultado)

resultados = reader.readtext('https://media.smooch.io/apps/600f2a17ea7d03000c058d41/conversations/d6b6f2bcb4a7ed8a71c98ce9/8NXQuloWEfh6n2ZcC6_1w-lz/rVDCLPH6T7SMwn8ncevU3wYU.jpeg', detail = 0)
for resultado in resultados:
    print(resultado)
