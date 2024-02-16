# Load model directly
import torch
from flask import Flask
from IPython.display import Audio
from transformers import (AutoModelForTextToSpectrogram, AutoProcessor,
                          SpeechT5HifiGan)

processor = AutoProcessor.from_pretrained("Ananie/japanes-tts")
model = AutoModelForTextToSpectrogram.from_pretrained("Ananie/japanes-tts")

vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

speaker_embeddings = torch.zeros(1, 512)  # use the same speaker embedding for all inputs

speaker_embeddings = torch.randn(1, 512)  # use the same speaker embedding for all inputs

inputs = processor(text="Kon'nichiwa, koreha tesutodesu", return_tensors="pt")

speech = model.generate(inputs["input_ids"], speaker_embeddings=speaker_embeddings, vocoder=vocoder)
speech.shape

speech = speech.squeeze().numpy()

my_audio = Audio(speech, rate=16000)

def getAudio(text):
    inputs = processor(text=text, return_tensors="pt")

    speech = model.generate(inputs["input_ids"], speaker_embeddings=speaker_embeddings, vocoder=vocoder)
    speech = speech.squeeze().numpy()

    return Audio(speech, rate=16000)._repr_html_()


app = Flask(__name__)

@app.route("/<text>")
def audio(text):
    return getAudio(text)