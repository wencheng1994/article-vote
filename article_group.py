import article_get

'''
文章群组功能，实现文章添加到群组和从群组移除
'''
def add_remove_groups(conn, article_id, to_add = [], to_remove = []):
    for group in to_add:
        conn.sadd('group:' + group, article_id)
    for group in to_remove:
        conn.srem('group:' + group, article_id)
    
def get_group_article(conn, group, page, order='score:'):
    key = order + group
    if not conn.exsit(key):
        conn.zinterstore(key, ['group:' + group, order], aggregate='max')
        conn.expire(key, 60)
    return article_get.article_get(conn, page, key)