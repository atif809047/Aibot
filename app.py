import os
from flask import Flask, render_template_string, request
import google.generativeai as genai

app = Flask(__name__)

# Aapki API Key yahan set ho gayi hai
GEMINI_API_KEY = "AIzaSyB7J5MF37uMS0liw5DhV3pNuHl-3M5lxkc"
genai.configure(api_key=GEMINI_API_KEY)

# Model configuration
model = genai.GenerativeModel('gemini-pro')

# Purane 2G browser ke liye ekdum basic HTML design
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Aibot - 2G Mode</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family:sans-serif; background-color:#e5e5e5; color:#000; padding:10px;">
    <div style="background-color:#0055ff; color:white; padding:5px; text-align:center;">
        <b>Aibot (Jio/Nokia Edition)</b>
    </div>
    <br>
    
    {% if reply %}
        <div style="background-color:white; border:1px solid #999; padding:8px; margin-bottom:15px;">
            <b style="color:#0055ff;">Aibot:</b><br>
            {{ reply }}
        </div>
    {% endif %}

    <form method="POST" action="/">
        <label><b>Sawal Likhein:</b></label><br>
        <input type="text" name="user_query" style="width:95%; border:1px solid #000; margin-top:5px;"><br><br>
        <input type="submit" value="Jawaab Paayein" style="background-color:#008000; color:white; font-weight:bold; padding:5px 15px;">
    </form>
    
    <br><hr>
    <div style="font-size:small; text-align:center;">
        Made by atif809047<br>
        Network: 2G/Low-End Friendly
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    reply = ""
    if request.method == 'POST':
        user_input = request.form.get('user_query')
        if user_input:
            try:
                # AI se response lena
                response = model.generate_content(user_input)
                reply = response.text
            except Exception as e:
                reply = "Maaf kijiyye, abhi AI kaam nahi kar raha. Network check karein."
    
    return render_template_string(HTML_TEMPLATE, reply=reply)

if __name__ == "__main__":
    # Port 5000 default hai
    app.run(host='0.0.0.0', port=5000)
