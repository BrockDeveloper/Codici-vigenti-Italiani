# ⚖️ Codici vigenti Italiani

Parser per i testi dei principali Codici della Legge Italiana, per rendere facilmente accessibile ciò che, per ora, non lo è.

> **Disclaimer** Tutto il contenuto è stato ottenuto a partire dai dati disponibili sul sito di Normattiva (www.normattiva.it), a cura della Presidenza del Consiglio dei Ministri e dell'Istituto Poligrafico e Zecca dello Stato. Questo progetto né normattiva sono sono responsabili di eventuali errori o imprecisioni, nonchè di danni conseguenti ad azioni o determinazioni assunte in base alla consultazione.

> **WIP** Il progetto è in corso di sviluppo, per ora il solo parser è completo e funzionante 

## Motivazioni
Le principali normative italiane sono difficilmente accessibili in formato digitale. Alcuni siti ne offrono la consultazione, ma con una navigazione appesantita da pubblicità e comunque non ne permettono l'esportazione in un formato adatto.
L'unico sito in grado di fornire una consultazione degna è Normattiva, che però presenta un'eterogeneità nelle modalità di rappresentazione delle varie normative, questo si ripercuote inevitabilmente anche nelle esportazioni, che sono tutt'altro che di facile lettura ed utilizzo.

## Realizzazione
L'esportazione più pulita tra tutte è in formato RTF, ma presenta comunque problemi di formattazione, discrepanze tra normative e varie incongruenze. Il lavoro di questo parser è, partendo da questi file, renderne il contenuto il più pulito possibile, per poi analizzarne il contenuto e fornire una rappresentazione degli stessi in un formato Json (propriamente, dizionari Python).

## Rest API
Il parser fornisce già le normative in un formato utilizzabile e comprensibile, ma per rendere questo progetto accessibile direttamente senza il dover integrare file Json o eseguire codice in Python, le normative stesse vengono riproposte come REST API, secondo la seguente documentazione.

---

licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/