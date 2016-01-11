Boulder Dash
===================

Grę możemy uruchomić z konsoli za pomocą polecenia `./boulderDash.py`.

### Opis gry

Celem gry jest zdobycie odpowiedniej liczby diamentów. Należy uważać na kamienie i diamenty, które mogą spaść na postać. W takim przypadku następuje koniec gry.

#### Podstawowe zasady gry:
* **Kamienie** i **diamenty** spadają, jeżeli pod nimi jest pusta przestrzeń.
* **Kamienie** i **diamenty** nie mogą stac na sobie, jeśli nie sa podtrzymywanie z boku. (Jeżeli pole znajdujące się obok i pole poniżej tego pola są wolne, to kamień lub diament spadnie po skosie.)
* **Kamienie** mogą być odpychane w lewo lub w prawo, jeśli przed nimi lub za nimi jest pusta przestrzeń.

#### Pozostałe elementy gry:
* **Mur** - otacza całą planszę, nie można go poruszyć, zniszczyć ani na niego wejść.
* **Ziemia** - można na nią wejść odkrywając puste pole.

#### Sterowanie:
Możemy poruszać się postacią przy użyciu klawiatury za pomocą klawiszy:
* &uarr; - w górę.
* &darr; - w dół.
* &larr; - w lewo.
* &rarr; - w prawo.
* P - pauza.
