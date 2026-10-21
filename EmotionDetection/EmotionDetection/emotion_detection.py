
import requests


def emotion_detector(text_to_analyze):
    """Analyze text using the Watson NLP emotion detection service."""
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return empty_result

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            url, headers=headers, json=payload, timeout=30
        )

        if response.status_code == 400:
            return empty_result

        response.raise_for_status()
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        result = {
            name: emotions[name]
            for name in ("anger", "disgust", "fear", "joy", "sadness")
        }
        result["dominant_emotion"] = max(
            ("anger", "disgust", "fear", "joy", "sadness"),
            key=lambda name: result[name],
        )
        return result

    except (
        requests.RequestException,
        ValueError,
        KeyError,
        IndexError,
        TypeError,
    ):
        return empty_result
