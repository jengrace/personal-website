import os
from django.shortcuts import render, redirect
from django.http import HttpResponse

from jengrace.mainpage.control import Control


from twitter import TweepyInterface

twitter = TweepyInterface()

control = Control()


def homepage(request):
    if request.method == 'GET':
        title = 'Jennifer Grace'
        if 'error' in request.GET:
            error = request.GET['error']
            out = render(request, 'homepage.html', {'title': title, 'error': error})
        else:
            out = render(request, 'homepage.html', {'title': title})
        return out
    elif request.method == 'POST':
        cookie_id = request.COOKIES['csrftoken']
        action = request.POST['action']
        text = request.POST['text']
        if control.detectBannedWord(text):
            return redirect('/?error=Inappropiate Comment')
        control.saveUserComments(text)
        if len(text) >= 5:
            tweet_list = twitter.retrieveSearchedTweets(text)
            if len(tweet_list) > 0:
                control.saveTweet(tweet_list[0], text)
        return redirect('/comments')


def blog(request):
    bio = 'Blog'
    out = render(request, 'blog.html', {'title': bio})
    return out


def comments(request):
    if request.method == 'GET':
        title = 'Comments'
        usercomments = control.retrieveUserComments()
        tweet = control.retrieveTweetsFromDb()
        out = render(request, 'comments.html', {'title': title, 'ucomments': usercomments, 'tweets': tweet})
    return out


def reset(request):
    if request.method == 'GET':
        if request.GET['password'] == os.environ["RESET_PASSWORD"]:
            control.reset_db()
    return HttpResponse('Database reset')
