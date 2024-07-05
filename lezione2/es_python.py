#Daniele Pietropaolo  


def html(n):

    pagine_html : str = '''<!doctype html>
<html lang="en">
  <head>

    <style>p{font-size: larger; color: red;}</style>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sito vacanze</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body style="text-align: center;">
    <h1></h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

'''

    pagina11 : str = '''<div class="container">
        <div class="row">
          <div class="col-sm">
            One of three columns
          </div>'''


    pagina12 : str = '''<div class="col-sm">
            One of three columns
          </div>'''



    pagina13 = '''<div class="col-sm">
            One of three columns
          </div>
        </div>
      </div>'''


    pagine_html = pagina11 + pagina12 * n + pagina13
 
    return pagine_html





n = 3


