# vaccinazione_COVID19
Andamento della vaccinazione per COVID19 in Italia, per regione. 
I dati sono ottenuti attraverso scraping utilizzando Selenium.

Sono stati aggiunte varie informazioni ritenute utili tra cui popolazione per regione, copertura vaccinale.

Una volta che i dati verranno resi pubblici in formato machine-readable, questo repo sarà probabilemnte dismesso.

## Struttura

* andamento_giornaliero = andamento giornaliere delle varie regioni
* andamento_giornaliero_gruppi = andamento giornaliero per fasce d'età.
* andamento_giornaliero_categorie = andamento giornaliero per categorie (Personale sanitario etc.)
* andamento_giornaliero_regioni = andamento nel tempo per ogni regione. In "Totale.csv" è presente l'andamento nazionale.


## Fonte

I dati vengono presi dall'interfaccia ufficiale https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9

## Dipendenze
* selenium~=3.141.0
* matplotlib~=3.1.1
* pandas~=0.25.1
* numpy~=1.16.5

## Struttura Attuale
Regioni | Somministrazioni | Dosi consegnate | Percentuale | Popolazione | Personale Sanitario | Copertura | Copertura Teorica | Data | 
--- | --- | --- | --- |--- |--- |--- |--- |

Significato delle colonne:
  * Regioni = nome regione
  * Somministrazoni = totale dosi somministrate
  * Dosi consegnate = totale dosi consegnate
  * Percentuale = percenuale dosi somministrate
  * Popolazione = popolazione regione, dati ISTAT 2019
  * Personale Sanitario = totale personale sanitario, dati ISTAT 2017
  * Copertura = copertura vaccinale basata su dosi somministrate sull'intera popolazione
  * Copertura Teorica = copertura vaccinale teorica basate su dosi consegnate (sull'intera popolazione)
  * Data = data di aggiornamento dei dati (inclusa)
  

## Disclaimer
Mi sollevo dai ogni responsabilità sulla correttezza dei dati. Potrebbero essere presenti errori occorsi durante l'ottenimento dei suddetti.


## Esempio Grafici Andamento Regionale

![alt text](https://github.com/dallanoce/vaccinazione_COVID19/blob/main/andamento_giornaliero_regioni_grafici/Abruzzo.png)
