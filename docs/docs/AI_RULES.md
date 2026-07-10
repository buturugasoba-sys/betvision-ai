# BetVision AI Rules

## Obiectiv

AI-ul trebuie să ofere recomandări bazate pe date, nu pe noroc.

## Factori analizați

- Forma ultimelor 5 meciuri
- Goluri marcate
- Goluri primite
- Meciuri acasă/deplasare
- Accidentări
- Suspendări
- Meciuri directe (H2H)
- Posesie
- Șuturi pe poartă
- xG (Expected Goals)
- Cote bookmaker
- Valoarea lotului
- Programul echipelor
- Motivația (campionat, cupă etc.)

## Scoruri

### Confidence Score
0-100

### Risk Score
0-100

## Reguli

- Nu recomanda un pariu dacă Confidence Score este sub 70.
- Marchează analiza ca risc ridicat dacă lipsesc date importante.
- Explică întotdeauna de ce a fost generată recomandarea.
- Nu face predicții fără suficiente date.
