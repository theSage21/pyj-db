import json


def make_ast(sql):
    """
    Turn a given sql query into an abstract syntax tree so that calculations
    can be done on top of it.
    """
    fn, _ = sql.lower().split(" ", 1)
    if fn == "select":
        assert "from" not in sql.lower(), "Not yet supported"
        # TODO: Support 'from' in select clause
        _, columns = sql.split(" ", 1)
        columns = columns.split(",")
        ast = {"fn": "select", "columns": []}
        for index, col in enumerate(columns, start=1):
            # TODO: Expand code into tuple of [op, arg1, arg2] like ['+', 23, 44]
            ast["columns"].append({"code": col.strip(), "name": f"col_{index}"})
        return ast
    # TODO: Implement create table function

    # --- something that we don't support was provided
    return None


def run(sql):
    ast = make_ast(sql)
    return json.dumps({"AST": ast}, indent=2)
