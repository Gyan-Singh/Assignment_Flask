import openai
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def customer():
    return render_template('index.html')

@app.route('/success', methods=['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result1 = {}
        result = request.form
        try:
            openai.api_key = "sk-.."
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": result['Query']}]
            )
            if completion.choices and completion.choices[0].message:
                mytext = completion.choices[0].message.content
            else:
                mytext = "No response from the API"
            
            result1['Query'] = result['Query']
            result1['Result'] = mytext
            return render_template("result_data.html", result=result1)
        
        except openai.OpenAIError as e:
            error_message = str(e)
            return render_template('fail.html')

    else:
        return render_template('fail.html')

if __name__ == '__main__':
    app.run(debug=True)
