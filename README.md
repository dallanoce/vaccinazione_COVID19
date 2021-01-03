# vaccinazione_COVID19
Andamento della vaccinazione per COVID19 in Italia, per regione. 
All'interno della cartella "andamento_giornaliero" sono presenti i file CSV divisi per giorno. I dati sono ottenuti attraverso scraping utilizzando Selenium.

Sono stati aggiunte varie informazioni ritenute utili tra cui popolazione per regione, copertura vaccinale.

Una volta che i dati verranno resi pubblici in formato machine-readable, questo repo sarà dismesso.

## Fonte

I dati vengono presi dall'interfaccia ufficiale https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9

## Dipendenze
	* numpy
	* datetime
	* PIL
	* pytesseract
	* selenium

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


