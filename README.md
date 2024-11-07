# Lab4-s25896 - Score prediction

Aplikacja Flask przewidująca wartość zmiennej `score` na podstawie danych dotyczących wykształcenia i tła społecznego. Aplikacja wykorzystuje wytrenowany model regresji do przewidywania wyniku (oceny), który może być pomocny w analizie wyników edukacyjnych.

## Spis treści
- [Wymagania](#wymagania)
- [Klonowanie repozytorium](#klonowanie-repozytorium)
- [Uruchamianie aplikacji lokalnie](#uruchamianie-aplikacji-lokalnie)
- [Uruchamianie aplikacji za pomocą Dockera](#uruchamianie-aplikacji-za-pomocą-dockera)
- [Użycie obrazu z Docker Hub](#użycie-obrazu-z-docker-hub)
- [Użycie](#użycie)

## Wymagania
- Python 3.9+
- Wymagane biblioteki wymienione w requirements.txt
- Docker (jeśli planujesz uruchomić aplikację w kontenerze)

## Klonowanie repozytorium

Aby sklonować to repozytorium, wykonaj:

```bash
git clone https://github.com/juliaChainska/Lab4_s25896.git
cd Lab4-s25896
```

## Uruchamianie aplikacji lokalnie

1. Zainstaluj zależności:
Upewnij się, że masz plik requirements.txt z listą wymaganych pakietów. Aby zainstalować zależności, użyj:
```bash
pip install -r requirements.txt
```

2. Uruchom skrypt treningowy (jeśli model nie został jeszcze wygenerowany):

    Skrypt train_model.py pobiera dane z zewnętrznego repozytorium GitHub i zapisuje przeszkolony model do pliku model.pkl.
```bash
python train_model.py
```

3. Uruchom aplikację:
```bash
python app.py
```

4. Testuj aplikację: API jest dostępne na http://127.0.0.1:5001/predict

## Uruchamianie aplikacji za pomocą Dockera
1. Zbuduj obraz Dockera:
```bash
docker build -t jchainska/flask_score_predict .
```
2. Uruchom kontener:
```bash
docker run -p 5001:5001 jchainska/flask_score_predict
```
3. Dostęp do API: aplikacja będzie dostępna na http://127.0.0.1:5001/predict.

## Użycie obrazu z Docker Hub
1. Pobierz obraz z Docker Huba:
```bash
docker pull jchainska/flask_score_predict
```
2. Uruchom kontener:
```bash
docker run -p 5001:5001 jchainska/flask_score_predict
```

## Użycie
Po uruchomieniu aplikacji (lokalnie lub w Dockerze), możesz użyć endpointu /predict, aby uzyskać przewidywania.

### Przykładowe Żądanie
Wyślij żądanie POST na http://localhost:5001/predict z danymi w formacie JSON:

```json
[
  {
    "fcollege": "yes",
    "mcollege": "no",
    "home": "yes",
    "urban": "yes",
    "unemp": 6.2,
    "wage": 8.09,
    "distance": 0.2,
    "tuition": 0.88915,
    "education": 12,
    "region": "other"
  }
]
```

### Przykładowa Odpowiedź:
Aplikacja odpowie obiektem JSON zawierającym przewidywaną wartość score:

```json
    "predictions": [
        43.172767823537185
    ]
```

