# use MySQL
import pymysql

weights1 = []
weights2 = []
weights3 = []
weights4 = []
weights5 = []
weights6 = []

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='python')
cur = conn.cursor()
sql1 = "select count(*) from students where sex='男' and grade='2 年级'"
sql2 = "select count(*) from students where sex='女' and grade='2 年级'"
sql3 = "select count(*) from students where sex='男' and grade='3 年级'"
sql4 = "select count(*) from students where sex='女' and grade='3 年级'"
sql5 = "select count(*) from students where sex='男' and grade='4 年级'"
sql6 = "select count(*) from students where sex='女' and grade='4 年级'"
sql7 = "select count(*) from students where sex='男'"
sql8 = "select count(*) from students where sex='女'"
cur.execute(sql1)
rs1, = cur.fetchone()
cur.execute(sql2)
rs2, = cur.fetchone()
cur.execute(sql3)
rs3, = cur.fetchone()
cur.execute(sql4)
rs4, = cur.fetchone()
cur.execute(sql5)
rs5, = cur.fetchone()
cur.execute(sql6)
rs6, = cur.fetchone()
cur.execute(sql7)
rs7, = cur.fetchone()
cur.execute(sql8)
rs8, = cur.fetchone()
cur.close()
conn.close()

print(rs1, rs2, rs3, rs4, rs5, rs6, rs7, rs8)

# data visualization
from matplotlib.pyplot import *
rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
labels = ['男', '女']
figure(figsize=(5, 5))

suptitle('江汉大学男女比例')

subplot(221)
title('大二')
pie([rs1, rs2], labels=labels, autopct='%.2f%%', startangle=67)

subplot(222)
title('大三')
pie([rs3, rs4], labels=labels, autopct='%.2f%%', startangle=67)

subplot(223)
title('大四')
pie([rs5, rs6], labels=labels, autopct='%.2f%%', startangle=67)

subplot(224)
pie([rs7, rs8], labels=labels, autopct='%.2f%%', startangle=67)
title('全校')

savefig('test02.png', dpi=500)
show()
