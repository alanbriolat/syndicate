=========
API notes
=========

A summary of interacting with various APIs to provide the "activity stream" we want.

github
======

What we want from github is a list of a user's activity across everything.  In fact, github already 
has a "public activity" Atom feed (e.g. https://github.com/alanbriolat.atom), and this can be 
accessed in JSON format by changing the extension (https://github.com/alanbriolat.json).

Steam
=====

To start with, what we want is an event stream of a user's Steam achievements.  This information is 
available on the Steam Community website - the information for most pages can be accessed in XML 
format by appending ``xml=1`` as a GET parameter, e.g.  
http://steamcommunity.com/id/feedmeammo/games?tab=all&xml=1.  This particular example is a list of 
all games that the user owns, and from each of those the ``statsLink`` can be extracted and modified 
to get the achievements for a particular game, e.g.  
http://steamcommunity.com/id/feedmeammo/stats/L4D2?tab=achievements&xml=1

Twitter
=======

Twitter make it easy to get a user's timeline in JSON, if you can find your way around the API 
documentation.  The simplest approach: 
https://api.twitter.com/1/statuses/user_timeline.json?screen_name=alanbriolat.

Facebook
========

Facebook's API is simple and well-documented (http://developers.facebook.com/docs/reference/api/), 
but they required an OAuth token to access most interesting information.  The activity feed is 
simply http://graph.facebook.com/alanbriolat/feed?access_token=xxxxxxxxx

Google+
=======

There is no official Google+ API yet, however several people have hacked together APIs, for example 
https://github.com/pct/python-googleplusapi.  This should be sufficient to get the public activity 
stream.

Disqus
======

Why not include any comments made on other stuff on the internet?  Disqus maintains a Python API for 
their service at https://github.com/disqus/disqus-python.
