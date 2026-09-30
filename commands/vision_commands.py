import cv2
import os
import base64
from core.state import state
import openai

def analyze_vision(command):
    state.emit("system", "👁️ Opening Eye of Vitus...")
    
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "I cannot access the camera."
        
    state.emit("system", "📸 Taking photo...")
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        return "Failed to capture an image."
        
    # Save image
    img_path = os.path.join(os.path.dirname(__file__), "..", "data", "vision.jpg")
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    cv2.imwrite(img_path, frame)
    
    # Encode to base64
    with open(img_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
    state.emit("system", "🧠 Analyzing image with Vision AI...")
    
    # Call Groq Vision API
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "I need a Groq API key to use computer vision."
        
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    try:
        response = client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe what you see in this image in one short sentence."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Vision error: {e}"
