# Sample Calendar Application


## run: `virtualenv venv --python=python3.7` 

## run: `source venv/bin/activate`

## run: `pip3 install -r requirements.txt`

## run: `export FLASK_APP=interview.py`

## run: `flask run`

## hit: `http://127.0.0.1:5000/` to ensure it is running

## hit: `http://127.0.0.1:5000/add-interview` with sample data: 
``
{
	"candidate":"nnamso",
	"interviewer":"Toney",
	"date":"01/01/2021",
	"time":"2021-04-03 17:43:33", 
	"duration":"10"
}
``