# Standvirtual Web scrapper

Web scrapper for the car sales website standvirtual.com, using the `requests` lib and `beautifulsoup` parser.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Modify the search string taken by the `search` function, using a `<brand>/<model>/<desde-YYYY>/` syntax. E.g.
```python
yaris = 'toyota/yaris/desde-2012/'

cars = search(yaris)
```

## License
[GPL 3.0](https://choosealicense.com/licenses/gpl-3.0/)