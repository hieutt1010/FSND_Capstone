### Endpoint for /Movies

`GET '/actors'`
- Fetches a list of actors
- Request Arguments: None
- Returns: list of actors contain id, title, release_date

```json
{
  {
    "id": 1,
    "title": "Inception",
    "release_date": "2010-07-16"
  },
  {
    "id": 2,
    "title": "The Dark Knight",
    "release_date": "2008-07-18"
  },
  {
    "id": 3,
    "title": "Interstellar",
    "release_date": "2014-11-07"
  }
}
```

`GET/movies/<int:id>`
- Get a special movie by id
- Request Arguments: `id` - integer
- Returns: a movie object
``` json
{
  "id": 1,
  "title": "Inception",
  "release_date": "2024-07-16"
}
```

`POST/movies`
- This endpoint creates a new movie
- Request Body:
```json
{
    "title": "Dunkirk",
    "release_date": "2024-07-21"
},
```

- Returns: a single new movie object and message-status
```json
{
    {
        "title": "Dunkirk",
        "release_date": "2024-07-21"
    },
    "message": True
}
```

`PATCH/movies/<int:id>`
- This endpoint updates the information of an existing movie by `id`
- Request Body:
```json
{
  "title": "Dunkirk (Updated)",
  "release_date": "2017-07-22"
}
```
- Returns: a single movie object after update and message-status
```json
{
    {
        "title": "Dunkirk",
        "release_date": "2024-07-21"
    },
    "message": True
}
```

`DELETE/movies/<int:id>`
- This endpoint deletes a movie by `id`
- Request Arguments: `id` - integer
- Returns: a single movie object deleted and message-status
```json
{
    {
        "title": "Dunkirk",
        "release_date": "2024-07-21"
    },
    "message": True,
}
```

### Endpoint for /Actors

`GET '/actors'`
- Fetches a list of actors
- Request Arguments: None
- Returns: list of actors contain id, name, age, gender, movie_id, movie

```json
{
  "actors": [
    {
      "id": 1,
      "name": "Leonardo DiCaprio",
      "age": 45,
      "gender": "Male",
      "movie_id": "1",
      "movie": {
        "id": 1,
        "title": "Inception",
        "release_date": "2010-07-16"
      }
    },
    {
      "id": 2,
      "name": "Natalie Portman",
      "age": 39,
      "gender": "Female",
      "movie_id": "1",
      "movie": {
        "id": 2,
        "title": "Black Swan",
        "release_date": "2010-12-03"
      }
    }
  ]
}

```

`GET/actors/<int:id>`
- Get a special actor by id
- Request Arguments: `id` - integer
- Returns: a actor object
``` json
{
    "id": 2,
    "name": "Natalie Portman",
    "age": 39,
    "gender": "Female",
    "movie_id": "1",
    "movie": {
    "id": 2,
    "title": "Black Swan",
    "release_date": "2010-12-03"
    }
}
```

`POST/actors`
- This endpoint creates a new actor
- Request Body:
```json
{
  "name": "Brad Pitt",
  "age": 56,
  "gender": "Male",
  "movie_id": 1 
}
```

- Returns: a single new actor object and message-status
```json
{
    "message": True,
    "actor": {
        "id": 3,
        "name": "Brad Pitt",
        "age": 56,
        "gender": "Male",
        "movie": {
        "id": 1,
        "title": "Inception",
        "release_date": "2010-07-16"
        }
    }
}
```

`PATCH/actors/<int:id>`
- This endpoint updates the information of an existing actor by `id`
- Request Body:
```json
{
  "name": "Leonardo DiCaprio (Updated)",
  "age": 46,
  "gender": "Male",
  "movie_id": 2
}

```
- Returns: a single actor object after update and message-status
```json
{
  "actor": {
    "id": 1,
    "name": "Leonardo DiCaprio (Updated)",
    "age": 46,
    "gender": "Male",
    "movie": {
      "id": 2,
      "title": "The Revenant",
      "release_date": "2015-12-25"
    }
  },
  "message": true
}
```

`DELETE/actor/<int:id>`
- This endpoint deletes a actor by `id`
- Request Arguments: `id` - integer
- Returns: a single actor object deleted and message-status
```json
{
  "actor": {
    "id": 1,
    "name": "Leonardo DiCaprio (Updated)",
    "age": 46,
    "gender": "Male",
    "movie": {
      "id": 2,
      "title": "The Revenant",
      "release_date": "2015-12-25"
    }
  },
  "message": true
}
```