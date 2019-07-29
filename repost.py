import praw
from praw.models import MoreComments
import time

reddit = praw.Reddit(client_id='clientid',
                     client_secret='clientsecret',
                     password='Password',
                     user_agent='NameOFBot bot.',
                     username='Username')
botMessage = "\n^^I ^^am ^^a ^^bot ^^and ^^this ^^message ^^was ^^performed ^^automatically. ^^If ^^you ^^have ^^an ^^issue ^^please ^^send ^^me ^^a ^^PM!"
counter = 0
dupeList = ""
i = 6
while i != 0:
    alreadyCommented = False
    for submission in reddit.subreddit('all').new(limit=40):
        for x in submission.comments:
            if isinstance(x, MoreComments):
                continue
            if x.author == "Username":
                alreadyCommented = True
        if alreadyCommented is True:
            pass
        else:
            for duplicates in submission.duplicates():
                if duplicates.subreddit == submission.subreddit:
                    counter += 1
                    dupeList += "[" + duplicates.title + "](" + duplicates.permalink + ") | " + str(duplicates.score) + "\n"
            if counter > 0:
                dupeMessage = "This link has been posted **" + str(counter) + "** times in this subreddit!\n\nFor more context please check out the links below: \n\n\nSubmission | Points\n:--|:-:\n" + dupeList + "\n\n\n---\n\n\n" + botMessage
                try:
                    submission.reply(dupeMessage)
                except:
                    pass
            counter = 0
            dupeList = ""
        alreadyCommented = False
        time.sleep(7)
