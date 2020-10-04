from flask import Flask, render_template, request, redirect
from ukro_g2p.predict import G2P

app = Flask(__name__)

# init g2p model
g2p = G2P('ukro-base-uncased')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        graphemes = request.form['graphemes']

        if graphemes:
            try:
                phonemes = g2p(graphemes, human_readable=True)
                phonemes = f"{' '.join(phonemes)}"

                return render_template('index.html', graphemes=graphemes, phonemes=phonemes)
            except:
                return 'There was an issue generating pronunciation for your word'
        else:
            return redirect('/')

    else:
        return render_template('index.html', g2p_result=None)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
