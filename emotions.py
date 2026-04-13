from deepface import DeepFace

def analyze_emotion(img_path):
    try:
        result = DeepFace.analyze(img_path=img_path, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except:
        return "unknown"