# KANTOR (najlepiej po lekcjach o funkcjach jako project dodatkowy)
 
## Krok 1. 
1. Napisz funkcję pobierz_aktualne_dane() do pobierania aktualnych danych o kursach walut. Przydatne będzie ci kilka rzeczy:
2. Zapoznaj się z opisem pobierania danych na stronie NBP: http://api.nbp.pl/
3. Zapoznaj się z funkcją get() z pakietu requests
4. Przypomnij sobie obsługę pakietu json i słowników
5. Przypomnij sobie, jak napisać funkcję
 
## Krok 2.
Napisz kilka potrzebnych funkcji z wykorzystaniem informacji zdobytych w kroku pierwszym:
1. funkcja wylistuj_dostspne_waluty()
2. funkcja kup_walute(waluta, kwota)
3. funkcja sprzedaj_walute(waluta, kwota)
	
## Krok 3.
Zapoznaj się z podstawową obsługą tworzenia interfejsu w notebooku ze strony: 
http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html, a następnie stwórz:
 
1. Selektor tego, czy chcesz kupić czy sprzedać walutę
2. Selektor do wybrania waluty
3. Pole tekstowe, gdzie należy wpisać kwotę
4. Przycisk "oblicz"
	
Potem za pomocą funkcji display() z pakietu IPython.display zobacz, jak prezentują się powyższe elementy.
 
## Krok 4.
Pora połączyć back-end (czyli napisane funkcje) z front-endem (czyli interfejsem)
 
1. Zapoznaj się z funkcją on_click(), którą możesz zastosować na Przycisku (4.)
2. Napisz funkcję wykonaj_na_klik(), która pobiera wartości z elementów interfejsu i w zależności od tego, czy zostało wybrane kupno czy sprzedać printuje ile należy zapłacić lub ile zostanie zapłacone klientowi.
3. Zapoznaj się z funkcją clear_output() z pakietu IPython.display i wykorzystaj ją
	
 
## Krok 5. (dodatkowy) 
A teraz pora na "bonusy":
 
1. Spróbuj upewnić się, że w polu kwota wpisana jest liczba, a jeśli nie, to wyprintuj "Podaj poprawną kwotę w polu "kwota""
2. Zaokrąglij podaną kwotę i rezultat, który program zwraca do dwóch miejsc po przecinku (funkcja round())
3. Stwórz dodatkową funkcjonalność, która pozwala zobaczyć historię kursów z ostatnich 10 dni (spójrz raz jeszcze na stronę NBP) - wyprintuj 10 linijek, gdzie w każdej mamy datę i kurs kupna oraz sprzedaży.
4. Do powyższej funkcjonalności dodaj wizualizację za pomocą pakietu matplotlib
5. (super bonus) Dodaj powyższe dodatki do interfejsu