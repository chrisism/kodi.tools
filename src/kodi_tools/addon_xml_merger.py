import sys
from xml.etree import ElementTree

def merge_xml(addon_name:str, file_source:str, file_dest:str):
    addons_xml    = ElementTree.parse(file_dest)
    addons        = addons_xml.getroot()
    addon_in      = ElementTree.parse(file_source).getroot()

    nodes = addons.findall(f"addon[@id='{addon_name}']")

    for addon_node in nodes:
        addons.remove(addon_node)

    addons.append(addon_in)
    addons_xml.write(file_dest)

def main():
    addon_name = sys.argv[1]
    file_combined = sys.argv[2]
    file_source = sys.argv[3]

if __name__ == '__main__':
    main()