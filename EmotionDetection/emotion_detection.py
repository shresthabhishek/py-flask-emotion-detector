import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)

    formatted_response = json.loads(response.text)

    # find the dominant emotion
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion_score = -1
    dominant_emotion = None
    for emotion, score in emotion_scores.items():
        
        if score > dominant_emotion_score:
            dominant_emotion = emotion
            dominant_emotion_score = score
            
    
    #return response.text;
    emotion_scores['dominant_emotion'] = dominant_emotion 

    return emotion_scores