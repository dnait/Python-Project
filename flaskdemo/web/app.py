
from flask import Flask, Response, render_template

app = Flask(__name__)

# @app.route("/")
# def hello():
    # return '''
    #     <html><body>
    #     Hello. <a href="/getPlotCSV">Click me.</a>
    #     </body></html>
    #     '''
# @app.route('/')
# def index():
#    return render_template(‘hello.html’)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name=user)

@app.route("/getPlotCSV/<user>")
def getPlotCSV(user):
    # filename = "my.log"
    with open("/Users/grace/rentlist.csv") as fp:
        log_file = fp.read()
    # csv = '1,2,3\n4,5,6\n'
    return Response(
        log_file,
        mimetype="text",
        headers={"Content-disposition":
                 "attachment; filename=%s" % user})


if __name__== "__main__":
    app.run(debug=True)