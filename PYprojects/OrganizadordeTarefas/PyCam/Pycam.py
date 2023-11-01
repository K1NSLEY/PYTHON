import cv2
import pytesseract
from PIL import Image

# Configuração do pytesseract para o local do executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# URL da câmera HTTP
url = 'http://192.168.0.3:4747/video'

# Abre a conexão com a câmera
cap = cv2.VideoCapture(url)

while True:
    # Lê um frame da câmera
    ret, frame = cap.read()

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplica um filtro para melhorar o contraste (opcional)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Usa o pytesseract para realizar o OCR no frame
    text = pytesseract.image_to_string(Image.fromarray(gray))

    # Mostra o frame na janela
    cv2.imshow('Camera OCR', frame)

    # Imprime o texto reconhecido
    print("Texto reconhecido:", text)

    # Se a tecla 'q' for pressionada, encerra o loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
