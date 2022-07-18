import uuid as v4
import sqlite3
from datetime import datetime, timedelta, time
#
# id = v4.uuid4()
# print(id)
#
# # conn = sqlite3.connect('test.sqlite')
# # sqlite3.register_adapter(v4.uuid4, lambda u: u.bytes_le)
# #
# # cur = conn.cursor()
# #
# # create_statement = '''CREATE TABLE IF NOT EXISTS test(id TEXT PRIMARY KEY)'''
# # cur.execute(create_statement)
# # statement = '''INSERT INTO test(id) values(?)'''
# # conn.commit()
# # cur.execute(statement, [id.bytes_le])
# # cur.execute('''SELECT * FROM test''')
# #
# # for i in cur.fetchall():
# #     print(i)
#
# RETURNDAY = 7
# today = datetime.now().date()
# return_date = today + timedelta(days=RETURNDAY)
# print(return_date)
# print(today)
# # if return_date >  :
# if today >= return_date:
#     print(return_date)
