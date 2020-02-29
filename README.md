# article-vote
这是一个非常简单的文章投票的工程，提供了文章分组、文章投票和按时间或者评分给出文章排行榜。
至于需求和思路，大都是参考《Redis实战》一书所写的demo，主要为了实践redis。

## Redis存储说明
* `time:` ，zset结构，存储文章的发布时间
* `score:` ，zset结构，存储文章的分数
* `votes:#{articleId}` ，set结构，某篇文章的投票用户
* `article:{articleId}` ，hash结构，某篇文章的元信息