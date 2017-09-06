import pymysql

conn = pymysql.connect(host = 'localhost',user = 'root',password = 'd27r703f559#\/*',db = 'teste',charset = 'utf8',cursorclass = pymysql.cursors.DictCursor,autocommit = True)
a = conn.cursor()
sql = "----????----" # valor da query
a.execute(sql)

# para queries de inserção, só executar a query

# para queries de seleção, executar a parte seguinte para filtrar os valores desejados, variáveis de nome genérico

#fetchone(), captura a primeira linha da query Select
#fetchall(), captura todas as linhas da query Select

b = a.fetchall()
print(b)
