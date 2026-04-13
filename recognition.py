from deepface import DeepFace

def recognize_face(img_path, db_path="data/"):
    try:
        result = DeepFace.find(img_path=img_path, db_path=db_path, enforce_detection=False)
        
        if len(result[0]) > 0:
            identity_path = result[0].iloc[0]['identity']
            name = identity_path.split("/")[-1].split(".")[0]
            return name
        else:
            return "Desconocido"
    except:
        return "Error"