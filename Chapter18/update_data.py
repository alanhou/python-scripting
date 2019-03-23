# import MySQLdb as db
import pymysql as db

con_obj = db.connect('localhost', 'test_user', 'test123', 'test')
cur_obj = con_obj.cursor()
cur_obj.execute('UPDATE books SET Name = "Fantastic Beasts" WHERE Id = 1')
try:
	con_obj.commit()
except:
	con_obj.rollback()
