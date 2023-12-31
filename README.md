# Fintel-Wrapper
This project is a wrapper written in python for the [Fintel API](https://developers.fintel.io/).  Currently, the wrapper supports retrieval
of **short** and **ownership** data.

## Download
To download the latest version from GitHub:
```bash
git clone https://github.com/MaxwellsPi/Fintel-Wrap
```

## API Authorization
For the wrapper to operate, you must have an active subscription and API key.  In addition, it is required that you set 
your key as an environmental variable to authorize your API access.  To set your environmental variable you can execute 
one of the following:

**Linux OS**
```bash
FINTEL-KEY='YOUR_KEY'
```

**Windows OS**
```bash
set FINTEL-KEY YOUR_KEY
```

## Retrieve Data

### Get Shorts
To retrieve shorts from the api, you can use the ```fintel.data.get_shorts()``` function:
```python
from fintel import data
df = data.get_shorts(['tsla', 'aapl'])
```

### Get Ownership
To retrieve ownership data from the api, you can use the ```fintel.data.get_ownership()``` function:
```python
from fintel import data
df = data.get_ownership(['tsla', 'aapl'])
```

# Example
<img title="a title" alt="Alt text" src="C:\Users\Edgar\Desktop\shorts-example.png" width="2048">
