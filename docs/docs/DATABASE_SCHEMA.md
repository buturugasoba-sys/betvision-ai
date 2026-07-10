# BetVision AI Database

## Users

- id
- username
- email
- password
- subscription
- created_at

---

## Teams

- id
- name
- country
- league

---

## Leagues

- id
- name
- country

---

## Matches

- id
- home_team
- away_team
- league
- match_date
- status

---

## Predictions

- id
- match_id
- confidence_score
- risk_score
- recommendation
- explanation

---

## Statistics

- possession
- shots
- shots_on_target
- xg
- corners
- fouls
- yellow_cards
- red_cards

---

## User History

- user_id
- prediction_id
- viewed_at
