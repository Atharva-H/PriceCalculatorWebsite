### Template ==> html files

assets ==> images<br>
js ==> javascript<br>
styles ==> css<br>

pip install virtualenv
virtualenv venv
./venv/Scripts/Activate
pip install -r requirements.txt
python manage.py runserver
python manage.py runserver 192.168.1.137:8000
python manage.py makemigrations calculator
python manage.py migrate calculator

python manage.py createsuperuser

## Django : Transfer data from Sqlite to another database

python manage.py dumpdata > db.json
Change the database settings to new database such as of MySQL / PostgreSQL.
python manage.py migrate
python manage.py shell
Enter the following in the shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
python manage.py loaddata db.json
