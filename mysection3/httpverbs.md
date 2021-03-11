## What is a web server?

-   A piece of software designed to accept incoming web requests
-   Example: Google has many web servers. Whenever we go to google's website, we are sending something to one of google's web servers, and they can send something back

### What do we send to a web server?

-   When we go to http://www.google.com, we are sending:
    `GET / HTTP/1.1 Host: www.google.com`

Called a GET request:
`Get` is called the "Verb"
`/` is called the "Path"
`HTTP` is called the Protocol

All the servers are seeing the same piece of data coming in, a GET request.
The only difference is what the server on the other end responds with

-   Going to a page will always do a GET

# HTTP Verbs

| Verb   | Meaning                      | Example          |
| ------ | ---------------------------- | ---------------- |
| Get    | Retrieve Something           | `GET /item/1`    |
| POST   | Receive data and use it      | `POST /item`     |
| PUT    | Make sure something is there | `PUT /item`      |
| DELETE | Remove something             | `DELETE /item/1` |
