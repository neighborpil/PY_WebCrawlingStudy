import xml.etree.ElementTree as ET
data = """<person>
    <name>Chuck</name>
    <phone type='intl'> +1 456 212 321</phone>
    <email hide='yes' />
</person>"""

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) # text 추출
print('Attr:', tree.find('email').get('hide')) # 속성 추출