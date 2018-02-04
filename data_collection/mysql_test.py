import pymysql
conn = pymysql.Connect(host='127.0.0.1', user='root', passwd='1234',db='mysql',charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")

# cur.execute("SELECT * From pages WHERE id = 3")
cur.execute("SELECT * From pages WHERE title LIKE '%Test%'")
print(cur.fetchone())
cur.close()
conn.close()