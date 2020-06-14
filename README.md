# Proyecto Integrador - Sistemas Multiusuarios

En este proyecto se demuestra cómo se pueden conectar diferentes servidores entre sí para poder brindar un servicio más robusto al usuario, así como seguro y resistente a fallos.

## Instalación

Para este proyecto sólo es necesario instalar [Docker](https://docs.docker.com/get-docker/), y docker-compose (ya viene pre instalado junto con Docker para la mayoría de sistemas operativos).

## Ejecución

Para ejecutar este proyecto, abre la carpeta donde se haya descargado, ejecuta:

```bash
# Asegúrate de que estés en la carpeta del proyecto
docker-compose up
```

Esto leerá el archivo `docker-compose.yaml` y levantará los recursos necesarios. Ten en cuenta que se hará un binding a los puertos `3306` y `8000` por lo que no tiene que haber ningún servicio corriendo que utilice esos puertos. También, si así lo deseas puedes cambiar dichos puertos directamente en el archivo `docker-compose.yaml`, en la parte de `ports` (sólo debes de cambiar el primero, que es el de tu computadora ya que el segundo es el puerto del contenedor generado). 

## Prueba

En el caso de que no hayas cambiado los puertos en el archivo de configuraciones, podrás hacer una petición desde tu explorador (como Chrome por ejemplo), o cualquier cliente HTTP a la ruta `http://localhost:8000`, si cambiaste el puerto, sólo pon el puerto que hayas puesto en lugar del 8000. También lo puedes hacer desde la consola:

```bash
curl localhost:8000
```

Si la petición fue exitosa, desde tu explorador podrás ver también todas las rutas disponibles en

```bash
http://localhost:8000/docs
```

## Detener ejecución

Para detener la ejecución sólo debes de parar la ejecución del `docker-compose` con la combinación de teclas CTRL-C y una vez detenida la ejecución, deberás escribir en la consola:

```bash
docker-compose down
```

Hecho con 💙 y 🌮 desde 🇲🇽