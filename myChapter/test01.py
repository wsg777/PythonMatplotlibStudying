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
sql1 = "select weight from students where sex='男' and grade='2 年级' and weight>30"
sql2 = "select weight from students where sex='女' and grade='2 年级' and weight>30"
sql3 = "select weight from students where sex='男' and grade='3 年级' and weight>30"
sql4 = "select weight from students where sex='女' and grade='3 年级' and weight>30"
sql5 = "select weight from students where sex='男' and grade='4 年级' and weight>30"
sql6 = "select weight from students where sex='女' and grade='4 年级' and weight>30"
cur.execute(sql1)
rs = cur.fetchall()
for (r,) in rs:
    weights1.append(r)
cur.execute(sql2)
rs = cur.fetchall()
for (r,) in rs:
    weights2.append(r)
cur.execute(sql3)
rs = cur.fetchall()
for (r,) in rs:
    weights3.append(r)
cur.execute(sql4)
rs = cur.fetchall()
for (r,) in rs:
    weights4.append(r)
cur.execute(sql5)
rs = cur.fetchall()
for (r,) in rs:
    weights5.append(r)
cur.execute(sql6)
rs = cur.fetchall()
for (r,) in rs:
    weights6.append(r)
cur.close()
conn.close()

# data visualization
from matplotlib.pyplot import *
rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
suptitle('江汉大学学生体重分布')

subplot(321)
hist(weights1, bins=100, color='green', alpha=0.5, label='大二男生')
locator_params('x', nbins=24)
locator_params('y', nbins=10)
xticks(fontsize=6, rotation=60)
yticks(fontsize=6)
xlim(30, 150)
legend()
subplots_adjust(wspace=0.2, hspace=0.3)

subplot(322)
hist(weights2, bins=100, color='pink', alpha=0.6, label='大二女生')
locator_params('x', nbins=14)
locator_params('y', nbins=15)
xticks(fontsize=6, rotation=60)
yticks(fontsize=6)
xlim(30, 100)
legend()
subplots_adjust(wspace=0.2, hspace=0.3)

subplot(323)
hist(weights3, bins=100, color='green', alpha=0.6, label='大三男生')
locator_params('x', nbins=24)
locator_params('y', nbins=10)
xticks(fontsize=6, rotation=60)
yticks(fontsize=6)
xlim(30, 150)
legend()
subplots_adjust(wspace=0.2, hspace=0.3)

subplot(324)
hist(weights4, bins=100, color='pink', alpha=0.8, label='大三女生')
locator_params('x', nbins=14)
locator_params('y', nbins=15)
xticks(fontsize=6, rotation=60)
yticks(fontsize=6)
xlim(30, 100)
legend()
subplots_adjust(wspace=0.2, hspace=0.3)

subplot(325)
hist(weights5, bins=100, color='green', alpha=0.7, label='大四男生')
locator_params('x', nbins=24)
locator_params('y', nbins=10)
xticks(fontsize=6, rotation=60)
yticks(fontsize=6)
xlim(30, 150)
legend()
subplots_adjust(wspace=0.2, hspace=0.3)

subplot(326)
hist(weights6, bins=100, color='pink', alpha=1.0, label='大四女生')
locator_params('x', nbins=14)
locator_params('y', nbins=15)
xticks(fontsize=6, rotation=60)
yticks(fontsize=6)
xlim(30, 100)
legend()
subplots_adjust(wspace=0.2, hspace=0.3)

text(22,-50,'横坐标：体重/kg  纵坐标：人数/人  数据来源：2017年体测', fontsize=10,
     verticalalignment="bottom", horizontalalignment="center")

savefig('test01.png', dpi=500)
show()
