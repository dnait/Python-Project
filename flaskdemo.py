#!/usr/bin/python

from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <html><body>
        Hello. <a href="/getPlotCSV">Click me.</a>
        </body></html>
        '''

@app.route("/getPlotCSV")
def getPlotCSV():
    filename = "my.log"
    with open("/Users/grace/rentlist.csv") as fp:
        log_file = fp.read()
    # csv = '1,2,3\n4,5,6\n'
    return Response(
        log_file,
        mimetype="text",
        headers={"Content-disposition":
                 "attachment; filename=%s" % filename})


if __name__== "__main__":
    app.run(debug=True)
