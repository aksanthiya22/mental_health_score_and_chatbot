from flask import Flask, render_template, request, jsonify
import re
import random

app = Flask(__name__)

conversation_history = []

@app.route('/')
def home():
    return render_template('index1.html', conversation=conversation_history)

@app.route('/get_response', methods=['GET'])
def get_response():
    pattern = request.args.get('pattern')
    user_message = "You: " + pattern
    conversation_history.append(user_message)
    response = generate_answer(pattern)
    bot_message = "Bot: " + response
    conversation_history.append(bot_message)
    return jsonify({'response': bot_message})

def generate_answer(pattern): 
    text = []
    txt = re.sub('[^a-zA-Z\']', ' ', pattern)
    txt = txt.lower()
    txt = txt.split()
    txt = " ".join(txt)
    text.append(txt)
        
    x_test = tokenizer.texts_to_sequences(text)
    x_test = np.array(x_test).squeeze()
    x_test = pad_sequences([x_test], padding='post', maxlen=X.shape[1])
    y_pred = model.predict(x_test)
    y_pred = y_pred.argmax()
    tag = lbl_enc.inverse_transform([y_pred])[0]
    responses = df[df['tag'] == tag]['responses'].values[0]

    return random.choice(responses)

if __name__ == '__main__':
    app.run(debug=True)
