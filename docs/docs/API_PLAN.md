# BetVision AI API

## POST /analyze

Primește date despre un meci și returnează analiza AI.

Input:

- Echipa gazdă
- Echipa oaspete
- Campionat
- Data meciului

Output:

- Confidence Score
- Risk Score
- Predicția principală
- Predicții alternative
- Explicația AI

---

## GET /matches

Lista meciurilor disponibile.

---

## GET /prediction/{id}

Detaliile unei analize.

---

## GET /health

Verifică dacă serverul funcționează.
