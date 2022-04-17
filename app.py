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
            <hr>
            <h2>Examples</h2>
            <pre>
select 1 + 1
create table mytable x int, y string
insert into mytable (x, y) values (1, 'something')
select x, y from mytable
            </pre>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
