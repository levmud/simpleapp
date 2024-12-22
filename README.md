# simpleapp
homework on the development infrastructure

### Docker

```$ docker build -t simpleapp . ```

``` $ docker run -d --name fastapi-app -p 8000:8000 simpleapp ```

### Запросы

POST
```
curl -X 'POST' \
  'http://localhost:8000/user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "mudrovlev17@gmail.com",
  "name": "Lev",
  "surname": "Mudrov",
  "patronymic": "Leonidovich"
}'
```
GET
```
curl -X 'GET' \
  'http://localhost:8000/user/mudrovlev17%40gmail.com' \
  -H 'accept: application/json'
```
  
