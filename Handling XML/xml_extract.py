import xml.etree.ElementTree as ET

def safe_text(elem):
    return elem.text if elem is not None else 'N/A'

tree = ET.parse("books.xml")
root = tree.getroot()

for book in root.findall('book'):
    title = safe_text(book.find('title'))
    author = safe_text(book.find('author'))
    genere = safe_text(book.find('genere'))

    print(f"Title: {title}, Author: {author}, Genere: {genere}")




