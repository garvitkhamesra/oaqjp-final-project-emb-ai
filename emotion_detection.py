import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)
    
    # Check for a successful response from the API
    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_json = response.json()
    
    # Extract emotion scores from the nested JSON structure
    try:
        emotion_predictions = response_json['emotionPredictions'][0]['emotion']
        
        # Get individual emotion scores, defaulting to 0 if an emotion is missing
        anger_score = emotion_predictions.get('anger', 0)
        disgust_score = emotion_predictions.get('disgust', 0)
        fear_score = emotion_predictions.get('fear', 0)
        joy_score = emotion_predictions.get('joy', 0)
        sadness_score = emotion_predictions.get('sadness', 0)
        
        # Create a dictionary of emotions and their scores
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        # Find the emotion with the highest score
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return the final formatted dictionary
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    except (KeyError, IndexError) as e:
        print(f"Error parsing response JSON: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

if __name__ == "__main__":
    test_text_joy = "I love this new technology."
    result_joy = emotion_detector(test_text_joy)
    print("Emotion Detection Result for 'I love this new technology.':", result_joy)

    test_text_anger = "I am so happy I am doing this."
    result_anger = emotion_detector(test_text_anger)
    print("Emotion Detection Result for 'I am so happy I am doing this.':", result_anger)

