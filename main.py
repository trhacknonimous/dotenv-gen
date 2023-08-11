#!venv/bin/python3
from flask import Flask, render_template, request
import json
from colorama import Fore, Style

app = Flask(__name__)

# Fonction pour afficher le texte en couleurs arc-en-ciel
def display_rainbow_text(text):
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    reset_color = Fore.RESET
    rainbow_text = ""
    for i, char in enumerate(text):
        rainbow_text += rainbow_colors[i % len(rainbow_colors)] + char
    rainbow_text += reset_color
    return rainbow_text

# Fonction pour générer un fichier .env à partir d'un texte JSON
def generate_env_from_json(json_text):
    env_data = json.loads(json_text)
    env_lines = [f'{key}={value}' for key, value in env_data.items()]
    return '\n'.join(env_lines)

# Fonction pour générer un texte JSON à partir d'un fichier .env
def generate_json_from_env(env_text):
    env_lines = env_text.strip().split('\n')
    env_data = {}
    for line in env_lines:
        key, value = line.split('=', 1)
        env_data[key] = value
    return json.dumps(env_data, indent=2)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        input_text = request.form['inputText']
        action = request.form['action']
        result = ""

        if action == 'generate_env':
            result = generate_env_from_json(input_text)
        elif action == 'generate_json':
            result = generate_json_from_env(input_text)

        return render_template('index.html', result=result, input_text=input_text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)