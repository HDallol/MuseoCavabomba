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
sas
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
                else:
                        controllo = False
                i+=1

        return imgs

app = Flask(__name__)            

NSALE = 5       # Numero di sale

sala1 = {
        "nomeSala": "Sala A",
        "temaSala": "La sala dedicata alla geologia e alla paleontologia.",
        "descrizione": "Questa larga stanza, nata in origine come magazzino dei prodotti della fornace, ospita la biglietteria del Museo. La sala va percorsa in senso orario partendo dalla sinistra della biglietteria e comprende una sezione esterna, addossata alla parete, in cui in modo didattico si introducono tipologie di rocce e fossili, per passare poi alla genesi e alla costituzione dei Colli Euganei, ai fossili eccezionali rinvenuti nel piazzale di Cava e appartenenti al Livello Bonarelli (datato circa 93 milioni di anni fa circa), ai fossili dell’area euganea e al termalismo. Nella sezione centrale invece, da percorrere sempre in senso orario, le vetrine ospitano fossili rappresentativi delle Ere geologiche, alcuni anche di provenienza veneta.",
        "imgMainSala": "static/imgs/salaA/mainSalaA.jpg"
}

sala2 = {
        "nomeSala": "Sala B",
        "temaSala": "La sala dedicata alla mineralogia.",
        "descrizione": "La sala di mineralogia contiene i migliori esemplari della collezione “Delmo Veronese”, organizzati secondo un criterio sistematico dato dalla classificazione semplificata del mineralogista tedesco Hugo Strunz. Una vetrina è invece dedicata ai minerali provenienti dai Colli Euganei donati da alcuni soci del GMPE, Gruppo Mineralogico Paleontologico Euganeo. Il Museo possiede anche una parte significativa della collezione di Leopoldo Fabris, ormai scomparso, autore tra l’altro di varie pubblicazioni tra cui l’importante testo intitolato Mineralogia Euganea. Tale preziosa collezione è oggetto di revisione scientifica da parte del GMPE (Gruppo Mineralogico Paleontologico Euganeo), coadiuvato dal Dipartimento di Geoscienze dell’Università di Padova. Assieme a campioni di diversa provenienza la collezione Fabris ospita minerali del Triveneto e quella che al momento può essere considerata una delle più importanti collezioni di minerali euganei.",
        "imgMainSala": "static/imgs/salaB/mainSalaB.jpg"
}

sala3 = {
        "nomeSala": "Sala C",
        "temaSala": "La sala dedicata alla collezione storica di Nicolò Da Rio.",
        "descrizione": "La sala Da Rio ha il fascino di una wunderkammer (camera delle meraviglie), termine utilizzato per designare le collezioni private che anticiparono i moderni musei. Ospita parte della collezione del nobile padovano Nicolò Da Rio (1765 - 1845) che comprendeva oltre 4000 reperti tra minerali, rocce, fossili, oggetti storici e artistici, “mirabilia”. La collezione esposta entro vetrine ottocentesche comprende minerali, rocce e fossili di varia provenienza. Le rocce di provenienza locale furono utili al Da Rio per cercare di dirimere l’acceso dibattito del tempo circa l’origine del Colli Euganei e come base di studio per la sua più importante opera scritta: Orittologia euganea.",
        "imgMainSala": "static/imgs/salaC/mainSalaC.jpg"
}

