***USING THE CRAWLER***
To gather our test data we have a function crawl() in hits.py, which is a 
modification of the file given to us by Jeff on the Google group.
To use it, you must first provide yor own authentication, then
you simply use the command "python crawl.py 'some search query'"
It will then gather 100 users relevant to the search query,
and 40 of their latest tweets.

It outputs these files to standard output, but they can easily be
routed to a file.

Now, these tweets are formatted differently compared to the mars landing
tweets we were provided for homeworks. These tweets are actually in the python
dictionary format. Because of this, our main algorithm currently uses the ast
python module to make a literal evaluation of the tweets in the function
read_tweets(). Other than this, the tweets operate the same as in the homeworks.

***THE ALGORITHM***
hits.py creates an adjacency matrix of all the users in a file that is fed to
it. The matrix includes users who have tweets in the corpus as well as any users
that are merely mentioned in the corpus. This means that 'adjacency' is defined
as 'mentioned by'.

Using the adjacency matrix, the algorithm computes a hubs and authorities score,
which are both simply printed out (though using numpy's truncated print format if the
resulting vectors are too large). It should be noted that these two values ARE the
corpus's hub and authority vectors.
