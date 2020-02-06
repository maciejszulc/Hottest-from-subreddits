#!/usr/local/bin/python

import os
import praw
import smtplib
import ssl
import email
import time, datetime


print("Welcome!")

reddit = praw.Reddit(
    client_id="client_id",
    client_secret="client_secret",
    password="reddit_password",
    user_agent="Hottest from selected subs - v.01 (by u/hardlowcore)",
    username="hardlowcore"
)

reddit.read_only = True

subs = ['netsec', 'hmmm', 'internet_funeral']

hottest = []

for i in range(len(subs)):
    for submission in reddit.subreddit(subs[i]).hot(limit=10):
        hottest.append(submission.title)

try:
    with open('logs.txt', 'a') as f:
        f.write(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')) + '\n Hottest from your favourite subreddits:\n {}'.format(enumerate(hottest)))
        f.close()
    print("Log saved succesfully!")

except Exception:
    print("Something went terribly wrong")

port = 465

password = "mail_password"

sender_mail = "sender@mail.com"

receiver_mail = "receiver@mail.com"

message = """\
    Subject: Your daily newsletter from reddit

    Hottest from your favourite subreddits:\n {}
    
    """.format(enumerate(hottest))

stmtp_server = "smptp.gmail.com"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(stmtp_server, port, context=context) as server:
    
    server.login(sender_mail, password)
 
    server.sendmail(sender_mail, receiver_mail, message)
