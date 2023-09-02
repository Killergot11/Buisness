from flask import Flask, render_template, request
import algorithm
#import sidecode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_input']
    bot_response = algorithm.getBotResponce(user_message)
    return {'response': bot_response,'imageurl':algorithm.getBotImage(user_message),'vidurl':algorithm.getBotVid(user_message)};


if __name__ == '__main__':
    app.run(debug=True,port=3000)