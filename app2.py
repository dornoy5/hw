import json

json_name ="my_name.json"

with open(json_name) as json_name:
    data=json.load(json_name)

green_color = "\033[32m"
reset_color = "\033[0m"

print(f"{green_color}{data}{reset_color}")