
"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Display the form and process emotion analysis requests."""
    result = None
    text = ""
    error = None

    if request.method == "POST":
        text = request.form.get("textToAnalyze", "").strip()

        if not text:
            error = "Please enter some text to analyze."
        else:
            result = emotion_detector(text)
            if result.get("dominant_emotion") is None:
                error = "Unable to analyze the text. Please try again."

    return render_template(
        "index.html", result=result, text=text, error=error
    )

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze text supplied through the URL."""
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Please enter some text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Unable to analyze the text. Please try again.", 400

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
