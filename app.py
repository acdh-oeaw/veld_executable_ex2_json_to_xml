import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import json


file_path_input = "/veld/input/data.json"
file_path_output = "/veld/output/data.xml"


def dict_to_xml(d, node_current=None):
    if node_current is None:
        node_current = ET.Element("root")
    for k,v in d.items():
        node_k = ET.Element(k)
        if type(v) is dict:
            dict_to_xml(v, node_k)
        elif type(v) is list:
            for lv in v:
                li = ET.Element("li")
                li.text = lv
                node_k.append(li)
        else:
            node_k.text = str(v)
        node_current.append(node_k)
    return node_current


try:
    with open(file_path_input, "r") as fi:
        d = json.load(fi)
        print(d)
except:
    print("file not found")
else:
    xml_root = dict_to_xml(d)
    xml_str = minidom.parseString(ET.tostring(xml_root)).toprettyxml(indent="  ")
    with open(file_path_output, "w") as fo:
        fo.write(xml_str)
