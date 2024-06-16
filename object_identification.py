from tensorflow.keras.models import load_model
import numpy as np

# Carrega o modelo pré-treinado
model = load_model('path_to_your_model.h5')

# Função para processar a imagem e prever o item
def identify_item(image):
    # Preprocessa a imagem (redimensiona, normaliza, etc.)
    image_resized = cv2.resize(image, (224, 224)) / 255.0
    image_array = np.expand_dims(image_resized, axis=0)

    # Faz a previsão
    prediction = model.predict(image_array)
    return np.argmax(prediction, axis=1)[0]  # Assumimos que a saída é categórica

# Integração com a captura de vídeo
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Identifica itens na imagem
    item_id = identify_item(frame)

    # Se o item identificado for manteiga, realiza uma ação
    if item_id == BUTTER_CLASS_ID:  # Substitua pelo ID da classe manteiga
        print("Manteiga identificada!")

    # Mostra a imagem
    cv2.imshow('Item Identification', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
