# -*- coding:utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host="10.213.128.98", port=13306
                       , user="idc_exchange", password="123456"
                       , db="idc_exchange")

print(conn)
c = conn.cursor()