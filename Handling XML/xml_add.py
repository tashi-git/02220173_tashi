import xml.etree.ElementTree as ET

tree = ET.parse("books.xml")
root = tree.getroot()

new_book = ET.Element('book')


title = ET.SubElement(new_book, 'title')
title.text = input("Enter the title of the book: ").strip()

author = ET.SubElement(new_book, 'author')
author.text = input("Who is the author of the book: ").strip()

genre = ET.SubElement(new_book, 'genre')  
genre.text = input("What is the genere of the book: ").strip()

root.append(new_book)

# Save the modified XML to a new file or overwrite original
# tree.write('books_modified.xml', encoding='utf-8', xml_declaration=True)

tree.write('books.xml', encoding='utf-8', xml_declaration=True)