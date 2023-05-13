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
import random

"""
Ritorna tutti gli slogan all'interno del path specificato (file txt).
Ogni slogan rappresenta una riga del file.
"""
def getSlogans(path):
        slogans = []
        if(exists(path)):
                with open(path,"r", encoding="utf-8") as file:
                        for line in file:
                                slogans.append(line.strip())

        return slogans
            

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
                elif(exists(path+name+str(i)+".webp")):
                        imgs.append(path+name+str(i)+".webp")
                else:
                        controllo = False
                i+=1

        return imgs

app = Flask(__name__)

NSALE = 5       # Numero di sale

sala1 = {
        "nomeSala": "Sala Geologia",
        "temaSala": "La sala dedicata alla geologia e alla paleontologia.",
        "sottoTitolo": "I Fossili",
        "descrizione": """
        Questa larga stanza, nata in origine come magazzino dei prodotti della fornace, ospita la biglietteria del Museo. 
        La sala va percorsa in senso orario partendo dalla sinistra della biglietteria e comprende una sezione esterna, 
        addossata alla parete, in cui in modo didattico si introducono tipologie di rocce e fossili, per passare poi alla genesi 
        e alla costituzione dei Colli Euganei, ai fossili eccezionali rinvenuti nel piazzale di Cava e appartenenti al Livello Bonarelli 
        (datato circa 93 milioni di anni fa), ai fossili dell'area euganea e al termalismo. Nella sezione centrale invece, da 
        percorrere sempre in senso orario, le vetrine ospitano fossili rappresentativi delle Ere geologiche, alcuni anche di provenienza veneta.
        """,
        "imgMainSala": "static/imgs/salaA/mainSalaA.webp",
        "metaDescr":"La sala dedicata alla geologia e alla paleontologia. Questa ospita anche la biglietteria del Museo, oltre alle rocce e ai fossili."
}

sala2 = {
        "nomeSala": "Sala Mineralogia",
        "temaSala": "La sala dedicata alla mineralogia.",
        "sottoTitolo": "I Minerali",
        "descrizione": """
        La sala di mineralogia contiene i migliori esemplari della collezione dell'estense “Delmo Veronese”, 
        organizzati secondo un criterio sistematico dato dalla classificazione semplificata del mineralogista tedesco Hugo Strunz. 
        Una vetrina è invece dedicata ai minerali provenienti dai Colli Euganei donati da alcuni soci del GMPE, Gruppo Mineralogico Paleontologico Euganeo.
        Il Museo possiede anche una parte significativa della collezione di Leopoldo Fabris, scomparso nel 2018, 
        autore tra l'altro di varie pubblicazioni tra cui l'importante testo intitolato Mineralogia Euganea. 
        Tale preziosa collezione è oggetto di revisione scientifica da parte del GMPE (Gruppo Mineralogico Paleontologico Euganeo), 
        coadiuvato dal Dipartimento di Geoscienze dell'Università di Padova. Assieme a campioni di diversa provenienza la collezione 
        Fabris ospita minerali del Triveneto e quella che al momento può essere considerata una delle più importanti collezioni di minerali euganei.
        """,
        "imgMainSala": "static/imgs/salaB/mainSalaB.webp",
        "metaDescr":"La sala dedicata alla mineralogia. Questa contiene la collezione di Delmo Veronese e altri minerali provenienti dai Colli Euganei."
}

sala3 = {
        "nomeSala": "Sala Da Rio",
        "temaSala": "La sala dedicata alla collezione storica di Nicolò Da Rio.",
        "sottoTitolo": "La Collezione",
        "descrizione": """
        La sala Da Rio ha il fascino di una wunderkammer (camera delle meraviglie), termine utilizzato per designare 
        le collezioni private che anticiparono i moderni musei. Ospita parte della collezione del nobile padovano 
        Nicolò Da Rio (1765 - 1845) che comprendeva oltre 4000 reperti tra minerali, rocce, fossili, oggetti storici e artistici, “mirabilia”.
        La collezione esposta entro vetrine ottocentesche riguarda minerali, rocce e fossili di varia provenienza. 
        Le rocce locali furono utili al Da Rio per cercare di dirimere l'acceso dibattito del tempo circa l'origine 
        del Colli Euganei e come base di studio per la sua più importante opera scritta: Orittologia euganea.
        """,
        "imgMainSala": "static/imgs/salaC/mainSalaC.webp",
        "metaDescr":"La sala dedicata alla collezione storica di Nicolò Da Rio. Questa ospita parte della sua collezione, che comprendeva oltre 4000 reperti tra minerali, rocce, fossili, oggetti storici e artistici."
}

