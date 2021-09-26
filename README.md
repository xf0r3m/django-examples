## django-exaples

Testowane na Ubuntu 20.04

* Foldery:
	1. Django1 - aplikacja Learning Log tworzona wraz książką (przewija się prze całą cześć od Django w książce). Aplikacja służy do monitorowania postępów na nauce i prowadzenia wpisów podsumowujących lekcje nauki danej rzeczy (rzeczy, przedstawionej jako temat).
	2. Django2 - aplikacja Pizzeria stworzona w jednym z ćwiczeń, ciągnięta dalej na potrzeby przykładów do ściągi z PYTHONga (narazie bez Bootstrapa, robie właśnie).
	3. Django3  - Aplikacja Blogs, najprostszy apka umożliwający wrzucanie wpisów z tytułem i datą. Jest Bootstrap zerżnięty z Django1. 

* Instalacja:
	1. `$ sudo apt install python3-venv`
	2. `$ python3 -m venv project_env`
	3. `$ source project_env/bin/activate`
	4. `(project_env) $ pip install django django-bootstrap4`
	5. Skopiuj zawartość jednego z katalogów DjangoX, gdzie X = 1 lub 2 lub 3.
	6. `$ chmod +x manage.py`
	
* Uruchomienie serwera:
	1. `(project_env) $ python manage.py runserver`
	
### Jak to odpalić pod Windą ? Nie mam zielonego pojęcia. ;)
	
