# test-enreda   
## Instrucciones para su despliegue en local 
1. `$ git clone https://github.com/estelaromer/test-enreda.git test-enreda`   
2. En la carpeta `src`dentro de `backend`: `python3.8 -m venv env`  
3. Copiamos el fichero `.env.local`en la carpeta `backend`   
4. En la carpeta `backend`: `docker-compose build`y `docker-compose up -d`    
5. Corremos migraciones y poblamos base de datos con los mocks: `docker-compose exec web python manage.py migrate`y `docker-compose exec web python manage.py generate_mock_data`   
6. Comprobamos accediendo a http://localhost:8000/api/notes/   
7. En la carpeta `frontend/app`: `docker-compose build`y `docker-compose up -d`
8. Comprobamos accediendo a http://localhost:8081  
9. Para apagar los contenedores, correr tanto en `backend` como en `frontend/app`el comando: `docker-compose down -v`  
## Nota: no se ha implementado la validación de los campos del formulario en el frontend, pero sí en el backend. Para ver el estado de las llamadas a la API, correr el siguiente comando en la carpeta `backend`: `docker-compose logs -f`   