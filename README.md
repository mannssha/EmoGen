# 🌟 Emotion-Based Motivation Generator using Falcon LLM

This is a web-based AI tool that generates motivational quotes based on your current emotional state using the Falcon RW-1B language model by TII-UAE. Whether you're feeling sad, anxious, or demotivated, this app will lift your spirits with custom motivational messages.

## 📌 Overview

- Takes an **emotion as input** (e.g., sad, tired, anxious)  
- Uses **Falcon-RW-1B LLM** via Hugging Face to generate motivational quotes  
- Built using **Flask** with a clean **HTML/CSS UI**  
- Lightweight and easy to run locally

## 🛠 Tech Stack

- Python (Flask)  
- Hugging Face Transformers  
- Falcon RW-1B model  
- PyTorch  
- HTML + CSS + Jinja2

## 📁 Project Structure

Emotion-Based-Motivation-Generator/
├── Emotion-Based-Motivation-Generator-using-Falcon-Language-Model/
│   ├── app.py  
│   ├── README.md  
│   └── templates/  
│       └── index.html

## ⚙️ How to Run

 

1. Navigate to the folder  
   `cd Emotion-Based-Motivation-Generator-using-Falcon-Language-Model`  
2. Install the requirements
   (optional requirements) 
   python -m venv venv
   venv\Scripts\activate  # on Windows
   pip install -r requirements.txt

   `pip install flask transformers torch`  
3. Run the app  
   `python app.py`  
4. Visit `http://127.0.0.1:5000` in your browser

## 💡 Example

Input: **overwhelmed**  
Output: _"You are capable of great things. Even in moments of doubt, your strength shines through."_

## 🔮 Future Enhancements

- Add speech-to-text emotion input  
- Support for multiple languages  
- Mobile responsive UI  
- Deploy on Render or Hugging Face Spaces  
- Option to get daily quotes via email

## 🧠 Model

Model used: `tiiuae/falcon-rw-1b`  
Provider: Hugging Face





