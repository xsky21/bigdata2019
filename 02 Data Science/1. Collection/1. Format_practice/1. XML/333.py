from xml.etree.ElementTree import parse, dump
tree = parse("note.xml")
note = tree.getroot() #최상위 노드를 가져온다는 뜻
# from_tag = note.find("from") # from이란 이름의 하위 태그를 리턴
# #print(from_tag)
# from_tags = note.findall("from")
# # for a in from_tags:
# #     dump(a)
# # print(from_tags)
# # print(note.findtext("from"))
childs = note.iter()
for k in childs:
    dump(k)
