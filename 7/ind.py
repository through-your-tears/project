from xml.etree import ElementTree as et


PATH = '17.osm'


def main():
    with open(PATH, 'r', encoding='utf-8') as file:
        data = file.readlines()
    root = et.fromstringlist(data)
    schools = []
    for appt in list(root):
        f = False
        for elem in list(appt):
            if elem.tag == 'tag':
                if (elem.get('k') == 'amenity' or elem.get('k') == 'building') and elem.get('v') == 'school':
                    f = True
                if elem.get('k') == 'official_name' and f:
                    schools.append(elem.get('v'))
    print(len(schools))
    print(*schools, sep='\n')


if __name__ == '__main__':
    main()
