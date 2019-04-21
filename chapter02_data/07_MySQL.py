# MySQL读1行
# import pymysql
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
# cur = conn.cursor()
# sql = "select * from students where name = '王少刚'"
# cur.execute(sql)
# rs = cur.fetchall()
# for r in rs:
#     print(r)

# MySQL读多行
# import pymysql
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
# cur = conn.cursor()
# sql = "select * from students where name like '%少%'"
# cur.execute(sql)
# rs = cur.fetchall()
# for r in rs:
#     print(r)

# MySQL更新
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
cur = conn.cursor()
sql = "update students set studentNumber='162208100101' where name='王少刚'"
cur.execute(sql)
conn.commit()
print(cur.rowcount, '行受影响')