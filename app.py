from flask import Flask, request
import pyjdb

app = Flask(__name__)


@app.route("/")
def hello_world():
    sql = request.args.get("sql", "")
    result = pyjdb.run(sql)
    return f"""
    <html>
        <head>
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css">
        </head>
        <body>
            <h1>PyjDb</h1>
            <form method='get' onchange='this.submit()'>
                <textarea name='sql'>{sql}</textarea>
                <button type='submit'>Run</button>
            </form>
            <hr>
            <pre>{result}</pre>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
