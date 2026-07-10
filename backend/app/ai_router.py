from fastapi import APIRouter
from ai_engine.core.analyzer import MatchAnalyzer

router = APIRouter()

analyzer = MatchAnalyzer()


@router.post("/analyze")
def analyze_match(match_data: dict):

    result = analyzer.analyze(match_data)

    return {
        "betvision_ai": result
    }
