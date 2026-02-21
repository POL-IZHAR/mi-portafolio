+++
date = '2026-02-20T21:27:36-08:00'
draft = false
title = 'Reporte'
+++
# Reporte: Sintaxis y uso de Markdown

## 1. ¿Qué es Markdown?
Markdown es un lenguaje de marcado ligero creado en 2004 por John Gruber. Su objetivo principal es permitir a las personas escribir usando un formato de texto plano que sea fácil de leer y de escribir, y que posteriormente pueda ser convertido de manera estructurada a HTML o a otros formatos (como PDF). 

A diferencia de los lenguajes de marcado complejos (como HTML o XML) que utilizan muchas etiquetas que dificultan la lectura, Markdown utiliza caracteres de puntuación simples y familiares para darle formato al texto. Hoy en día, es el estándar indispensable en el desarrollo de software para escribir documentación, archivos `README` en repositorios y contenido para generadores de sitios estáticos.

## 2. ¿Cómo se utiliza?
Para utilizar Markdown solo necesitas un editor de texto plano (como Visual Studio Code, Sublime Text o el Bloc de notas). 

1. **Creación del archivo:** Creas un archivo y lo guardas con la extensión `.md` (por ejemplo, `reporte.md`).
2. **Escritura:** Escribes tu contenido utilizando la sintaxis especial de caracteres (asteriscos, guiones, numerales).
3. **Renderizado (Visualización):** El archivo es procesado por un "intérprete" de Markdown. Plataformas como GitHub, herramientas como Hugo, o extensiones de Visual Studio Code leen estos caracteres especiales y los traducen visualmente a texto con formato.

## 3. Sintaxis Básica de Markdown
A continuación, se presentan los elementos más comunes de la sintaxis y cómo se escriben:

### Encabezados (Títulos)
Se utiliza el símbolo de numeral o gato (`#`) al inicio de la línea. La cantidad de símbolos determina el nivel del título (del 1 al 6).

* `# Título 1` (El más grande)
* `## Título 2`
* `### Título 3`

### Énfasis de Texto
Para resaltar palabras o frases, se envuelven en asteriscos (`*`) o guiones bajos (`_`).

* **Negrita:** Se usan dos asteriscos. Ejemplo: `**Este texto es negrita**`.
* *Cursiva:* Se usa un asterisco. Ejemplo: `*Este texto es cursiva*`.
* ***Negrita y cursiva:*** Se usan tres asteriscos. Ejemplo: `***Texto muy resaltado***`.

### Listas
Markdown permite crear listas de manera muy intuitiva.

* **Listas desordenadas:** Usa un guion (`-`), un asterisco (`*`) o un signo de suma (`+`) seguido de un espacio.
  - Elemento A
  - Elemento B

* **Listas ordenadas:** Usa un número seguido de un punto y un espacio.
  1. Primer paso
  2. Segundo paso

### Enlaces
Para crear un hipervínculo, el texto que se va a mostrar se encierra entre corchetes `[ ]`, seguido inmediatamente por la URL encerrada entre paréntesis `( )`.
* **Sintaxis:** `[Texto a mostrar](https://url-del-sitio.com)`
* **Ejemplo:** `[Visita Google](https://google.com)`

### Imágenes
Es casi idéntico a los enlaces, pero se debe agregar un signo de exclamación (`!`) al principio.
* **Sintaxis:** `![Texto alternativo para la imagen](https://url-de-la-imagen.jpg)`

### Citas (Blockquotes)
Para citar texto de otra fuente, se utiliza el signo de "mayor que" (`>`) al inicio de la línea.
> Este es un bloque de cita.

