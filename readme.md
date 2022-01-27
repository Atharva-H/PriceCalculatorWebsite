### Template ==> html files

assets ==> images<br>
js ==> javascript<br>
styles ==> css<br>

pip install virtualenv
virtualenv venv
./venv/Scripts/Activate
pip install -r requirements.txt
python manage.py runserver
python manage.py makemigrations calculator
python manage.py migrate calculator
