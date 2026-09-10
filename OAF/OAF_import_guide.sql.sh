# =====================================================================
# One Acre Fund Rwanda — MySQL import guide (Aiven, shared team DB)
# =====================================================================
# Step 0: connect once and create the database + tables.
# Run:  mysql -h mysql-af646a8-summative101.h.aivencloud.com -P 17641 -u avnadmin -p
# Then paste the SQL below (between the SQL markers).
# NOTE: Aiven normally REQUIRES SSL. If DISABLED fails, use --ssl-mode=REQUIRED
# ---------------------------------------------------------------------
# ---------------- SQL: run once (one teammate only) ------------------
# CREATE DATABASE IF NOT EXISTS OAF;
# USE OAF;
#
# CREATE TABLE sites (
#   site_id INT PRIMARY KEY,
#   site_name VARCHAR(100),
#   district VARCHAR(50),
#   sector VARCHAR(50) );
#
# CREATE TABLE warehouses (
#   warehouse_id INT PRIMARY KEY,
#   warehouse_name VARCHAR(100),
#   district VARCHAR(50) );
#
# CREATE TABLE products (
#   product_id INT PRIMARY KEY,
#   product_name VARCHAR(100),
#   product_type VARCHAR(20),
#   unit VARCHAR(10) );
#
# CREATE TABLE requests (
#   request_id INT PRIMARY KEY,
#   site_id INT,
#   product_id INT,
#   season VARCHAR(5),
#   quantity_requested INT,
#   request_date DATE,
#   FOREIGN KEY (site_id) REFERENCES sites(site_id),
#   FOREIGN KEY (product_id) REFERENCES products(product_id) );
#
# CREATE TABLE deliveries (
#   delivery_id INT PRIMARY KEY,
#   request_id INT,
#   warehouse_id INT,
#   quantity_delivered INT,
#   promised_date DATE,
#   delivered_date DATE,
#   status VARCHAR(20),
#   FOREIGN KEY (request_id) REFERENCES requests(request_id),
#   FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id) );
# ----------------------- end of SQL ----------------------------------

# Shared connection shorthand (edit path to where you saved the CSVs)
MYSQL="mysql -h mysql-af646a8-summative101.h.aivencloud.com -P 17641 -u avnadmin -p --ssl-mode=REQUIRED"
DIR="/workspaces/higher_level_programming"

# IMPORT ORDER MATTERS (foreign keys):
# 1 sites  2 warehouses  3 products  4 requests  5 deliveries

# ---------- 1. sites ----------
CSV="$DIR/OAF_sites.csv"; \
python3 -c "import csv,sys;f=sys.argv[1];q=lambda s:(s or '').strip().replace('\\\\','\\\\\\\\').replace(\"'\",\"''\");print('USE OAF; START TRANSACTION;');rows=[f\"({int(r['site_id'])},'{q(r['site_name'])}','{q(r['district'])}','{q(r['sector'])}')\" for r in csv.DictReader(open(f,newline='',encoding='utf-8'))];print('INSERT INTO sites (site_id,site_name,district,sector) VALUES\\n'+',\\n'.join(rows)+'\\nON DUPLICATE KEY UPDATE site_name=VALUES(site_name),district=VALUES(district),sector=VALUES(sector); COMMIT; SELECT COUNT(*) AS total_rows FROM sites;')" "$CSV" | $MYSQL

# ---------- 2. warehouses ----------
CSV="$DIR/OAF_warehouses.csv"; \
python3 -c "import csv,sys;f=sys.argv[1];q=lambda s:(s or '').strip().replace('\\\\','\\\\\\\\').replace(\"'\",\"''\");print('USE OAF; START TRANSACTION;');rows=[f\"({int(r['warehouse_id'])},'{q(r['warehouse_name'])}','{q(r['district'])}')\" for r in csv.DictReader(open(f,newline='',encoding='utf-8'))];print('INSERT INTO warehouses (warehouse_id,warehouse_name,district) VALUES\\n'+',\\n'.join(rows)+'\\nON DUPLICATE KEY UPDATE warehouse_name=VALUES(warehouse_name),district=VALUES(district); COMMIT; SELECT COUNT(*) AS total_rows FROM warehouses;')" "$CSV" | $MYSQL

# ---------- 3. products ----------
CSV="$DIR/OAF_products.csv"; \
python3 -c "import csv,sys;f=sys.argv[1];q=lambda s:(s or '').strip().replace('\\\\','\\\\\\\\').replace(\"'\",\"''\");print('USE OAF; START TRANSACTION;');rows=[f\"({int(r['product_id'])},'{q(r['product_name'])}','{q(r['product_type'])}','{q(r['unit'])}')\" for r in csv.DictReader(open(f,newline='',encoding='utf-8'))];print('INSERT INTO products (product_id,product_name,product_type,unit) VALUES\\n'+',\\n'.join(rows)+'\\nON DUPLICATE KEY UPDATE product_name=VALUES(product_name),product_type=VALUES(product_type),unit=VALUES(unit); COMMIT; SELECT COUNT(*) AS total_rows FROM products;')" "$CSV" | $MYSQL

# ---------- 4. requests ----------
CSV="$DIR/OAF_requests.csv"; \
python3 -c "import csv,sys;f=sys.argv[1];q=lambda s:(s or '').strip().replace('\\\\','\\\\\\\\').replace(\"'\",\"''\");print('USE OAF; START TRANSACTION;');rows=[f\"({int(r['request_id'])},{int(r['site_id'])},{int(r['product_id'])},'{q(r['season'])}',{int(r['quantity_requested'])},'{q(r['request_date'])}')\" for r in csv.DictReader(open(f,newline='',encoding='utf-8'))];print('INSERT INTO requests (request_id,site_id,product_id,season,quantity_requested,request_date) VALUES\\n'+',\\n'.join(rows)+'\\nON DUPLICATE KEY UPDATE site_id=VALUES(site_id),product_id=VALUES(product_id),season=VALUES(season),quantity_requested=VALUES(quantity_requested),request_date=VALUES(request_date); COMMIT; SELECT COUNT(*) AS total_rows FROM requests;')" "$CSV" | $MYSQL

# ---------- 5. deliveries ----------
CSV="$DIR/OAF_deliveries.csv"; \
python3 -c "import csv,sys;f=sys.argv[1];q=lambda s:(s or '').strip().replace('\\\\','\\\\\\\\').replace(\"'\",\"''\");print('USE OAF; START TRANSACTION;');rows=[f\"({int(r['delivery_id'])},{int(r['request_id'])},{int(r['warehouse_id'])},{int(r['quantity_delivered'])},'{q(r['promised_date'])}','{q(r['delivered_date'])}','{q(r['status'])}')\" for r in csv.DictReader(open(f,newline='',encoding='utf-8'))];print('INSERT INTO deliveries (delivery_id,request_id,warehouse_id,quantity_delivered,promised_date,delivered_date,status) VALUES\\n'+',\\n'.join(rows)+'\\nON DUPLICATE KEY UPDATE request_id=VALUES(request_id),warehouse_id=VALUES(warehouse_id),quantity_delivered=VALUES(quantity_delivered),promised_date=VALUES(promised_date),delivered_date=VALUES(delivered_date),status=VALUES(status); COMMIT; SELECT COUNT(*) AS total_rows FROM deliveries;')" "$CSV" | $MYSQL

# Expected row counts:  sites=220  warehouses=6  products=5  requests=2464  deliveries=2464
