"""
Flask server for emotion detection using Watson NLP API.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Flask route that receives a GET request with a text parameter,
    processes it using the emotion_detector function, and returns
    a formatted response based on the detected emotions.
    """
    text_to_analyze = request.args.get('text')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(debug=True)
