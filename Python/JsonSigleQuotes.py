import json

# JSON formed String variables
json_with_double_quotes = '{"Name": "Jin"}'
json_with_single_quotes = "{'Name': 'Jin'}"

# (1) It works.
json.loads(json_with_double_quotes)

# (2) It doesn't work. Because It is expressed by double quotes.
# json.loads(json_with_single_quotes)

# solution: Alternative way to convert from Single Quotes JSON to DICT
import ast
dict_with_single_quotes = ast.literal_eval(json_with_single_quotes)

# Tranform from JSON with single quotes to double-quotes.
json.dumps(dict_with_single_quotes)
