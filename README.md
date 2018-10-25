# miniobservium

Para la instalacion de la version grafica se requerira de instalar algunos componentes de Django
además de tener instalados previamente todas las librerias requeridas como snmp, pandas etc

##Para Django 

pip3 install Django

Una vez instalado Django se procede a correr dentro de la carpeta mini el archivo manage.py
de la siguiente forma

#python3 manage.py runserver 

Esto levantara un servidor interno en la direccion localhost:8080/

En caso de querer usar su computadora como servidor usar

python3 manage.py runserver ip:puerto

###Ejemplo

python3 manage.py runserver 192.168.0.3:8080

#Una vez hecho acceder desde el navegador a la direccion ip dos puntos el puerto /miniobservium
Ejemplo

localhost:8080/miniobservium

o bien

192.168.0.3:8080/miniobservium



