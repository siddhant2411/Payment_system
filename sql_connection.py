import sqlite3

# import mysql.connector
__cnx = None


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = sqlite3.connect('db\ssip.db', check_same_thread=False)

    # __cnx = mysql.connector.connect(user='root', password='Siddhant@001',
    #                                 host='127.0.0.1',
    #                              database='ssip')'''

    return __cnx
