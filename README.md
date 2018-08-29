# park.io
Domain search via [park.io](park.io).

I use this script pretty often; they have some rare domain names. Python 3.7.

An example:
```
$ python
>>> import parkio
>>> n = parkio.names()
>>> n[:5]  # first 5, alphabetical
['0dr0px.me', '0x86.me', '1995parham.me', '1kw.me', '1portal.io']
>>> sorted(n, key=len)[:5]  # shortest 5 results
['xj.ag', '26.gg', 'fu.je', 'qa.je', 'qb.je']
>>> [x for x in n if 'vote' in x]  # search
['virtualvote.me', 'virtuvote.me', 'votecoin.io', 'vote4joe.me']
>>> # etc.
```
