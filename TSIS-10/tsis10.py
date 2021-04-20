import psycopg2


#connecting

conn = psycopg2.connect(
    host="localhost",
    database="tsisnoten",
    user="postgres",
    password="password")

cur = conn.cursor()


def creating_table():
    cur.execute("""
    CREATE TABLE auto (
        name TEXT,
        cost VARCHAR(100),
        speed INTEGER
    );
    """)

def inserting_data():
    sql = """
    INSERT INTO auto(name) VALUES (%s) RETURNING name, cost
    """
    car_name = 'BMW'
    cur.execute(sql, (car_name,))
    inserted_name = cur.fetchone()
    #print(inserted_name)

def updating():
    sql = """
    UPDATE auto SET speed=%s WHERE name=%s
    """
    car_speed = 280
    car_name = 'BMW'
    cur.execute(sql, (car_speed, car_name))

    print(cur.rowcount)


def reading():
    sql = '''
    SELECT * FROM auto
    '''
    cur.execute(sql)

    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()

def deleting():
    sql = """
    DELETE FROM auto WHERE name=%s
    """
    car_name = 'Toyota'
    cur.execute(sql, (car_name,))
    print(cur.rowcount)


#creating_table() 
#inserting_data()   
#updating()   
#reading()
#deleting()


cur.close()
conn.commit()