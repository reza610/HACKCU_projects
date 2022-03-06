from cProfile import label
from posixpath import split
#from tracemalloc import start
from twarc import Twarc2
from http import client
from re import search
import matplotlib.pyplot as plt
import matplotlib

#Authors: Andrew Philips, Reza Naiman, Murilo Tibana, Kevin O'Brien
#purpose: take hashtag input and generate bar graph for tweets containing the hashtag over the last week. 
#tweet the graph and mention the account of the person who asked 

#Take user inputs:
client = Twarc2(bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKKeZwEAAAAAED4xDTh6fcuhx4KgQFGreEh%2FcR8%3DkLDaoGKJJJ9umtQKJeA83dhbE8VrMHnvmPSFsHWYzWWTBTVc9B')
hashtag = input("Please enter a hashtag")
"\n"
user_name = input("Please enter your username")
"\n"
query =  hashtag
global name
name = "@" + user_name

#find the tweets for the relevant query term 
search_tweets = client.counts_recent(query = query, granularity = "day")

for page in search_tweets:
        data = page['data']
        break

day = []
tweet_counts = []
likes = []

#initialize lists to contain the tweet statistics for each day 
for k in data:
    day.append(k['start'][:30])
    tweet_counts.append(k['tweet_count'])

short_list = []

for i in range(len(day)):
    day_list = day[i].split('-')
    month = day_list[1]
    #print("day_list", day_list[2])
    date = day_list[2].split('T')[0]
    #print("date", date)
    #print("Month", month)
    #print("Day", day)
    shortday = month + '-' + date
    #print("shortday", shortday)
    #print(day_list)
    # day[i] = day[i][1] + '-' + day[i][2]
    short_list.append(shortday)

#print(day)
#graph = go.Figure(data = [go.Bar(x = day, y = tweet_counts)])

#graph the data 
graph = plt.bar(short_list, tweet_counts )
#matplotlib.rc('xtick', fontsize = 5)
plt.xticks(rotation = 45)
plt.autoscale()
plt.show()

#save the figure locally 
plt.savefig("graph1.png")
global image
image = "/Users/rezanaiman/Documents/hackcu8/graph1.png"