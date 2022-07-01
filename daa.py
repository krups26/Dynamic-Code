from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def daa():
    data = request.form
    print(data)
    return render_template ("daa.html")

@app.route("/dtp", methods=['GET', 'POST'])
def dtp():
    data = request.form
    print(data)
    return render_template ("dtp.html")

# @app.route('/')
# def daa(tata):
#     return render_template ("daa.html" , name=tata)

# @app.route('/<temp>/')
# def dtp(temp):
#     return render_template ("dtp.html" , name=temp)

#@app.route('/test', methods=['GET'])

#def dropdown():
    #colours = ['DTP', 'DHEP', 'ASET', 'DCS', 'DAA']
    
    #return render_template('test.html', colours=colours)    

#@app.route('/<tata>/')
#def daa(tata):
    #return render_template ("daa.html" , name=tata)

app.run(debug=True)