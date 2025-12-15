import gradio as gr
import requests

API_URL = "https://mlopdock-latest.onrender.com"

def predict_image(file):
    try:
        if hasattr(file, "name"):
            path = file.name
        elif isinstance(file, str):
            path = file
        else:
            # If it's a numpy array or PIL image, save temporarily
            from PIL import Image
            import numpy as np, tempfile
            if isinstance(file, np.ndarray):
                img = Image.fromarray(file.astype("uint8"))
            else:
                img = file
            tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
            img.save(tmp.name)
            path = tmp.name

        with open(path, "rb") as f:
            files = {"file": ("image.jpg", f, "image/jpeg")}
            response = requests.post(f"{API_URL}/predict", files=files, timeout=10)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}


iface = gr.Interface(
    fn=predict_image,
    inputs=gr.File(file_types=[".png", ".jpg", ".jpeg"]),
    outputs=gr.JSON(),
    title="Random Image Classifier",
    description="Upload an image and get a random prediction from the API."
)

if __name__ == "__main__":
    iface.launch()
