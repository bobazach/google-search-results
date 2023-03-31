from flask import Flask, render_template, request, redirect, url_for, session
from bs4 import BeautifulSoup
import requests
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

def pyGoogleSearch(word):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    address = "https://www.google.com/search?q="
    URL = address + word
    result = requests.get(URL, headers=headers)

    soup = BeautifulSoup(result.content, 'html.parser')

    total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False)
    results_num = ''.join([num for num in total_results_text if num.isdigit()])
    return results_num

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_word = request.form['search']
        results = int(pyGoogleSearch(search_word))  # Convert the search results to an integer
        result_text = f"Total search results for '{search_word}': {results}"

        if 'results_list' not in session:
            session['results_list'] = []

        session['results_list'].append((results, search_word))
        session.modified = True

    return render_template('search.html')

@app.route('/clear', methods=['POST'])
def clear():
    session.pop('results_list', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
