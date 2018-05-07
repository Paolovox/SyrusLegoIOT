import os
import time

email = raw_input('Inserisci l\'email su cui ricevere i fotogrammi: ')

print ("L\'email che hai scelto e' "+email)



print("Ogni 3 minuti riceverai una foto all'email appena scelta.")
while True:

        time.sleep(5)
        os.system("python snapshot.py")
        print("Foto scattata")

        os.system("python sendmailwithattachment.py "+email)
        print("Foto inviata")

        time.sleep(160)

        print("Tra 20 secondi verra' scattata una nuova foto")
        time.sleep(15)

