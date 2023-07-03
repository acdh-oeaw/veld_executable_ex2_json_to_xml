import xml.etree.ElementTree as ET
import json


file_path_input = "/veld/input/data.json"
file_path_output = "/veld/output/data.xml"

try:
    with open(file_path_input, "r") as f:
        d = json.load(f)
        print(d)
except:
    print("file not found")
