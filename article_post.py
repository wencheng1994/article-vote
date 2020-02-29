'''
文章发布函数
'''
import time
import constants

def article_post(conn, user, title, link):
    article_id = str(conn.incr('article:'))

    redis_article_id = "article:" + article_id
    voted = 'voted:' + redis_article_id
    conn.sadd(voted, user)
    conn.expire(voted, constants.ONE_WEEK_IN_SECONDS)

    now = time.time()
    article = "article:" + article_id
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1
    })

    conn.zadd('score:', article, now + constants.VOTE_SCORE)
    conn.zadd('time:', article, now)

    return article_id