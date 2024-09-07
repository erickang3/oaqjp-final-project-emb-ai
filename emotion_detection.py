import requests

def emotion_detector(text_to_analyze):
    '''This function calls the Emotion Predict function and returns the response
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url=url, headers=header, json=input_json)
    return response.text
