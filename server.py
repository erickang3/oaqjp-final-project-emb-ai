'''Server file'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detect_emotion():
    ''' Takes in string input from webpage and analyzes the emotions'''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    result = f"""For the given statement, the system response is 'anger': {anger},
             'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
             The dominant emotion is {dominant_emotion}."""

    return result

@app.route('/')
def render_page():
    '''Renders the webpage'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
