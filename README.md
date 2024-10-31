# Lab 3 Analizator wyników
## Opis Projektu
Celem projektu jest opracowanie modelu regresyjnego, który będzie przewidywał wartość score. Proces modelowania obejmuje:

1. Eksplorację i wizualizację danych.
2. Przetwarzanie danych (obsługa danych kategorycznych i numerycznych, standaryzacja).
3. Trenowanie modelu Random Forest Regressor.
4. Ewaluację modelu za pomocą Średniego Błędu Bezwzględnego (MAE), Średniego Błędu Kwadratowego (MSE) oraz współczynnika determinacji R².
5. Optymalizację modelu z użyciem GridSearchCV do strojenia hiperparametrów.


## Przygotowanie danych oraz wizualizacje
Wstępna analiza obejmowała wczytanie oraz eksplorację danych, aby zrozumieć dostępne zmienne i potencjalne braki danych.

W celu lepszego zrozumienia danych przygotowałam wykresy:
* Zmienne Numeryczne: Histogramy dla każdej zmiennej numerycznej.
* Zmienne Kategoryczne: Wykresy liczności dla każdej zmiennej kategorycznej.

## Przetwarzanie danych
Zmieniłam zmienne kategoryczne na wartości numeryczne przy użyciu kodowania one-hot. Usunełam kolumnę 'rownames', ponieważ mogłaby ona zmienić ostateczme wyniki. Dane nie posiadały żadnych pustych pól, więc pominełam uzupełnianie wartości.
Przeprowadziłam standaryzację w celu spójności danych. 

## Trenowanie i ocena modelu
Do trenowania wybrałam model RandomForestRegressor ze względu na jego odpornośćna przuczenie oraz zdolność obsługi różnorodnych typów danych.
Dane zostały podzielone na zbiór treningowy i testowy w stosunku 80-20.
Jakość modelu oceniłam za pomocą metryk MAE, MSE ora R^2

## Wyniki
Wyniki początkowe:
* MAE: 5.86
* MSE: 53.69
* R²: 0.29
 
Ze względu na niski wynik R^2 zdecydowałam się na próbę optymalizacji modelu poprzez strojenie hiperparametrów.

## Optymalizacja 
GridSearchCV do przeszukania najlepszych wartości hiperparametrów, takich jak n_estimators, max_depth, oraz min_samples_split. Po przeprowadzeniu optymalizacji model uzyskał nieznacznie lepsze wyniki: 
* MAE: 5.86
* MSE: 49.69
* R²: 0.29







