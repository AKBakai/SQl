import psycopg2

password = input('input your password for database: ')
conect = psycopg2.connect(
    database = 'dc',
    user = 'batman',
    password = f'{password}',
    host = 'localhost',
    port = '5432'
)
print('Succes connection')
print('Database succef opened')
cur = conect.cursor()
# cur.execute(
#     '''CREATE TABLE courses(
#         id SERIAL PRIMARY KEY,
#         title VARCHAR,
#         price INT
#     );'''
# )
# print('table create succes!')

cur.execute(
    '''INSERT INTO courses(
        title,
        price
        )
        VALUES(
        'python',
        10000);
    '''
)
cur.execute(
    '''INSERT INTO courses(
        title,
        price
        )
        VALUES(
        'JS',
        9000);
    '''
)
conect.commit()
print('succes added data')
conect.close()
