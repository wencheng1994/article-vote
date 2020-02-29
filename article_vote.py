#!/usr/bin/python
# coding=utf8
# 文章投票函数
# 传入conn redis连接，user 用户在redis中的标识， article 文章在redis中的标识
# 先检查文章时间是否过去一周了
# 没有过去一周的情况下，检查user是否已经给article投过票了
# 没有投过票的情况下，真正执行投票动作
# 更新文章分数

#
# time: zset结构，存储文章的发布时间
# score: zset结构，存储文章的分数
# votes:#{articleId} set结构，某篇文章的投票用户
# article:{articleId} hash结构，某篇文章的元信息
#
import time
import constants

def article_vote(conn, user, article):
    if(checkTimePassed(conn, article)):
        return
    if(addUser(conn, user, article)):
        internal_article_vote(conn, article)

def checkTimePassed(conn, article):
    cutoff = time.time() - constants.ONE_WEEK_IN_SECONDS
    if(conn.zscore("time:", article) < cutoff):
        print("time passed...")
        return False
    return True 

def addUser(conn, user, article):
    print("add user to article vote set: " + user)
    return conn.sadd("voted:" + article, user)
    
def internal_article_vote(conn, article):
    conn.zincrby("score:", constants.VOTE_SCORE, article)
    conn.hincrby(article, "votes", 1)

import redis
conn = redis.Redis(db=1)
print("voting...")
article_vote(conn, "user:417525", "article:100408")

