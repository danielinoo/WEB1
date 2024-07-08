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

    pagina11 : str = ''' 
    <br>
    <br>
    <br>
  
   <div class="container">
   <div class="row">
    <div class="col-sm">
      
           
        <div class="col">
            <div class="card" style="width: 18rem;">
                <img src="img/siamese.jpeg"  width="286" height="245"alt="GATTO">
              <div class="card-body">
                <h5 class="card-title">Siamese</h5>
                <p class="card-text"></p>
                <a href="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://it.wikipedia.org/wiki/Siamese_(gatto)&ved=2ahUKEwjumKzS75aHAxV9h_0HHe-vAUEQFnoECC4QAQ&usg=AOvVaw0tqi0whpau_qSNqNL_Kr-v" class="btn btn-primary" target="_blank">vedi caratteristiche</a>
              </div>
             </div>
            </div>
  
    </div>
          '''


    pagina12 : str = '''     <br>
    <br>

    <div class="col-sm">
      <div class="card" style="width: 18rem;">
        <img src="img/maine.jpeg"  width="286" height="245"alt="GATTO">
      <div class="card-body">
        <h5 class="card-title">Maine coon</h5>
        <p class="card-text"></p>
        <a href="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://it.wikipedia.org/wiki/Maine_Coon&ved=2ahUKEwiMmufi8JaHAxX7hP0HHeRmD7QQFnoECDcQAQ&usg=AOvVaw3ns9qADW_D4HOlSmjNSQHk" class="btn btn-primary" target="_blank">vedi caratteristiche</a>
      </div>
    </div>
    <br>
    <br>
          '''



    pagina13 = ''' <div class="col-sm">
      
      <div class="col">
        <div class="card" style="width: 18rem;">
            <img src="img/scottich.jpeg"  width="286" height="245"alt="GATTO">
          <div class="card-body">
            <h5 class="card-title">British Shorthair</h5>
            <p class="card-text"></p>
            <a href="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://it.wikipedia.org/wiki/British_Shorthair&ved=2ahUKEwjz2cGx8JaHAxXd7rsIHe9nDW8QFnoECDwQAQ&usg=AOvVaw0PmolSFLEpzgCMxgsy4zsP" class="btn btn-primary" target="_blank">vedi caratteristiche</a>
          </div>
         </div>
        </div>
    </div>
  </div>
</div>
     '''


    pagine_html = pagina11 + pagina12 * n + pagina13
 
    return pagine_html





n = 3


