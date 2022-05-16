import sqlite3
DB_NAME = "railways.db"

def db_init():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""CREATE TABLE clients(
        client_id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        email TEXT
    )""")
    conn.execute("""INSERT INTO clients (username, password, email) VALUES
    ("ioann", "dfgdgcxfgg", "ioann@ioann.com"),
    ("vasilly", "dfgdfgdthf", "vasilly@vasylly.com"),
    ("pyotr", "cgjhcrgdrg", "pyotr@pyotr.com")""")

    conn.execute("""CREATE TABLE genders(
        gender_id INTEGER PRIMARY KEY,
        gender_name TEXT
    )""")
    conn.execute("""INSERT INTO genders (gender_name) VALUES
    ("муж"),
    ("жен"),
    ("апач")""")

    conn.execute("""CREATE TABLE client_document_types(
        document_type_id INTEGER PRIMARY KEY,
        type_name TEXT
    )""")
    conn.execute("""INSERT INTO client_document_types (type_name) VALUES
    ("паспорт"),
    ("загран паспорт"),
    ("паспорт моряка")""")

    conn.execute("""CREATE TABLE geo_entities(
        geo_entity_id INTEGER PRIMARY KEY,
        geo_entity_name TEXT
    )""")
    conn.execute("""INSERT INTO geo_entities (geo_entity_name) VALUES
    ("Земля"),
    ("Россия"),
    ("Москва"),
    ("Санкт-Петербург"),
    ("Красноярск"),
    ("Омск"),
    ("Владивосток"),
    ("Домодедово"),
    ("Беларусь"),
    ("Минск")""")

    conn.execute("""CREATE TABLE geo_hierarchy(
        geo_hierarchy_entry INTEGER PRIMARY KEY,
        parent INTEGER, FOREIGN KEY(parent) REFEREMCES geo_entities(geo_entity_name),
        child INTEGER, FOREIGN KEY(child) REFEREMCES geo_entities(geo_entity_name)
    )""")
    conn.execute("""INSERT INTO geo_hierarchy (parent, child) VALUES
    (1, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (1, 9),
    (9, 10)""")

    conn.execute("""CREATE TABLE document_issue_places (
        document_issue_place_id INTEGER PRIMARY KEY,
        org_name TEXT,
        org_code TEXT,
        geo_entity_id INTEGER, FOREIGN KEY(geo_entity_id) REFEREMCES geo_entities(geo_entity_id)
    )""")
    conn.execute("""INSERT INTO document_issue_places (org_name, org_code, geo_entity_id) VALUES
    ("МВД по Орехово-Борисово Южное", "123", 3),
    ("МВД по Орехово-Борисово Северное", "124", 3),
    ("Консульство РФ в Минске", "321", 10)""")
    conn.commit()

def db_check():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    for i in cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"):
        print(i)

from os.path import exists
if not exists(DB_NAME):
    db_init()
db_check()