# What is a REST API?

-   Is a way of thinking about how a web server responds to your requests
-   It doesn't respond with just date, it responds with resources

## What are Resources?

-   Similar to OOP. Can think of resources kind of like objects
-   Think of server as having resources, and each is able to interact with the pertinent request

## Key Feature of REST: Stateless

-   Stateless: One request cannot depend on any other requests
-   The server only knows about the current request, and not any previous requests, i.e. the output depends only on the current request

### Example of Statelessness

`POST /item/chair` creates an item

-   The server does not know the item now exists. It simply creates that item, stores it in a database, and forgets about it.

`GET /item/chair` then goes to the database and checks to see if the item is there

-   To get an item, you do not need to have created an item before. The item could be in the database from something previous. This is because the server has no knowledge of anything that has happened before

### Another Example Regarding Statelessness and Log In Authentication

-   A user logs in to a web app
-   The web server does not know the user is logged in (since it does not remember any state)
-   This problem is solved using a key
-   The web app must end enough data to identify the user IN EVERY REQUEST, or else the server won't associate the request with that specific user
