from flask import Flask

app = Flask(__name__)

@app.route('/') 
def hello_world():
    return '''
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Mi página</title>
</head>
<body>
    <h1>Mi saludo</h1>
    <p>Hola, mundo</p>
    
</body>
</html>
'''

#export FLASK_APP=hello.py escrito en el terminal nos mete el programa en una variable(flask espera esa variable)
#flask run la pone en marcha
