import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import json
from prefect import flow


file_path_input = "./veld_data_ex1_json/data.json"
file_path_output = "./veld_data_ex2_xml/data.xml"


def dict_to_xml(d, node_current=None):
    if node_current is None:
        node_current = ET.Element("root")
    k_v_pairs = None
    if type(d) is dict:
        k_v_pairs = [(ET.Element(k), v) for k, v in d.items()]
    elif type(d) is list:
        k_v_pairs = [(ET.Element("li"), v) for v in d]
    for node_k, v in k_v_pairs:
        if type(v) is dict or type(v) is list:
            dict_to_xml(v, node_k)
        else:
            node_k.text = str(v)
        node_current.append(node_k)
    return node_current


@flow(name="veld_executable_ex2_json_to_xml__yaml__submodules", log_prints=True)
def convert():
    print("HIER")
    print("loading from:", file_path_input)
    with open(file_path_input, "r") as fi:
        d = json.load(fi)
        print("original json data:")
        print(d)
        xml_content = dict_to_xml(d)
        xml_str = minidom.parseString(ET.tostring(xml_content)).toprettyxml(indent="  ")
        print("converted xml data:")
        print(xml_str)
        print("writing to", file_path_output)
        with open(file_path_output, "w") as fo:
            fo.write(xml_str)


if __name__ == "__main__":
    convert()