### Código
Para mostrar código fuente sin que Markdown intente darle formato, se usan acentos graves.
* **Código en línea:** Se envuelve en un solo acento grave. Ejemplo: Usa el comando `git status`.
* **Bloques de código:** Se envuelven en tres acentos graves (```) en la línea anterior y posterior al bloque.

---

## Segunda sesión: Uso de Git y GitHub

### 1. ¿Qué son Git y GitHub?
Aunque a menudo se mencionan juntos, Git y GitHub son dos cosas distintas que trabajan en conjunto para gestionar el código fuente:

* **Git:** Es un sistema de control de versiones distribuido y de código abierto. Funciona de manera local en tu computadora y se encarga de registrar el historial de cambios de tus archivos. Te permite regresar a versiones anteriores, experimentar sin dañar el código original y facilitar el trabajo colaborativo.
* **GitHub:** Es una plataforma basada en la nube que permite alojar repositorios de Git. Sirve como un respaldo remoto de tu código y ofrece herramientas visuales para gestionar proyectos, colaborar con otros desarrolladores, revisar código y automatizar procesos (como el despliegue de páginas web).

### 2. ¿Cómo se utilizan?
El flujo de trabajo habitual consiste en usar **Git** desde la línea de comandos (como *Git Bash*) en tu entorno local. Trabajas en tus archivos, guardas el progreso en un historial local (haciendo *commits*) y, cuando estás listo para respaldar o compartir tu trabajo, utilizas Git para enviar (*push*) esos cambios a tu repositorio remoto alojado en **GitHub**.

### 3. Comandos Esenciales de Git
Para utilizar Git en la terminal, estos son los comandos fundamentales:

* `git init`: Inicializa un nuevo repositorio de Git en la carpeta en la que te encuentras.
* `git status`: Muestra el estado actual del repositorio (archivos modificados, archivos sin rastrear y archivos listos para ser guardados).
* `git add <archivo>` o `git add .`: Añade archivos específicos (o todos los modificados usando el punto) al área de preparación (*staging area*), indicando que están listos para el próximo guardado.
* `git commit -m "Mensaje descriptivo"`: Guarda los cambios que están en el área de preparación de forma permanente en el historial local, junto con un mensaje que explica qué se modificó.
* `git remote add origin <URL>`: Conecta tu repositorio local con un repositorio remoto (como uno en GitHub).
* `git push origin main`: Envía (sube) tus *commits* locales al repositorio remoto en la rama principal (*main*).
* `git pull origin main`: Descarga y fusiona los cambios que estén en el repositorio remoto hacia tu repositorio local.
* `git clone <URL>`: Descarga una copia exacta de un repositorio remoto existente en tu computadora.

### 4. Cómo crear un repositorio y subir información a la nube (GitHub)
Para subir tu proyecto local a la nube por primera vez, sigue estos pasos:

1. **Crear el repositorio remoto:** Entra a tu cuenta de [GitHub](https://github.com), haz clic en el botón **"New"** (Nuevo repositorio), asígnale un nombre, déjalo público o privado y haz clic en **"Create repository"**. *(Nota: No marques la opción de añadir un archivo README en este paso para que el repositorio esté completamente vacío).*
2. **Inicializar Git localmente:** Abre tu terminal (Git Bash) en la carpeta de tu proyecto local y ejecuta:
   ```bash
   git init
   ```
3. **Preparar y guardar los archivos:** Añade tus archivos y crea tu primer *commit*:
   ```bash
   git add .
   git commit -m "Mi primer commit: reporte de Markdown"
   ```
4. **Renombrar la rama principal:** Por convención moderna, la rama principal se llama `main`:
   ```bash
   git branch -M main
   ```
5. **Vincular el repositorio local con GitHub:** Copia la URL que te da GitHub y ejecútala en tu terminal:
   ```bash
   git remote add origin [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
   ```
6. **Subir los archivos a la nube:** Finalmente, envía tu código a GitHub:
   ```bash
   git push -u origin main
   ```
   *(El parámetro `-u` hace que Git recuerde la conexión, por lo que en el futuro solo necesitarás escribir `git push`).*

   ---

## Tercera sesión: Páginas estáticas con Hugo y GitHub Actions

### 1. ¿Qué son Hugo y GitHub Actions?

* **Hugo:** Es uno de los generadores de sitios estáticos más rápidos y populares, escrito en el lenguaje de programación Go. Su función principal es tomar un directorio de archivos de texto plano (escritos en Markdown) junto con plantillas de diseño, y renderizarlos para construir un sitio web completo en HTML, CSS y JavaScript. Al ser "estático", no requiere de una base de datos en tiempo real, lo que lo hace muy rápido y seguro.
* **GitHub Actions:** Es la plataforma de Integración Continua y Despliegue Continuo (CI/CD) integrada nativamente en GitHub. Permite automatizar tareas de tu ciclo de desarrollo. En este contexto, se utiliza para automatizar la construcción y publicación de tu sitio web: cada vez que subes un cambio (push) a tu repositorio, GitHub Actions ejecuta las instrucciones necesarias para actualizar tu página sin que tengas que hacerlo manualmente.



### 2. Cómo crear un sitio estático en Hugo
Una vez que tienes instalado Hugo en tu sistema (ya sea Windows, macOS o Linux), el proceso básico es el siguiente:

1. **Generar la estructura:** En tu terminal (Git Bash), ejecuta el comando para crear un nuevo sitio:
   ```bash
   hugo new site mi-portafolio
   ```
2. **Añadir un tema:** Navega dentro de la nueva carpeta (`cd mi-portafolio`). Puedes añadir un tema utilizando Git. Por ejemplo:
   ```bash
   git init
   git submodule add [https://github.com/theNewDynamic/gohugo-theme-ananke.git](https://github.com/theNewDynamic/gohugo-theme-ananke.git) themes/ananke
   ```
3. **Configurar el sitio:** Abre el archivo de configuración `hugo.toml` (o `config.toml`) en tu editor y añade la línea `theme = "ananke"` para activar el tema.
4. **Crear contenido:** Genera tu primera página o post en formato Markdown ejecutando:
   ```bash
   hugo new content/posts/mi-primer-reporte.md
   ```
5. **Servidor de prueba local:** Para ver tu sitio antes de subirlo, levanta el servidor local de Hugo con los borradores habilitados:
   ```bash
   hugo server -D
   ```
   (Podrás ver tu página en tu navegador, generalmente en `http://localhost:1313`).

### 3. Subir la información y configurar GitHub Actions para GitHub Pages
Para que tu sitio sea público y automatizado, debes seguir estos pasos:

1. **Subir tu proyecto a GitHub:** Utilizando los comandos vistos en la Sesión 2 (`git add .`, `git commit`, `git push`), sube todo el directorio de tu proyecto Hugo a un repositorio nuevo en GitHub.
2. **Configurar GitHub Pages:**
   - Ve a tu repositorio en GitHub y haz clic en la pestaña **Settings** (Configuración).
   - En el menú lateral izquierdo, selecciona **Pages**.
   - En la sección "Build and deployment" (Construcción y despliegue), busca la opción **Source** (Origen) y cámbiala a **GitHub Actions**.
3. **Configurar el Workflow de Hugo:**
   - GitHub te sugerirá automáticamente el flujo de trabajo llamado "Hugo". Haz clic en **Configure**.
   - Esto creará un archivo llamado `hugo.yaml` dentro de la ruta `.github/workflows/` en tu repositorio.
   - Revisa el código autogenerado y haz clic en **Commit changes** para guardarlo.
4. **Publicación automática:** - A partir de este momento, GitHub Actions detectará el nuevo archivo y comenzará a construir tu sitio de manera automática. 
   - Cuando el proceso termine, tu sitio estático estará publicado y disponible en la URL proporcionada por GitHub Pages.

---

## Enlaces del Proyecto

A continuación, se presentan los enlaces a los recursos generados durante estas sesiones:

