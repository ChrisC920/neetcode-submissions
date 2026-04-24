class Twitter:
    # userIds -> followeeIds | followMap
    # userIds -> (count, tweetId) | tweetMap
    
    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followMap[userId].add(userId)
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for user in self.followMap[userId]:
            for tweet in self.tweetMap[user]:
                res.append(tweet)
        res.sort(reverse=True)
        if len(res) > 10:
            res = res[:10]
        return [x[1] for x in res]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.followMap[followerId]:
            return
        self.followMap[followerId].remove(followeeId)
