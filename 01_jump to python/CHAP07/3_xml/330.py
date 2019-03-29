from xml.etree.ElementTree import Element, SubElement, dump, ElementTree

note = Element("note")
note.attrib["date"] = "20120104"
note.attrib["name"] = "코난"
note.attrib["sex"] = "남성"
to = Element("to")
to.text = "Tove"
note.append(to)
SubElement(note,"from").text="Jani"
SubElement(note,"heading").text="Reminder"
SubElement(note,"body").text="Don't forget me this weekend!"
dump(note)
ElementTree(note).write("note.xml", encoding='utf-8')

