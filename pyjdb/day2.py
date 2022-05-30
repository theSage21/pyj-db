from json import dumps, loads
from .day1 import run as getAst


def get_db():
    try:
        with open('db', 'r') as fl:
            db = loads(fl.read())
        return db
    except:
        return {'tables': {}, "values": {}}


def save_db(db):
    with open('db', 'w') as fl:
        fl.write(dumps(db, indent=2))


def createTable(table, columns=None, **kwargs):
    columns = [] if columns is None else columns
    db = get_db()
    if table in db['tables']:
        return 'ERR: Table already exists'
    db['tables'][table] = columns
    db['values'][table] = []
    save_db(db)


def insertTable(table, columns, values, **kwargs):
    db = get_db()

    if table not in db['tables']:
        return f"Err: Table not found '{table}'"

    schema = {colname['name'] for colname in db['tables'][table]}
    for column in columns:

        if column not in schema:
            return f"Err: {column} not available in schema"

    db['values'][table].append(values)
    save_db(db)


def selectTable(table, columns, **kwargs):
    db = get_db()
    if table not in db['tables']:
        return f"Err: Table not found '{table}'"
    rows = db['values']
    rows = dumps(rows, indent=2)
    return rows


def run(sql):

    a = getAst(sql)
    ast = loads(getAst(sql)).get("sql")
    # return a
    if ast.get('fn') == 'create':
        return createTable(**ast)
    elif ast.get('fn') == 'select':
        return selectTable(**ast)
    elif ast.get('fn') == 'insert':
        return insertTable(**ast)
    else:
        return 'This feature is not supported!!!!'
    return ast
