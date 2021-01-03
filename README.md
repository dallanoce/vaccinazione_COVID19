# vaccinazione_COVID19
Andamento della vaccinazione per COVID19 in Italia, per regione. 
I dati sono ottenuti attraverso scraping utilizzando Selenium.

Sono stati aggiunte varie informazioni ritenute utili tra cui popolazione per regione, copertura vaccinale.

Una volta che i dati verranno resi pubblici in formato machine-readable, questo repo sarà dismesso.

## Struttura

* andamento_giornaliero = andamento giornaliere delle varie regioni
* andamento_giornaliero_gruppi = andamento giornaliero delle fasce d'età.


## Fonte

I dati vengono presi dall'interfaccia ufficiale https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9

## Dipendenze
	Numpy
	Datetime
	Selenium

## Struttura Attuale
Regioni | Somministrazioni | Dosi consegnate | Percentuale | Popolazione | Copertura | Copertura Teorica | Data | 
--- | --- | --- | --- |--- |--- |--- |--- |

Significato delle colonne:
  * Regioni = nome regione
  * Somministrazoni = totale dosi somministrate
  * Dosi consegnate = totale dosi consegnate
  * Percentuale = percenuale dosi somministrate
  * Popolazione = popolazione regione
  * Copertura = copertura vaccinale basata su dosi somministrate
  * Copertura Teorica = copertura vaccinale teorica basate su dosi consegnate
  * Data = data di aggiornamento dei dati (inclusa)
  

## Disclaimer
Mi sollevo dai ogni responsabilità sulla correttezza dei dati. Potrebbero essere presenti errori occorsi durante l'ottenimento dei suddetti.


