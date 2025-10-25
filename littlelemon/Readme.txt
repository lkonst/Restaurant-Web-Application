1)
/api/menu-items/           (GET list, POST create)
/api/menu-items/<id>/      (GET detail, PUT/PATCH update, DELETE)

2) 
Endpoints to test (Menu Items)

A) List & Create

URL: http://127.0.0.1:8000/api/menu-items/
Methods: GET (list), POST (create)
Headers:

 Content-Type: application/json

 Accept: application/json

 Authorization: Token <token>

 POST body example (create):

{
  "title": "Baguette",
  "price": "2.00",
  "inventory": 110
}

Expected responses:

GET --> 200 OK with a JSON array of menu items
POST --> 201 Created with the created item, e.g.:
{
  "id": 15,
  "title": "Baguette",
  "price": "2.00",
  "inventory": 110
}

B) Retrieve / Update / Delete single item

URL (detail): http://127.0.0.1:8000/api/menu-items/<id>/
Methods:

GET (retrieve one)

PUT (full update)

PATCH (partial update)

DELETE (delete)

PUT example (replace item id=5):
PUT http://127.0.0.1:8000/api/menu-items/5/

{
  "id": 5,
  "title": "Ice Cream",
  "price": "9.00",
  "inventory": 11
}

PATCH example (partial update):
PATCH http://127.0.0.1:8000/api/menu-items/5/

{
  "price": "8.50"
}


DELETE example:
DELETE http://127.0.0.1:8000/api/menu-items/5/

Expected responses:

GET (detail) --> 200 OK with the item JSON
PUT/PATCH --> 200 OK (or 202/204 depending on config) with updated item
DELETE --> 204 No Content


3) 
Insomnia / Postman tips

Set the request Body to JSON and include the headers above.
Add an Authorization header with value Token <token>.
Verify status codes: 200/201 for success, 400/401/403 for errors.