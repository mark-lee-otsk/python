import re

def tables_in_query(sql_str):

    sql_str = f'''
      SELECT a 
           , B
           , C, D
      FROM A.BBBB, C.XXXX
      WHERE A.B = C.B
      '''

    #remove th /* */ comments
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/","", sql_str)


    #remove wole line -- and # comments
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]
   


    # remove trailing -- and # comments
    q = " ".join([re.split("--|#", line)[0] for line in lines])


    #re.split(r"[\s)(,;]+", q)
    #split on blanks, parens and semicolons
    tokens = re.split(r"[\s)(;]+", q)
 

    #sacn the tokens. if we see a FROM or JOIN, we set the get_next
    #flag, and grab the next one (unless it's SELECT).

    result = set()
    get_next = False

    for tok in tokens:
        if get_next:
            if tok.lower() not in ["", "select"]:
                result.add(tok)
            get_next = False
        get_next = tok.lower() in ["from", "join"]      

    return result

def fn_queryString():
    returnVal = 'SELECT X.B FROM X X'
    return returnVal

print(tables_in_query('select a from BBBB'))