from xml.etree.ElementTree import ElementTree
tree = ElementTree()

root = tree.parse('''C:\classes\myWorld\world.xml''')
root = root
for assetType in root.findall(""):
    for type in assetType.getchildren("world"):
        print(type.text)