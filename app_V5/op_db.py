def conn_db(db_manager,sql_op):
    cursor = db_manager.cursor()
    cursor.execute(sql_op)
    ans=cursor.fetchall()
    #print(ans)
    cursor.close()
    db_manager.commit()
    db_manager.close()
    return ans