import urllib.request
import tornado.ioloop
import tornado.web
import sqlite3 as sql
import random
import string
import datetime
e = datetime.datetime.now()



con  = sql.connect("urls.db")
cursor = con.cursor()

class imlinBotAuthHandler(tornado.web.RequestHandler):
  def head(self):
    self.finish()

  def get(self):
    self.write("Thanks for inviting the <a href='https://discord.com/users/993498803598536806'>Imlin bot</a> to your server!")

class mainHandler(tornado.web.RequestHandler):
  def head(self):
    self.finish()

  def get(self):
    self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, HEAD')
    self.render("index.html")
    
 

class imgUploadHandler(tornado.web.RequestHandler):
  def head(self):
    self.finish()

  def get(self):
    self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, HEAD')
    self.render("img.html")

  def post(self):
    files = self.request.files["imgFile"]
    for f in files:
      fha = open(f"img/{f.filename}", "wb")
      fha.write(f.body)
      fha.close
    self.write(f"<a href='https://www.imlin.tk/img/{f.filename}'>Fotoğrafın Linki</a> <title>Imlin</title>")


class urlUploadHandler(tornado.web.RequestHandler):
  def head(self):
    self.finish()

  def get(self):
    self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, HEAD')
    self.render("url.html")

  def post(self):
    url = self.get_argument("urlText")
    name = ''.join(random.choice(string.ascii_letters) for i in range(4))
    urllib.request.urlretrieve(url, "img/" + name + ".jpg")
    self.write(f"<a href='https://www.imlin.tk/img/{name}.jpg'>Fotoğrafın Linki</a> <title>Imlin</title>")
    
  
class txtUploadHandler(tornado.web.RequestHandler):
  def head(self):
    self.finish()

  def get(self):
    self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, HEAD')
    self.render("txt.html")

  def post(self):
    files = self.request.files["txtFile"]
    for f in files:
      fha = open(f"txt/{f.filename}", "a+")
      fha.write(f.body)
      fha.close
    self.write(f"<a href='https://imlin.andecy0.repl.co/txt/{f.filename}'>Txt Dosyasının Linki</a> <title>Imlin</title>")


class apiHandler(tornado.web.RequestHandler):
  def head(self):
    self.finish()


  def get(self):
    self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, HEAD')
    url = self.get_argument('url')
    name = ''.join(random.choice(string.ascii_letters) for i in range(4))                                                  
    urllib.request.urlretrieve(url, "img/" + name + ".jpg")
    self.write({"url": f"https://www.imlin.tk/img/{name}.jpg" })


def make_app():
    return tornado.web.Application([
      (r"/", mainHandler),
      (r"/api", apiHandler),
      (r"/img", imgUploadHandler),
      (r"/url", urlUploadHandler),
      (r"/txt", txtUploadHandler),
      (r"/img/(.*)", tornado.web.StaticFileHandler, {"path" : "img"}),
      (r"/txt/(.*)", tornado.web.StaticFileHandler, {"path" : "txt"}),
      (r"/botauth", imlinBotAuthHandler)
    ])

if __name__ == "__main__":
  app = make_app()
  app.listen(8888)
  print("Site açıldı!")
  tornado.ioloop.IOLoop.current().start()



