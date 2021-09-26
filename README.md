# Proyecto Web con el Framework Django

Este proyecto es el resultado de un curso de análisis y diseño de sistemas d einformación II usando el framework de Django impartido en la Universidad de Caldas para el programa de tecnología en sistemas de información.

## Temas tratados en el curso

- Conceptos básicos de Python. [Documentación oficial](https://www.python.org/)
- Framework de Django V3.2^. [Documentación Oficial](https://www.djangoproject.com/)
- Patrón de diseño Model, Template, View (MTV) con la estructura recomendada por Django. [Documentación Oficial](https://docs.djangoproject.com/en/3.2/intro/overview/)
- Trabajo con base de datos incluyendo migraciones (Model). [Documentación Oficial](https://docs.djangoproject.com/en/3.2/topics/db/models/)
- Templates implementados en el ORM. [Documentación Oficial](https://docs.djangoproject.com/en/3.2/topics/templates/)
- Capa vista (View). [Documentación Oficial](https://laravel.com/docs/7.x/controllers)
- Creación de rutas en el archivo `urls.py`. Rutas con parámetros. [Documentación oficial](https://docs.djangoproject.com/en/3.2/topics/http/urls/)
- Construcción de Queries con el ORM usado por Django. [Documentación Oficial](https://docs.djangoproject.com/en/3.2/topics/db/queries/)

## Puesta a punto del proyecto

Para poner en funcionamiento el proyecto, se debe clonar el repositorio actual y posteriormente en la carpeta del proyecto realizar los siguientes pasos:

### Prerequisitos

- Tener instalado Python V3.8 o superior.
- Tener instalado el gestor de paquetes pip.
- Tener instalado un motor de bases de datos. Puedes ser Postgresql, MySql o sqlite.

### Instrucciones

1. Ejecutar el comando de instalación de paquetes de python (Desde una consola estando en la raiz del proyecto).
   `pip install -r requirements.txt`

2. A continuación, se deben ejecutar las migraciones para que se creen las tablas de la base de datos, esto se realiza con el siguiente comando.
   `python manage.py migrate`

3. Finalmente se ejecuta la aplicación, se registra un nuevo usuario y ya se pueden crear nuevos recursos.

`python manage.py runserver`

## Documentación del curso

Para más información de la creación del proyecto, dejo abierto el [documento oficial](https://drive.google.com/file/d/1cuW4TfngmqvS40aRaNa0yFjkfK0Wkelv/view?usp=sharing) en donde explico paso por paso la creación del proyecto actual desde la puesta a punto del entorno de trabajo hasta dejar la aplicación totalmente funcional. En el documento dejo referencias a documentación y cursos que permiten complementar el conocimiento visto.

**Creado por**: Carlos Andres Castañeda Osorio