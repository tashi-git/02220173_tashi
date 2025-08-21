import json
from jsonschema import validate,ValidationError

with open('books.json') as file:
    books = json.load(file)

print(books)

schema = {
  "title": "Books",
  "description": "A collection of books",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "description": "Unique identifier for the book"
      },

      "title": {
        "type": "string",
        "description": "Title of the book"
      },
      "author": {
        "type": "string",
        "description": "Author of the book"
      },
      "genre": {
        "type": "string",
        "description": "Genre of the book"
      }
    },
    "required": ["id", "title", "author", "genre"],
  }
}

try:
    validate(instance=books, schema=schema)
    print("JSON is valid")
except ValidationError:
    print("JSON is invalid")