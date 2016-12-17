import psycopg2
import json
conn = psycopg2.connect(host="localhost",database="testsql",port=5432,user="vagrant",password="vagrant")
cursor = conn.cursor()
cursor.execute("select * from kappa_count")
result = cursor.fetchall()
json_str_list = ""
for row in result:
	json_str = ""
	json_str = "{"+"'"+str(row[0])+"',"+str(row[1])+",'"+str(row[2])+"','"+str(row[3])+"'},"
	json_str_list += json_str
conn.commit()
cursor.close()
conn.close()

result_json = "["+json_str_list+"]"
result_json = json.dumps(result_json, ensure_ascii=False)
print (result_json)
