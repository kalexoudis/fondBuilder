from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit_selection', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        return redirect('/thankyou.html')
    else:
        return 'wrong'



if __name__ == '__main__':
    app.run()
