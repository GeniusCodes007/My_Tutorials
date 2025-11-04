
from fastapi import FastAPI

app = FastAPI()

@app.get("/SQL Infos")
def SQL_Facts():
    response = [f"When using the SQL commands, it is recommended to use them in upper case",
                f"SQL syntaxes and Explanations",

    ]
    return response

@app.get("/additional SQL Info")
def additional_SQL_Info():
    response = {
        "SELECT * FROM 'table_name'":   "This line extracts information from all columns in the table" ,
        "SELECT \"column_1\", \"column_2\", \"column_3\" and so on FROM 'table_name'":
                        "This line extracts information from the columns respectively. "
                        "The order of columns need not be written in the order of appearance.",
        "The Use of Operators": "The Use of Operators in SQL",
        "SELECT * FROM 'table_name' WHERE 'condition_column' = 'condition'":
                        "This line extracts information from the row(s), "
                        "whose column meets the condition of the 'condition-column'",
        "SELECT \"column_1\", \"column_2\", \"column_3\" and so on FROM 'table_name' WHERE 'condition_column' = 'condition'":
                        "Similar to the third condition",
        "Nota Bene": "The above principle or pattern applies to the operators: '<', '>', '<=', and '>=', all in the same way",
        "Not in SQL": ["This has two syntaxes:",
                                   {
                                       "-> SELECT \"column_1\", \"column_2\", \"column_3\" and so on FROM 'table_name' WHERE 'condition_column' != 'condition'": "Syntax One",
                                        "-> SELECT \"column_1\", \"column_2\", \"column_3\" and so on FROM 'table_name' WHERE 'condition_column' <> 'condition'": "Syntax Two"
                                   }
                                   ],
        "SELECT \"column_1\" AS \"preferred_column_name_1\", \"column_2\" AS \"preferred_column_name_2\", and so on FROM 'table_name'":
                        "This Line extracts information from the column specified [i.e. column_1 or column_2], and displays it in a column with name"
                        "'preferred_column_name_1' or 'preferred_column_name_2', depends on the user.",
        "SELECT * FROM 'table_name' ORDER BY 'column_name'":
                        "This line presents information in table_name in the "
                        "ascending order of the values of column_name",
        "SELECT * FROM 'table_name' ORDER BY 'column_name' ASC":
                        "The same as 'SELECT * FROM 'table_name' ORDER BY 'column_name'",
        "SELECT * FROM 'table_name' ORDER BY 'column_name DESC'":
                        "This line does the direct opposite of "
                        "SELECT * FROM 'table_name' ORDER BY 'column_name'",
        "The LIMIT keyword": "The Limit keyword displays the first number of lines"
                             " [as specified by the Limit]"
                             "of records that meet the condition of the statement "
                             "before the LIMIT declaration. For instance, "
                             "a user runs the query command 'SELECT * FROM 'table_name "
                             "ORDER BY 'column_name' LIMIT 3'. This instance displays "
                             "the first 3 rows of information from the output of the"
                             " part of the statement before 'LIMIT 3'",
        "The OFFSET keyword": "The OFFSET keyword skips the first number of lines"
                             " [as specified by the OFFSET]"
                             "of records that meet the condition of the statement "
                             "before the OFFSET declaration. For instance, "
                             "a user runs the query command 'SELECT * FROM 'table_name "
                             "ORDER BY 'column_name' OFFSET 3'. This instance skips "
                             "the first 3 rows of information from the output of the"
                             " part of the statement before 'OFFSET 3'",
                }
    return response