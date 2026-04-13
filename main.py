import cv2
from src.recognition import recognize_face
from src.emotions import analyze_emotion
from src.actions import smart_home_action

def capture_image():
    cap = cv2.VideoCapture(0)
    
    print("📸 Presiona 's' para capturar imagen")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_path = "captured.jpg"
            cv2.imwrite(img_path, frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    return img_path


def main():
    img_path = capture_image()

    print("\n🔍 Analizando usuario...")
    
    user = recognize_face(img_path)
    emotion = analyze_emotion(img_path)

    print(f"\n👤 Usuario: {user}")
    print(f"😊 Emoción: {emotion}")

    smart_home_action(user, emotion)


if __name__ == "__main__":
    main()