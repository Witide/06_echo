from flask import Flask, render_template, request

echo = Flask(__name__)

@echo.route("/")
def root():
    return render_template("form.html")
    
@echo.route("/echo", methods=['POST','GET'])
def echoResponse():
    print request.method
    print request.headers
    print request.form
    user_name = request.form["username"]
    method = request.method
    return render_template("echo.html", username=user_name, method_type=method)
    
if __name__ == "__main__":
    echo.debug = True
    echo.run()