#import
import qrcode
import os
import subprocess

#configurazione
lettura = open("parametri.txt", "r").readlines()
conf = "CONFIGURATO" in lettura
lettura.close()
if conf == False:
    ##file
    file = open("parametri.txt", "w")
    percorso = input('inserisci qui il percorso della cartella in cui salvare le immagini che conterranno i codici QR')
    file.write(percorso)
    file.write('CONFIGURATO')
    print('ok, operazione completata')
    file.close()
else:
    print("benvenuto nel creatore qr code!!!")
    #spostamento directory
    os.chdir(percorso)
    #creazione codice qr
    img = qrcode.make('ciao, questo è un testo di prova')
    img.save("prova_1.jpg")