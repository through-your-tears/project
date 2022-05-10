from typing import List
from xml.dom import minidom as md


def export_to_xml(data: List, path: str):
    str_data = [[str(el) for el in row] for row in data]
    root = md.Document()
    doc = root.createElement('items')
    root.appendChild(doc)
    for row in str_data:
        song_child = root.createElement('song')
        song_child.setAttribute('id', row[0])
        song_child.setAttribute('name', row[1])
        song_child.setAttribute('length', row[2])
        song_child.setAttribute('artist_id', row[3])
        song_child.setAttribute('album_id', row[4])
        doc.appendChild(song_child)
    xml_str = root.toprettyxml()
    with open(path, 'w+') as f:
        f.write(xml_str)


def import_from_xml(path: str):
    with open(path, 'r') as f:
        xml_data = f.read()
    xmlparse = md.parseString(xml_data)
    songs = xmlparse.getElementsByTagName('song')
    data = []
    for song in songs:
        row = [song.getAttribute('id'), song.getAttribute('name'), song.getAttribute('length'),
               song.getAttribute('artist_id'), song.getAttribute('album_id')]
        data.append(row)
    return data

