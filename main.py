import redis
import article_vote

conn = redis.Redis(db=1)
print("voting...")
article_vote.article_vote(conn, "user:417525", "article:100408")