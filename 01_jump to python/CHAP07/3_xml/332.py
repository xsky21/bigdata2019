from xml.etree.ElementTree import parse,dump
tree = parse("note.xml")
note = tree.getroot() #최상위 노드를 가져온다는 뜻
dump(tree)
dump(note)
# print(note.get("date"))
# print(note.get("name"))
# print(note.keys())
# print(note.items())

