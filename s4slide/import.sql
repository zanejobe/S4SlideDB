/*
Use this script to import sample data to the sqlite3 database.
Relative pathnames are used, so run it from this directory.
Usage: sqlite3 -init import.sql db.sqlite3
*/

.shell python3.6 manage.py migrate app zero
.shell rm -f app/migrations/????_*.py
.shell python3.6 manage.py makemigrations
.shell python3.6 manage.py migrate

.mode csv
.import ../data/sample/summary_info_id.csv app_summary_info_id
.import ../data/sample/landslide_morphometrics.csv app_landslide_morphometrics
.import ../data/sample/landslide_metrics.csv app_landslide_metrics
.import ../data/sample/meta_table.csv app_meta_table
