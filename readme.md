Simple django REST API for Android app that send emails and push notifications to remind you of yearly or one-time events, like birthdays or so on...

users/ GET COLECCTION; POST
users/:id /GET; PATCH; PUT; DELETE

```
user/:id/events/
{
    "id": 2345234523 // Normal
    "username": "Peter", // max 25
    "password": "1234", // normal password restrictions
    "email": "hiiampeter@peter.com" // email restrictions
    "fbcm_token": [<token>,...]  // string
}
```

```
user/:id/events/:eventId
{
    "id": 234223432 // Normal
    "title": "Grandma's Birthday" // max 50
    "description": "My favourite grandma deserve me to remember her birthday" // max 255
    "frequency" : "once" // once|yearly
    "date": "2017-06-06" // YYYY-MM-DD ISO-8601
}
```
