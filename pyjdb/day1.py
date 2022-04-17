import json


def normalize_sql(sql):
    sql = sql.replace('"', "'")
    final = []
    for line in sql.split("\n"):
        for c in ",()":
            line = line.replace(c, f" {c} ")
        final.append(line.strip())
    return "\n".join(final)


def make_ast(sql):
    """
    Turn a given sql query into an abstract syntax tree so that calculations
    can be done on top of it.
    """
    fn, _ = sql.lower().split(" ", 1)
    AST = {"fn": fn}
    if fn == "select":
        # Table name
        _, tail = sql.split(" ", 1)
        columns = tail
        table = None
        if "from" in tail:
            columns, table = tail.split("from")
        # Columns
        columns = columns.split(",")
        AST["table"] = table
        AST["columns"] = []
        for index, col in enumerate(columns):
            AST["columns"].append(
                {
                    "index": index,
                    "name": f"col_{index+1}",
                    "code": col.strip(),
                }
            )
        return AST
    elif fn == "create":
        # Table name
        _, _, table, *tail = sql.split()
        AST["table"] = table
        # Columns
        columns = " ".join(tail).split(",")
        AST["columns"] = []
        for index, col in enumerate(columns):
            name, ty = col.replace("(", "").replace(")", "").split()
            AST["columns"].append({"index": index, "name": name, "type": ty})
        return AST
    elif fn == "insert":
        # Table name
        _, _, table, *tail = sql.split()
        AST["table"] = table
        stack = []
        is_header = True
        for tok in tail:
            if tok == "values":
                is_header = False
            else:
                stack.append(tok)
            buff = []
            while tok == ")" and stack[-1] != "(":
                if stack[-1] != ")":
                    buff.append(stack[-1])
                stack = stack[:-1]
            if buff:
                stack = stack[:-1]
                row = [i.strip() for i in " ".join(reversed(buff)).split(",")]
                AST["columns" if is_header else "values"] = row

        # Headers
        return AST

    # --- something that we don't support was provided
    return None


def run(sql):
    result = {}
    sql = normalize_sql(sql)
    result["sql"] = sql.strip().split("\n")
    result["sql"] = make_ast(sql) if sql.strip() else {}
    return json.dumps(result, indent=2)