salaAttrezzi = {
        "nomeSala": "Mostra degli attrezzi",
        "temaSala": "La mostra degli attrezzi tradizionali per l'estrazione e la lavorazione della pietra di Antonio Girardi",
        "descrizione": "Nel complesso museale Cava Bomba è presente un cortiletto interno, provvisto di una tettoia, originariamente utilizzata come stalla. Nei primi anni di funzionamento del museo questo spazio è servito per le pause delle scolaresche in visita d'istruzione. \
                        Negli anni 1996-97 si è presentata una buona opportunità: il custode del museo, Antonio Girardi, propose di mettere a disposizione per l'esposizione una singolare raccolta di attrezzi tradizionali per il lavoro nelle cave e per la lavorazione della trachite. \
                        Gli spazi espositivi del complesso erano già tutti occupati ma, data la natura degli oggetti da esporre, si ritenne che la tettoia del cortiletto poteva benissimo quindi ospitare la raccolta senza vetrine, ma con semplici strutture di distanziamento. \
                        La mostra consta di tre sezioni. Da un lato sono esposti gli attrezzi che servivano per sbancare gli strati di calcare e per frantumare le pietre che dovevano alimentare la fornace, quindi relativi alla cava di calcare; nel lato opposto ci sono invece gli attrezzi per il taglio e la lavorazione della trachite. \
                        Nel mezzo, forgia, grande trapano manuale a colonna, incudine ecc., richiamano l'officina del fabbro dove si forgiavano e si riparavano tutti gli attrezzi. \
                        Tutti i reperti esposti sono stati raccolti con passione e competenza da Antonio Girardi, custode del museo Cava Bomba fino al 2006, anno della sua scomparsa. \
                        Nella sezione dedicata alla lavorazione in cava della trachite e riolite compaiono, tra i vari oggetti, le “penole” e i “levarini” per staccare la roccia in blocchi dalla parete di cava, i “punciotti” per rompere la pietra a terra a colpi di mazza, le punte della bocciarda per la rifinitura. \
                        Il filo d'acciaio elicoidale, azionato da un motore, costituisce la tecnica di taglio che sostituisce i cunei o “punciotti” e che viene rappresentata da un modellino in scala realizzato da Antonio Girardi.",
        "imgMainSala": "static/imgs/salaAttrezzi/mainSalaAttrezzi.jpg"
}

salaArcheologia = {
        "nomeSala": "Archeologia industriale",
        "temaSala": "Il percorso dedicato all'archeologia industriale",
        "descrizione": "Le cave di calcare dei Colli Euganei hanno sempre rifornito i forni di cottura dei centri maggiori di Padova, Este e Monselice; nella seconda metà dell'Ottocento, grazie alle migliorate condizioni della rete viaria, è risultato conveniente l'impianto di fornaci da calce anche in numerose località periferiche presso le cave presenti nei Colli (Marendole, Lozzo, Baone, Bastia di Rovolon, ecc.). \
                        L'impianto di Cava Bomba rappresenta tra questi il complesso più imponente nella produzione di calce dei Colli Euganei. Il primo impianto è rappresentato da un tipico forno a tino, risalente all'ultimo decennio del XIX secolo (la data precisa non è nota); successivamente la produzione viene incrementata con la costruzione di altri due forni funzionanti analogamente al primo, ma inglobati in una massiccia costruzione a base quadrata. \
                        Man mano che aumenta l'attività della fornace, culminata nei primi decenni del '900, si rende necessaria la costruzione di nuove strutture edilizie (magazzini, locali di servizio per i fornaciai, stalla per gli animali da soma, ecc.). \
                        Dopo il restauro, realizzato dal Consorzio sotto la guida della Soprintendenza ai Beni Ambientali e Architettonici, il complesso è ritornato alla sua fisionomia originale, salvo l'abbattimento di alcune parti eccessivamente degradate. \
                        Il percorso ottimale ideato per la visita, guidata o autonoma, è supportato da una serie di pannelli didascalici che illustrano la struttura e il funzionamento dei forni e la sequenza del processo produttivo.",
        "imgMainSala": "static/imgs/salaArcheologia/mainSalaArcheologia.png"
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
salaAttrezziImgs = getImgs("static/imgs/salaAttrezzi/","")
salaArcheologiaImgs = getImgs("static/imgs/salaArcheologia/","")
didatticaImgs = getImgs("static/imgs/didattica/","")

slogans = getSlogans("static/slogans/slogans.txt")

@app.route('/')
def index():
        slogan = ""
        if(len(slogans)>0):
                x = random.randint(0, len(slogans)-1)
                slogan = slogans[x]
        print("IMGS:",homeCarouselImgs)
        return render_template("index.html", images=homeCarouselImgs, slogan = slogan)


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
        return render_template("ambiente.html")

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
                
        
        


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
