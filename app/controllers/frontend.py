from app import application as app

@app.route('/', methods=['GET', 'POST'])
def index():
    indexBody = """
<h1>API de candidatxs a elecciones de México 2021</h1>
</br>
<pre>
           __________
         .'----------`.
         | .--------. |
         | |########| |
         | |########| |      /__________\\
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             |
|       ______|_|_______     |__________|             |
|      /  %%%%%%%%%%%%  \                             |
|     /  %%%%%%%%%%%%%%  \                            |
|     ^^^^^^^^^^^^^^^^^^^^                            |
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</pre>
</br>
<h2>Endpoints disponibles</h2>
</br>
<ul>
    <li><a href="./export">Toda la información</a></li>
    <li><a href="./export-min">Información mínima necesaria</a></li>
    <li><a href="./person">Personas</a></li>
    <li><a href="./membership">Adscripciones politicas</a></li>
    <li><a href="./contest">Contiendas politicas</a></li>
    <li><a href="./party">Partidos Politicos</a></li>
    <li><a href="./coalition">Coaliciones</a></li>
    <li><a href="./area">Áreas</a></li>
    <li><a href="./chamber">Cámaras</a></li>
    <li><a href="./role">Roles</a></li>
    <li><a href="./other-name">Listado de otros nombres por persona</a></li>
    <li><a href="./person-profession">Listado de profesiones por persona</a></li>
    <li><a href="./profession">Listado de profesiones</a></li>
    <li><a href="./url">URLs</a></li>
</ul>
<h2>Enlaces útiles</h2>
Para conocer más acerca del proyecto, te recomendamos visitar el repositorio de GitHhub o nuestras redes sociales.
</br>
<ul>
    <li><a href="https://github.com/SocialTIC/mx-elections-2021">Documentación de la API</a></li>
    <li><a href="https://socialtic.org">Sitio de SocialTIC</a></li>
    <li><a href="https://www.facebook.com/Socialtic/">Facebook de SocialTIC</a></li>
    <li><a href="https://twitter.com/socialtic/">Twitter de SocialTIC</a></li>
    <li><a href="https://www.instagram.com/socialtic/">Instagram de SocialTIC</a></li>
</ul>
    """
    return indexBody
