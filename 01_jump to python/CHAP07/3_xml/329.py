from xml.etree.ElementTree import Element,dump,SubElement

note = Element('note')
to = Element('to') #자식 노드
to.text = "Tove"

note.append(to)
SubElement(note,"from_tag").text="Jani" #SubElement는 어떤 태그를 만드는 동시에 자식노드를 추가한다.
                                      # note라는 태그 밑에 from이라는 이름의 자식노드를 추가하고, Jani라는 택트를 추가한다.
                                      # append를 활용하는 것과 동일한 결과
dump(note)
dummy = Element("dummy")
note.insert(1,dummy) #자식노드를 자리를 정해서 추가한다
                     #태그에 값이 없으면 <tag />라는 형식으로 나온다
dump(note)
note.remove(dummy) #노드를 삭제한다.이때 부모노드를 기준으로 찾아들어간다.
dump(note)
