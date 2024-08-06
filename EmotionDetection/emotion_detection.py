import requests
import json as js

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """
    This function evaluates the emotional tenor of the input text
    """
    req = requests.post(url=URL, headers=HEADERS, json={"raw_document": {"text": text_to_analyze}})
    if req.status_code == 200:
        json_dict = js.loads(req.text)
        emotions = json_dict["emotionPredictions"][0]["emotion"]
        dominant_emotions = [k for k,v in emotions.items() if v==max(list(emotions.values()))]
        emotions["dominant_emotion"] = ",".join(dominant_emotions)
    elif req.status_code == 400:
        emotions = {x:None for x in ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]}
    return emotions

if __name__ == '__main__':
    print(emotion_detector("I love this new technology"))
