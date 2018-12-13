import xml.etree.ElementTree as ET

input = """<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x='8'>
            <id>004</id>
            <name>Cirl</name>
        </user>
    </users>
</stuff>"""

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') # users 안에 user로 이루어진 태그를 모두 찾는다 => 2개
print('User count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get('x'))
