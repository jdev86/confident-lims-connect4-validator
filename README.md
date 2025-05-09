Confident Lims Connect 4 Validator

### Tools used:
Flask

Install Dependencies:
```
pip3 install -r requirements.txt
```

To run project:
```
python3 run.py
```

Some test objects:
Invalid placement:
```
{
    "board": [
        [1, 2, 1, 2, 0, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 0]
    ]
}
```
Invalid winner(simultaneous):
```
{
    "board": [
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2]
    ]
}
```