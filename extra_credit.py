def topKFrequent(self, nums, k):
  values = list()
  frequent = list()
  counts = dict()
  for num in nums:
    if num in counts:
      counts[num] = counts[num] + 1
    else:
      counts[num] = 1
      frequent.append(num)
  total = list()
  for value in frequent:
    total.append(counts[value])
  for i in range(k):
    indx = total.index(max(total))
    values.append(frequent[indx])
    total[indx] = 0
  return values


def kSmallestPairs(self, nums1, nums2, k):
  if len(nums1) == 0 or len(nums2) == 0:
    return []
  pairs = list()
  for value in nums1:
    counter = 0
    while counter < len(nums2):
      pairs.append([value, nums2[counter]])
      counter += 1
  def sort_key(elem):
    return elem[0] + elem[1]
  pairs= sorted(pairs, key=sort_key)
  return pairs[0:k]

class User:


  def __init__(self, userId):
    self.id = userId
    self.following = set()
    self.following.add(userId)
    self.tweets = list()


  def follow(self, userId):
    self.following.add(userId)


  def unfollow(self, userId):
    if userId in self.following and userId != self.id:
      self.following.remove(userId)
            

  def post(self, tweetId, timestamp):
    tweet = Tweet(tweetId, timestamp)
    self.tweets.append(tweet)


class Tweet:
    
    
  def __init__(self, tweetId, timestamp):
    self.id = tweetId
    self.timestamp = timestamp



class Twitter:

  def __init__(self):
    self.timestamp = 0
    self.users = dict()
        

  def postTweet(self, userId, tweetId):
    if userId in self.users:
      self.users[userId].post(tweetId, self.timestamp)
    else:
      self.users[userId] = User(userId)
      self.users[userId].post(tweetId, self.timestamp)
    self.timestamp += 1
        
        

  def getNewsFeed(self, userId):
    if userId not in self.users:
      return []
    every = list()
    for person in self.users[userId].following:
      for tweet in self.users[person].tweets:
          every.append([tweet.id, tweet.timestamp])
    def sort_key(elem):
      return elem[1]
    every = sorted(every, key=sort_key, reverse=True)
    recent = list()
    if len(every) > 10:
      every = every[0:10]
    else: 
      every = every[0:len(every)]
    for element in every:
      recent.append(element[0])
    return recent


  def follow(self, followerId, followeeId):
    if followerId not in self.users:
      self.users[followerId] = User(followerId)
    if followeeId not in self.users:
      self.users[followeeId] = User(followeeId)
    self.users[followerId].follow(followeeId)
        

  def unfollow(self, followerId, followeeId):
    if followerId not in self.users:
      self.users[followerId] = User(followerId)
    if followeeId not in self.users:
      self.users[followeeId] = User(followeeId)
    if followeeId in self.users[followerId].following:
      self.users[followerId].unfollow(followeeId)
