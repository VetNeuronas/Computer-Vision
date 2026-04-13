def smart_home_action(user, emotion):
    print("\n🏠 Ajustando ambiente...")

    if user == "Desconocido":
        print("🔒 Usuario no reconocido. Activando modo seguro.")
        return

    print(f"👤 Bienvenido {user}")

    if emotion == "happy":
        print("🎵 Reproduciendo música alegre")
        print("💡 Luces brillantes")
    
    elif emotion == "sad":
        print("🎵 Música relajante")
        print("💡 Luces cálidas")
    
    elif emotion == "angry":
        print("🌿 Activando ambiente calmado")
        print("💡 Luces tenues")
    
    elif emotion == "surprise":
        print("🎉 Activando modo fiesta")
    
    else:
        print("⚙️ Ajuste estándar del hogar")