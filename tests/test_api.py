import requests
from PIL import Image
import numpy as np

def test_predict():
    # Создаем тестовое изображение
    img = np.zeros((32, 32), dtype=np.uint8)
    img[10:20, 10:20] = 255  # Рисуем белый квадрат
    Image.fromarray(img).save("test_image.png")

    # Отправляем запрос
    with open("test_image.png", "rb") as f:
        response = requests.post("http://localhost:8000/predict/", files={"file": f})
    
    assert response.status_code == 200
    data = response.json()
    assert "class" in data and "confidence" in data
    print(data)

test_predict()
