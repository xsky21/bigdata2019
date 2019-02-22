from xml.etree.ElementTree import Element,dump,SubElement

note = Element('note')
to = Element('to') #자식 노드
to.text = "Tove"

note.append(to)
SubElement(note,"from_tag").text="Jani"
dump(note)

note.attrib["date"] = "20120104" #부모 태그에 속성을 준다

dump(note)

