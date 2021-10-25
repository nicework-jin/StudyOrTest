import json

# JSON formed String variables
json_with_double_quotes = '{"Name": "Jin"}'
json_with_single_quotes = "{'Name': 'Jin'}"

# (1) It works.
r = json.loads(json_with_double_quotes)

# (2) It doesn't work. Because It is expressed by double quotes.
r = json.loads(json_with_single_quotes)

# (2-solution) Alternative way to convert from Single Quotes JSON to DICT
import ast

r = ast.literal_eval(json_with_single_quotes)