salaAttrezzi = {
        "nomeSala": "Mostra degli attrezzi",
        "temaSala": "La mostra degli attrezzi tradizionali per l'estrazione e la lavorazione della pietra di Antonio Girardi.",
        "sottoTitolo": "Gli Attrezzi",
        "descrizione": """
        Nel complesso museale Cava Bomba è presente un cortiletto interno, provvisto di una tettoia, 
        originariamente utilizzato come stalla, cisterna per l'acqua pluviale e deposito. 
        Negli anni 1996-97 il custode del museo, Antonio Girardi, propose di mettere in esposizione una sua 
        singolare raccolta di attrezzi tradizionali per il lavoro nelle cave, del calcare e della trachite.
        Si scelse di collocare la collezione sotto la tettoia del cortile.
        Ci sono quindi esposti cunei di ferro “penole” che venivano infilati nelle fessure delle rocce per romperle, 
        mazze per battere ,“leve”, “levarini”  per sollevare la roccia dopo l'esplosione ottenuta con la polvere da sparo. 
        E ancora cunei di ferro detti “punciotti” per il taglio dei blocchi in blocchi più piccoli, scalpelli e 
        bocciarde per la lavorazione di fino. Indispensabile la forgia del fabbro per mantenere gli attrezzi efficienti.
        """,
        "imgMainSala": "static/imgs/salaAttrezzi/mainSalaAttrezzi.webp",
        "metaDescr":"La mostra degli attrezzi tradizionali per l'estrazione e la lavorazione della pietra di Antonio Girardi. Gli attrezzi sono esposti in un cortiletto interno, senza vetrine."
}

salaArcheologia = {
        "nomeSala": "Archeologia industriale",
        "temaSala": "Il percorso dedicato all'archeologia industriale.",
        "sottoTitolo": "Le Fornaci di Cava Bomba",
        "descrizione": """
        Le cave di calcare dei Colli Euganei rifornirono i forni di cottura dei centri maggiori di Padova, Este e Monselice; 
        nella seconda metà dell'Ottocento, grazie alle migliorate condizioni della rete viaria, risultò conveniente l'impianto 
        di fornaci da calce anche in numerose località periferiche presso le cave presenti nei Colli (Marendole, Lozzo, Baone, Bastia di Rovolon, ecc.).
        L'impianto di Cava Bomba rappresenta tra questi il complesso più imponente nella produzione di calce dei Colli Euganei. 
        Il primo impianto è rappresentato da un tipico forno a tino, risalente all'ultimo decennio del XIX secolo 
        (la data precisa non è nota); successivamente la produzione fu incrementata con la costruzione di altri due forni inglobati 
        in una massiccia costruzione a base quadrata. Il percorso ottimale ideato per la visita, guidata o autonoma, 
        è supportato da una serie di pannelli didascalici che illustrano la struttura e il funzionamento dei forni e la sequenza del processo produttivo.
        """,
        "imgMainSala": "static/imgs/salaArcheologia/mainSalaArcheologia.webp",
        "metaDescr":"Il percorso dedicato all'archeologia industriale. Le cave di calcare dei Colli Euganei hanno sempre rifornito i forni di cottura dei centri maggiori di Padova, Este e Monselice. Oggi, i forni rappresentano un elemento fondamentale nella visita del museo."
}

"""
HOME CAROUSEL IMGS
Per aggiungere immagini al carosello della pagina principale in modo dinamico: 
        - mettere l'immagine in static/imgs/home/carousel/
        - Rinominarla "imgX.jpg" OPPURE "imgX.png" dove X è il numero progressivo
"""
homeCarouselImgs = getImgs("static/imgs/home/carousel/", "")


