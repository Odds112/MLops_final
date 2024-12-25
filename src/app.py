from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image

app = FastAPI()

model = tf.keras.models.load_model('model.h5')

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Читаем изображение
    img = Image.open(file.file).convert("L").resize((32, 32))  # Ч/б, размер 32x32
    img_array = np.array(img) / 255.0  # Нормализация
    img_array = np.expand_dims(img_array, axis=(0, -1))  # Добавляем батч и канал

    # Предсказание
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)

    return {"class": int(predicted_class), "confidence": float(confidence)}

@app.get("/health")
def health_check():
    return {"status": "ok"}
