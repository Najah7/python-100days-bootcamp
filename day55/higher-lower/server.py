import random

from flask import Flask, render_template

app = Flask(__name__)

ANSWER = random.randint(0, 9)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/guess/<int:number>')
def guess(number):
    if number < ANSWER:
        return render_template('low.html', number=number)
    elif number > ANSWER:
        return render_template('high.html', number=number)
    else:
        return render_template('correct.html', number=number)
        
    


if __name__ == "__main__":
    
    app.run(debug=True)