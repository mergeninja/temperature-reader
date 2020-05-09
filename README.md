# Simple Temperature Reader

## To run in debug:
```
  $ export FLASK_APP=app.py; python3 -m flask run
```

## To call the endpoints:
```
  $ curl http://localhost:5000/
  $ curl http://localhost:5000/temperatures
  $ curl -X POST  http://lcoalhost:5000/temperatures/store
```
