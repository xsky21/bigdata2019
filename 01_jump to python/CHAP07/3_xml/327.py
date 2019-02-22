from xml.etree.ElementTree import Element,dump

note = Element('note') #element는 태그를 생성하는 메서드인듯?
to = Element('to')
to.text = "Tove"

note.append(to) #여기선 append가 상위 하위를 가려준다.
dump(note) #note 하위에 있는 모든 정보를 보여준다.
dump(to)

