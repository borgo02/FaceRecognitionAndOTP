# Progetto di esame per Architetture dei calcolatori e Cloud Computing
Nella seguente repository sono stati divisi nelle varie cartelle il codice da caricare nell'Azure function, nell'Arduino e nel Raspberry. Il codice presente nelle cartelle OtpClient ed OtpServer può essere ignorato in quanto utilizzato per trasferire l'istanza all'applicazione sul telefono ed effettuare dei test.

## Configurazione Raspberry
Rimanendo nella cartella principale "Raspberry", "CaptureImageDocker" è stata utilizzata solamente per testare il comando per scattare l'immagine, dobbiamo fare la build dell'immagine Docker. Il comando per eseguire la build è il seguente "sudo docker build -t raspberry_docker ." che si occuperà di eseguire tutte le azioni specifica nel Dockerfile.
Per mandare in esecuzione l'immagine in un container dobbiamo eseguire il seguente comando "sudo docker run -it -v --privileged raspberry_docker", dove il flag -it serve per avere stampati a schermo tutti i log dell'esecuzione. Mentre il flag "--privileged" serve per fare accesso al container a tutte le risorse del Raspberry. Un'alternativa può essere quella di sostituirlo mappando il device con il seguente flag "--device /dev/video0:/dev/video0".

## Esecuzione
Una volta effettuati i collegamenti tra l'Arduino ed il Raspberry tramite cavo usb e collegato il Raspberry alla rete possiamo proseguire. 
Procediamo mandando in esecuzione il container Docker sul Raspberry e successivamente mandiamo in esecuzione il codice anche sull'Arduino. Nel momento in cui si instaura la connessione seriale tra le due schede l'Arduino è pronto a procedere e si mette in ascolto del sensore ad ultrasuoni.
