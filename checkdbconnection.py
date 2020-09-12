import pymysql.cursors

connection = pymysql.connect(host="192.168.64.2", database="addressbook", user="admin", password="admin")
print(connection)
try:
    cursor = connection.cursor()

    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
