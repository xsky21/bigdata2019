from xml.etree.ElementTree import Element,dump,SubElement

note = Element('note', date="20120104", to = "Tove") #attrib를 써서 속성을 추가하는 것과 같은 결과가 나온다
#to = Element('to') #자식 노드

SubElement(note,"from_tag").text="Jani"
dump(note)


