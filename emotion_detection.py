import requests, json

def emotion_detector(text_to_analyse):
    # URL to send the request to
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Custom headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Sending POST request with headers and JSON data
    response = requests.post(url, headers=headers, json=data)
     # Parse the JSON string
    parsed_data = json.loads(response.text)
    
    # Print parsed data
    #print(json.dumps(parsed_data, indent=4))

    # Find the emotion with the highest value
    highest_emotion = None
    highest_value = 0
    
    for prediction in parsed_data['emotionPredictions']:
        emotions = prediction['emotion']
        for emotion, value in emotions.items():
            if value > highest_value:
                highest_value = value
                highest_emotion = emotion
    
    #print(f"Highest emotion: {highest_emotion} with value {highest_value}")
    emotions['dominant_emotion']=highest_emotion
    return json.dumps(emotions, indent=4)
