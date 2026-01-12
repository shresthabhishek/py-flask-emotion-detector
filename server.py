from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_scores = emotion_detector(text_to_analyze)
    
    #print(emotion_scores)

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
            resp_text += " and '{}': {}".format(emo, score)
        else:
            resp_text += " '{}': {},".format(emo, score)

    return resp_text


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)