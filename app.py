#progetto di Alessandro Contarini per il Museo Cava Bomba di Cinto Euganeo
#5^AI
#20/10/2022
#gestione webApp


from fileinput import filename
from genericpath import exists
import genericpath
import os
from flask import Flask,render_template,redirect, request, url_for
import json



app = Flask(__name__)            

nsale = 3       # Numero di sale


homeCarouselImgs = []
i = 1
controllo = True

"""
Per aggiungere immagini al carosello della pagina principale in modo dinamico: 
        - mettere l'immagine in static/HomeCarouselImgs
        - Rinominarla "imgX.jpg" OPPURE "imgX.png" dove X è il numero progressivo
"""
while controllo:
        if(exists("static/HomeCarouselImgs/img"+str(i)+".jpg")):
                homeCarouselImgs.append("static/HomeCarouselImgs/img"+str(i)+".jpg")
        elif(exists("static/HomeCarouselImgs/img"+str(i)+".png")):
                homeCarouselImgs.append("static/HomeCarouselImgs/img"+str(i)+".png")
        else:
                controllo = False
        i+=1


@app.route('/')
def index():
         pagina ='intro.html'
         print("IMGS:",homeCarouselImgs)
         return render_template("index.html", images=homeCarouselImgs)


@app.route("/contatti")
def contatti():
        return render_template("contatti.html")

@app.route("/faq")
def faq():
        return render_template("faq.html")

@app.route("/orari")
def orari():
        return render_template("orari.html")

# Una stanza per sala o una sala per tre stanze?
# I ipotesi) Hai un template, puoi customizzare testo, img ma non il template generale
# II ipotesi) Puoi customizzare completamente le tre sale per renderle completamente diverse
@app.route('/sala<indice>')
def stanza(indice):
        try:
                indice = int(indice)
                if(indice >=1 and indice<=nsale):
                        sala = "sala"+str(indice)+".html"
                        return render_template(sala)
                else:
                        return redirect(url_for("index"))
        except ValueError:
                return redirect(url_for("index"))
                
        
        


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
