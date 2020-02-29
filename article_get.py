import constants

def article_get(conn, page, order='score:'):
    start = (page - 1) * constants.ARTICLES_PER_PAGE
    end = start + constants.ARTICLES_PER_PAGE - 1

    article_ids = conn.zrevrange(order, start, end)
    articles = []
    for id in article_ids:
        article_data = conn.hgetall(id)
        article_data['id'] = id
        articles.append(article_data)

    return articles
    