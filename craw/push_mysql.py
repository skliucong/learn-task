# -*- coding: UTF-8 -*-
import jieba
import json
import MySQLdb
def update_corpus(title,source,link,content):
    db = MySQLdb.connect("127.0.0.1", "root", "123456", "topic_model", charset='utf8' )
    cursor = db.cursor()

    # SQL 更新语句
    sql = "INSERT INTO news (title,source,link,content) VALUES('%s','%s','%s','%s')" % (title,source,link,content)
    try:

        cursor.execute(sql)
        db.commit() # 提交到数据库执行
    except:
        db.rollback() #回滚
        return False

    db.close()
    return True

if __name__ == '__main__':
    pass
    import os


    L = []
    for root, dirs, files in os.walk("D:\data\people_news"):
        for file in files:
            if 'success' in file:
                L.append(os.path.join(root, file))
    for item in L:
        source=item.split('_')[-2]
        file=open(item,'r')
        for line in file.readlines():
            line_content=json.loads(line.strip('\n'))
            # print(line_content)
            update_corpus(line_content['biaoti'],source,line_content['link'],line_content['neirong'])


        file.close()