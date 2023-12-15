from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
import openai
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import json



app = Flask(__name__)

secret = secrets.token_urlsafe(32)
app.secret_key = secret  # set the secret key




# This function checks if the user is logged in


@app.route('/', methods=['GET', 'POST'])
def index():
    result=None
    if request.method == 'POST':
        essayLength = request.form['essayLength']
        essayQuality = request.form['essayQuality']
        essayTopic = request.form['essayTopic']

        client = openai.OpenAI(api_key='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')
     
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=0,
            max_tokens=1000,
            messages=[
                    {"role": "system", "content": f"You are a Writing Wizard who writes essays precisely of {essayLength} size or length and of {essayQuality} quality focused totally on the topic, finally be friendly with the user and do your job as perfectly as possible, Seperate the essay completely from your wizard intro, Be unbiased."},
               { "role": "user", "content":  essayTopic},
            ]
        )
        result = response.choices[0].message.content
        

    return render_template('index.html', result=result)

