from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/news', methods=['GET'])
def get_news():
    sample_news = [
        {'id': 1, 'title': 'Ultime novità sull\'AI', 'content': 'Contenuto dell\'articolo...'},
        {'id': 2, 'title': 'Scoperte rivoluzionarie', 'content': 'Contenuto dell\'articolo...'}
    ]
    return jsonify(sample_news)

if __name__ == '__main__':
    app.run(debug=True)