sala1Imgs = getImgs("static/imgs/salaA/masonry/","")
sala2Imgs = getImgs("static/imgs/salaB/masonry/","")
sala3Imgs = getImgs("static/imgs/salaC/masonry/","")
salaAttrezziImgs = getImgs("static/imgs/salaAttrezzi/masonry/","")
salaArcheologiaImgs = getImgs("static/imgs/salaArcheologia/masonry/","")
didatticaImgs = getImgs("static/imgs/didattica/masonry/","")
ambienteImgs = getImgs("static/imgs/ambiente/masonry/", "")

slogans = getSlogans("static/slogans/slogans.txt")

@app.route('/')
def index():
        slogan = ""
        if(len(slogans)>0):
                x = random.randint(0, len(slogans)-1)
                slogan = slogans[x]
        print("IMGS:",homeCarouselImgs)

        randIndexCarousel = random.randint(1, len(homeCarouselImgs))
        return render_template("index.html", images=homeCarouselImgs, startIndex = randIndexCarousel, slogan = slogan)


@app.route("/contatti")
def contatti():
        return render_template("contatti.html")

@app.route("/museo")
def museo():
        return render_template("museo.html")

@app.route("/storia")
def storia():
        return render_template("storia.html")

@app.route("/ambiente")
def ambiente():
        return render_template("ambiente.html", images = ambienteImgs)

@app.route("/didattica")
def didattica():
        return render_template("didattica.html", images=didatticaImgs)

@app.errorhandler(404)
def paginaNonTrovata(e):
        print("Errore? ", e)
        return render_template("404.html"), 404


# Una stanza per sala o una sala per tre stanze?
# I ipotesi) Hai un template, puoi customizzare testo, img ma non il template generale
# II ipotesi) Puoi customizzare completamente le tre sale per renderle completamente diverse
@app.route('/sala<indice>')
def stanza(indice):
        try:
                indice = int(indice)
                if(indice >=1 and indice<=NSALE):
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
                        elif(indice==4):
                                datiSala = salaAttrezzi
                                immagini = salaAttrezziImgs
                        elif(indice==5):
                                datiSala = salaArcheologia
                                immagini = salaArcheologiaImgs

                        return render_template(sala, images=immagini, **datiSala)
                else:
                        return redirect(url_for("index"))
        except ValueError:
                return redirect(url_for("index"))
                
#Nota: data: non è un granché sicuro
@app.after_request
def headerSicurezza(resp):
        resp.headers["Content-Security-Policy"] = "default-src 'self'; \
                style-src cdn.jsdelivr.net 'self'; \
                script-src 'self' 'unsafe-inline' ajax.googleapis.com unpkg.com 'strict-dynamic' \
                'sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe' \
                'sha384-vtXRMe3mGCbOeY7l30aIg8H9p3GdeSe4IFlP6G8JMa7o7lXvnz3GFKzPxzJdPfGK' \
                'sha384-e3sbGkYzJZpi7OdZc2eUoj7saI8K/Qbn+kPTdWyUQloiKIc9HRH4RUWFVxTonzTg' \
                'sha384-GNFwBvfVxBkLMJpYMOABq3c+d3KnQxudP/mGPkzpZSTYykLBNsZEnG2D9G/X/+7D' \
                'sha384-xzqSMp0j1kPFRh682C5tlArpX5xYGbXGtHPtF693a77VDGMDUZQaAfPbOo3ry0jV' \
                'sha384-92q2i0bvlETKyujVqeFyriIyHvHEr2iSaegMB8aH6tSoCJ3sgUXJ+h7mTziCe8WB' \
                'sha384-xO2TuTohBtx07p7fuqjtBzjIMMxHPlfAc1cGeaGMj+NaUktHMkw3JoR3ewXId90g'; \
                img-src 'self' data:; \
                object-src 'none';\
                base-uri 'none' \
                " 
        return resp

#script-src-elem 'self'  ajax.googleapis.com unpkg.com;\

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
