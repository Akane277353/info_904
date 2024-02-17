# Load model directly
import torch
from flask import Flask
from flask_cors import CORS
from IPython.display import Audio
from transformers import (AutoModelForTextToSpectrogram, AutoProcessor,
                          SpeechT5HifiGan)

processor = AutoProcessor.from_pretrained("Ananie/japanes-tts")
model = AutoModelForTextToSpectrogram.from_pretrained("Ananie/japanes-tts")

vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

speaker_embeddings = torch.zeros(1, 512)  # use the same speaker embedding for all inputs

speaker_embeddings = torch.randn(1, 512)  # use the same speaker embedding for all inputs


def getAudio(text):
    inputs = processor(text=text, return_tensors="pt")

    speech = model.generate(inputs["input_ids"], speaker_embeddings=speaker_embeddings, vocoder=vocoder)
    speech = speech.squeeze().numpy()

    return Audio(speech, rate=16000)._repr_html_()


app = Flask(__name__)
CORS(app)

@app.route("/<text>", methods=['GET'])
def audio(text):
    
    return getAudio(text)


if __name__ == "__main__":
    app.run(debug=True, port=5000)