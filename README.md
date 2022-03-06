# Descripción del proyecto

El objetivo del proyecto era **crear un modelo de Machine Learning para predecir el precio de los distintos componentes para PCs.**

Con Scrapy se ha creado un csv con todos los componentes que ha hido obteniendo de la web de Amazon.

Posteriormente se ha tratado en KNIME para generar un modelo de predicción con Gradient Boosted Trees (w/ XGBoost).

**El modelo para este ejemplo ha sido entrenado solo con tarjetas gráficas de Nvidia aunque el dataset tiene de todo tipo de componentes.**

# Funcionamiento

Amazon tiene un bloqueo para los bots que usan Web Scrapping, se ha montado un servidor de Tor para ir cambiando de IP cada 5 intentos además de User-Agents, etc...
Esa parte se encarga de obtener los html con los datos de los componentes (notebooks/WebScrappingTor) y guardarlos.

Posteriormente con Scrapy se obtienen los datos de los html descargados y se va generando el csv.

# Instalación

-> poetry install (Instalar dependencias)

-> cd notebooks/amazon_webscrapping && scrapy crawl "webscrapping_amazon" -O amazon_data.csv (Generar el csv)

También se puede abrir el notebook "AmazonReaderMain.ipynb" y lanzarlo desde ahí.

# Resultado de algunas predicciones

![image](https://user-images.githubusercontent.com/60214254/156945857-8458b29a-f106-42a5-b10e-4e57f6ceb968.png)

# Workflow KNIME

![image](https://user-images.githubusercontent.com/60214254/156946489-f3569b56-41f1-41dd-8ec1-abe49f8f0cb9.png)
