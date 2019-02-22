from xml.etree.ElementTree import parse
tree = parse("note.xml")
note = tree.getroot() #최상위 노드를 가져온다는 뜻
print(note.get("date"))
print(note.get("foo","default"))
print(note.keys())
print(note.items())

