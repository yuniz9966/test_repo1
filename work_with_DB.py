# import pymysql
#
# dbconfig = {  # для mysql порт по умолчанию 3306
#     'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'ich_edit'
# }
#
# name = 'USER 5'
# age = 48
#
# connector = pymysql.connect(**dbconfig)
# cursor = connector.cursor()
#
# cursor.execute("SELECT * FROM users")
# data = cursor.fetchall()
#
# for user in data:
#     print(user)
#
#
#

import mysql.connector
from pymysql.cursors import DictCursor

# dbconfig = {'host': 'ich-edit.edu.itcareerhub.de',
#             'user': 'ich1',
#             'password': 'ich1_password_ilovedbs',
#             'database': 'ich_edit'}

dbconfig = {  # для mysql порт по умолчанию 3306
'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
'user': 'ich1',
'password': 'password',
'database': 'ich_edit'
}
connector = mysql.connector.connect(**dbconfig)
print(connector)