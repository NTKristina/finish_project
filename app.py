import psycopg2

DB_HOST = 'db'
DB_PORT = '5432'
DB_NAME = 'neretina'
DB_USER = 'postgres'
DB_PASSWORD = '12345'

try:
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    print("Соединение с БД установлено")
    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS test_table (
        "ID" INT,
        "Name" VARCHAR(15),
        "Age" INT,
        "Department" VARCHAR(50));
    '''
    cursor.execute(create_table_query)
    conn.commit()
    print("Таблица создана или уже существует")
    
    # Наполнение таблицы данными
    insert_data_query = '''
    INSERT INTO test_table VALUES
      (1, 'Алина', 28, 'Sales'),
      (2, 'Евгений', 35, 'Security'),
      (3, 'Александр', 42, 'HR'),
      (4, 'Ангелина', 46, 'Cybersecurity'),
      (5, 'Петр', 29, 'Development'),
      (6, 'Василий', 48, 'Security' ),
      (7, 'Семен', 22, 'Testing'),
      (8, 'Алексей', 31, 'Sales'),
      (9, 'Андрей', 35, 'HR'),
      (10, 'Анастасия', 26, 'Development');
    '''
    cursor.execute(insert_data_query)
    conn.commit()
    print("Данные были успешно добавлены.")
    
    select_query = 'SELECT * FROM test_table;'
    cursor.execute(select_query)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    print("Данные из таблицы:")
    for row in rows:
        row_data = ", ".join(f"{column_names[i]}: {value}" for i, value in enumerate(row))
        print(row_data)
    
except psycopg2.Error as e:
    print(f"Ошибка при работе с PostgreSQL: {e}")
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Подключение к PostgreSQL закрыто")
