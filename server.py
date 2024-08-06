"""
This module uses flask to create a webapp.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    This route evaluates the emotional tenor of the input text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"]:
        dominant_emotion = f"The dominant emotion is {response.pop('dominant_emotion')}"
        text_output = ', '.join(k+': '+str(v) for k,v in response.items())
        text = f"For the given statement, the system response is {text_output}. {dominant_emotion}."
    else:
        text = "Invalid text! Please try again!"
    return text

@app.route("/")
def render_index_page():
    """
    This route renders the template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
