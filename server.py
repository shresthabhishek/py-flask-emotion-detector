'''
Module for detecting emotions of the user provided input using AI

Executing this function initiates the application of emotion detection
to be executed over the Flask channel and deployed on
localhost:5000.
'''

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion score as well as the dominant emotion
        for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_scores = emotion_detector(text_to_analyze)

    if emotion_scores['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    resp_text = "For the given statement, the system response is"

    cnt = len(emotion_scores)
    i = 0
    for emo, score in emotion_scores.items():
        i = i+1
        if emo == 'dominant_emotion':
            resp_text += '. The dominant emotion is joy.'
        elif i == cnt -1:
            # remove the trailing comma
            resp_text = resp_text[:-1]
            resp_text += f" and '{emo}': {score}"
        else:
            resp_text += f" '{emo}': {score},"

    return resp_text


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
