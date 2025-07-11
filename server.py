"""
Flask application for emotion detection.

This module provides a web interface for analyzing emotions in text
using the Watson NLP emotion detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze emotions in the provided text.

    Returns:
        str: Formatted emotion analysis result or error message
    """
    # Get the text to analyze from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Check if the response is valid (not None or empty)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Format the response as requested
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


@app.route("/")
def render_index_page():
    """
    Render the main index page.

    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    