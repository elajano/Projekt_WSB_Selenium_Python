# Projekt_WSB_Selenium_Python
SPIS TREŚCI
I.	Cel projektu
II.	Specyfikacja
III.	Środowisko testowe, dane konfiguracyjne
IV.	Opisy przypadków testowych
V.	Skrypty testowe
VI.	Uwagi końcowe
 
I.	Cel projektu:
Opis: 	Testy mają na celu:
1.	Ustalenie obecności ikon z aktywnymi linkami do portali społecznościowych na stronie internetowej www.poland4weekend.com
2.	Weryfikację: czy linki te przenoszą do właściwych profili firmy na portalach społecznościowych

II. 	Specyfikacja:
1.	podana strona do testowania www.poland4weekend.com
2.	podane linki do profili na portalach społecznościowych:
- Facebook: https://www.facebook.com/Poland4Weekend/
- Twitter: https://twitter.com/Poland4W
- Instagram: https://www.instagram.com/poland4weekend/
- użytkownik nie potrzebuje konta na w/w profilach społecznościowych

III. 	Środowisko testowe, dane konfiguracyjne:
System operacyjny komputera: Windows 10, 64-bitowy
Dane o komputerze: Procesor Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz, 16GB RAM
Testy na przeglądarce Chrome wersja:  114.0.5735.90
Testy z wykorzystaniem Python3 i Selenium


IV. 	Opisy przypadków testowych:

I.	Przypadek testowy 
ID:001
Tytuł: Obecność ikon do portali FB, Twitter, Instagram na stronie www.poland4weekend.com
Środowisko: Chrome wersja:  114.0.5735.90
Warunek wstępny: Uruchomiona przeglądarka
Kroki:
1.	wejdź na stronę “https://www.poland4weekend.com/”
2.	zaakceptuj button Cookies
3.	nawiguj do stopki
4.	zrób screenshot stopki
Oczekiwany rezultat:
Ikony FB, Twitter, Instagram są widoczne w stopce strony.

II.	Przypadek testowy 
ID:002
Tytuł: Aktywny link do FB https://www.facebook.com/Poland4Weekend/ 
Środowisko: Chrome wersja:  114.0.5735.90
Warunek wstępny: Uruchomiona przeglądarka, otwarta strona “https://www.poland4weekend.com/”
Kroki:
1.	znajdź element - ikona FB 
2.	sprawdź, czy ikona FB ma aktywny link
3.	sprawdź, czy link z ikony FB przenosi do strony  https://www.facebook.com/Poland4Weekend/

Oczekiwany rezultat:
Link do strony FB jest aktywny.
Link do profilu na FB jest poprawny.
		
III.	Przypadek testowy 
ID:003
Tytuł: Aktywny link do Twitter https://twitter.com/Poland4W 
Środowisko: Chrome wersja:  114.0.5735.90
Warunek wstępny: Uruchomiona przeglądarka, otwarta strona “https://www.poland4weekend.com/”
Kroki:
1.	znajdź element - ikona Twitter 
2.	sprawdź, czy ikona Twitter ma aktywny link
3.	sprawdź, czy link z ikony Twitter przenosi do strony  https://twitter.com/Poland4W 

Oczekiwany rezultat:
Link do strony Twitter jest aktywny.
Link do profilu na Twitter jest poprawny.
		
IV.	Przypadek testowy 
ID:004
Tytuł: Aktywny link do Instagram https://www.instagram.com/poland4weekend/
Środowisko: Chrome wersja:  114.0.5735.90
Warunek wstępny: Uruchomiona przeglądarka, otwarta strona “https://www.poland4weekend.com/”
Kroki:
1.	znajdź element - ikona Instagram
2.	sprawdź, czy ikona Instagram ma aktywny link
3.	sprawdź, czy link z ikony Instagram przenosi do strony  https://www.instagram.com/poland4weekend/ 

Oczekiwany rezultat:
Link do strony Instagram jest aktywny.
Link do profilu na Instagram jest poprawny.

