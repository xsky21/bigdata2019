from xml.etree.ElementTree import Element,dump,SubElement
note = Element('note')
to = Element('to') #자식 노드
to.text = "Tove"

note.append(to)
from_tag = SubElement(note,"from_tag")
from_tag.text="Jani" #SubElement는 어떤 태그를 만드는 동시에 자식노드를 추가한다.
# note라는 태그 밑에 from이라는 이름의 자식노드를 추가하고, Jani라는 택트를 추가한다.
# append를 활용하는 것과 동일한 결과
dump(note)

