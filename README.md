# Dynamic-Code
from flask import Flask,render_template,request  app = Flask(__name__)  @app.route("/", methods=['GET', 'POST']) def daa():     data = request.form     print(data)     return render_template ("daa.html")  @app.route("/dtp", methods=['GET', 'POST']) def dtp():     data = request.form     print(data)     return render_template ("dtp.html")  app.run(debug=True)
