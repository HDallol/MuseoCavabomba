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

#Hi i'm sos

"""
Ritorna tutte le immagini all'interno del percorso PATH rinominate
in NAME + NUMERO. Funziona con jpg o png.

Esempio path: static/HomeCarouselImgs/
Esempio name: img

Risultato: Array di stringhe con tutti i percorsi di tutte le immmagini

"""
def getImgs(path, name):
        i = 1
        controllo = True
        imgs = []
        while controllo:
                if(exists(path+name+str(i)+".jpg")):
                        imgs.append(path+name+str(i)+".jpg")
                elif(exists(path+name+str(i)+".png")):
                        imgs.append(path+name+str(i)+".png")
                else:
                        controllo = False
                i+=1

        return imgs

app = Flask(__name__)            

nsale = 3       # Numero di sale

sala1 = {
        "nomeSala": "Sala 1",
        "temaSala": "La sala dedicata alla geologia e alla paleontologia.",
        "descrizione": "Questa larga stanza, nata in origine come magazzino dei prodotti della fornace, ospita la biglietteria del Museo. La sala va percorsa in senso orario partendo dalla sinistra della biglietteria e comprende una sezione esterna, addossata alla parete, in cui in modo didattico si introducono tipologie di rocce e fossili, per passare poi alla genesi e alla costituzione dei Colli Euganei, ai fossili eccezionali rinvenuti nel piazzale di Cava e appartenenti al Livello Bonarelli (datato circa 93 milioni di anni fa circa), ai fossili dell’area euganea e al termalismo. Nella sezione centrale invece, da percorrere sempre in senso orario, le vetrine ospitano fossili rappresentativi delle Ere geologiche, alcuni anche di provenienza veneta.",
        "imgMainSala": "static/imgs/salaA/mainSalaA.jpg"
}

sala2 = {
        "nomeSala": "Sala 2",
        "temaSala": "La sala dedicata alla mineralogia.",
        "descrizione": "La sala di mineralogia contiene i migliori esemplari della collezione “Delmo Veronese”, organizzati secondo un criterio sistematico dato dalla classificazione semplificata del mineralogista tedesco Hugo Strunz. Una vetrina è invece dedicata ai minerali provenienti dai Colli Euganei donati da alcuni soci del GMPE, Gruppo Mineralogico Paleontologico Euganeo. Il Museo possiede anche una parte significativa della collezione di Leopoldo Fabris, ormai scomparso, autore tra l’altro di varie pubblicazioni tra cui l’importante testo intitolato Mineralogia Euganea. Tale preziosa collezione è oggetto di revisione scientifica da parte del GMPE (Gruppo Mineralogico Paleontologico Euganeo), coadiuvato dal Dipartimento di Geoscienze dell’Università di Padova. Assieme a campioni di diversa provenienza la collezione Fabris ospita minerali del Triveneto e quella che al momento può essere considerata una delle più importanti collezioni di minerali euganei.",
        "imgMainSala": "static/imgs/salaB/mainSalaB.jpg"
}

sala3 = {
        "nomeSala": "Sala 3",
        "temaSala": "La sala dedicata alla collezione storica di Nicolò Da Rio.",
        "descrizione": "La sala Da Rio ha il fascino di una wunderkammer (camera delle meraviglie), termine utilizzato per designare le collezioni private che anticiparono i moderni musei. Ospita parte della collezione del nobile padovano Nicolò Da Rio (1765 - 1845) che comprendeva oltre 4000 reperti tra minerali, rocce, fossili, oggetti storici e artistici, “mirabilia”. La collezione esposta entro vetrine ottocentesche comprende minerali, rocce e fossili di varia provenienza. Le rocce di provenienza locale furono utili al Da Rio per cercare di dirimere l’acceso dibattito del tempo circa l’origine del Colli Euganei e come base di studio per la sua più importante opera scritta: Orittologia euganea.",
        "imgMainSala": "static/imgs/salaC/mainSalaC.jpg"
}

"""
HOME CAROUSEL IMGS
Per aggiungere immagini al carosello della pagina principale in modo dinamico: 
        - mettere l'immagine in static/HomeCarouselImgs
        - Rinominarla "imgX.jpg" OPPURE "imgX.png" dove X è il numero progressivo
"""
homeCarouselImgs = getImgs("static/HomeCarouselImgs/", "img")


sala1Imgs = getImgs("static/imgs/salaA/","")
sala2Imgs = getImgs("static/imgs/salaB/","")
sala3Imgs = getImgs("static/imgs/salaC/","")


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
                        sala = "sala.html"
                        
                        datiSala = {}
                        immagini = {}

                        if(indice==1):
                                datiSala = sala1
                                immagini = sala1Imgs
                        elif(indice==2):
                                datiSala = sala2
                                immagini = sala2Imgs
                        elif(indice==3):
                                datiSala = sala3
                                immagini = sala3Imgs

                        return render_template(sala, images=immagini, **datiSala)
                else:
                        return redirect(url_for("index"))
        except ValueError:
                return redirect(url_for("index"))
                
        
        


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
