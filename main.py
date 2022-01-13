from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/",)
def index():
    return render_template('index.html')


@app.route("/form", methods=['GET', 'POST'])
def form():
    data = request.form.to_dict()
    print(data)
    resultado = data.values()
    resultado = list(resultado)
  
    return render_template('index.html', resultado=resultado) 

     
app.run(debug=True)