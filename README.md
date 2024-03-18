
# Music Store Data Analysis - SQL

This project offers a comprehensive analysis of a music store utilizing PostgreSQL. Dive deep into the intricacies of music store operations and insights using robust SQL queries and data analysis techniques.


## Table of Content
 - Installation
 - Usage
 - Data Description
 - Contributing
## Installation
To execute the SQL queries and perform analysis, you'll need:
 - SQL database management system (DBMS) such as PostgreSQL
 - Python (version 3.0 or above) installed on your system.
 - Required Python libraries: ```pandas```, ```sqlalchemy```.
## Usage
### 1. Load Data into PostgreSQL

 - Ensure you have PostgreSQL installed and running on your system.
 - Create a PostgreSQL database for this project.
 - Modify and execute the Python script ```load_files.py``` to load data from CSV files into your PostgreSQL database.
### 2. Execute SQL Queries

 - Open your preferred SQL interface.
 - If you don't want to load data through python file so you can directly restore the database file. Import the database dump provided in the database_dump folder ```music_database.sql```
 - Execute SQL queries located in the ```Music_Store_Database_Query.sql``` folder to perform analysis.
## Data Description
The dataset includes the following tables:

``album``: Contains information about music albums.

``artist``: Contains details of artists.

``customer``: Stores customer information.

``employee``: Contains employee details.

``genre``: Includes music genres.

``invoice``, invoice_items: Includes information about 
invoices and associated items.

``media_types``: Contains media types (e.g., MPEG audio file).

``playlist``, playlist_track: Information about playlists and 
associated tracks.

``track``: Contains details of tracks available in the store.
## Contributing

Contributions to enhance the analysis or add new insights are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.
