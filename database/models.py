from dataclasses import dataclass
from datetime import datetime


@dataclass
class Team:
    id: int
    name: str


@dataclass
class Match:
    id: int
    home_team: str
    away_team: str
    match_date: datetime


@dataclass
class Prediction:
    id: int
    match_id: int
    confidence_score: float
    risk_score: float
    recommendation: str
