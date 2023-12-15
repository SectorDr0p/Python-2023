import psycopg2

connect_string = "dbname=my_database user=my_user password=secret host=127.0.0.1"

with psycopg2.connect(connect_string) as connection:
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) from fooditem;')

        cursor.execute('CREATE TABLE FOODS(id int NOT NULL, name char(15), price float')
        cursor.execute('COPY FOODS(id,name,price)
                       FROM "C:\\Users\\localadmin\\PycharmProjects\\Python-2023\\17_Wstep_do_obiektowosci\\foods.csv"
                       DELIMETER "," CSV HEADER;'

        result = cursor.fetchall()
        for row in result:
            print (row)
    except psycopg2.Error as e:
        print(e)