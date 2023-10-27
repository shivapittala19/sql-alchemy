# SetUp

### Clone the repo.
```
git clone  git@github.com:shivapittala19/sql-alchemy.git
```
### Create a virtual environment and activate it.
```
python3 -m venv sqlalchemy
```
```
source path/to/venv/bin/activate
```
### Navigate to the project directory.
```
cd sql-alchemy
```

### Install the requirements
```
pip install -r requirements.txt
```
## Run files
#### Create Tables
```
python3 models.py
```
#### Load the data
```
python3 load.py
```

To run the scripts:
* open python shell 
```
python3
```
* Import the class IPLdata from file views
```
from views import IPLdata
```
* Now we can call any function as per required to see the output
```
IPLdata.func_name()
```

