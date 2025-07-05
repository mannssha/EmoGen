from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)


model_name = "tiiuae/falcon-rw-1b"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

def generate_quote(emotion):
    prompt = f"Write a short motivational message for someone who is feeling {emotion}."
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=50, temperature=0.8, do_sample=True)
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    return text.replace(prompt, "").strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    if request.method == 'POST':
        emotion = request.form['emotion']
        quote = generate_quote(emotion)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
