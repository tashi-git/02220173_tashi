import xml.etree.ElementTree as ET

tree = ET.parse("books.xml")
root = tree.getroot()

title_to_delete = input("Enter the title of the book to delete: ").strip()

found = False
for book in root.findall('book'):
    title = book.find('title')
    if title is not None and title.text == title_to_delete:
        root.remove(book)
        found = True
        print(f"Deleted book titled '{title_to_delete}'.")
        break

if not found:
    print(f"No book found with the title '{title_to_delete}'.")

tree.write("books.xml", encoding='utf-8', xml_declaration=True)
