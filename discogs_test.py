import discogs_client

_token = 'HNKSqzqfBCsUthQIToWwyfgdYUrWuEEaxmqqOHYz'

def init():
	d = discogs_client.Client('PeoplesApll/3.7', user_token=_token)
	return d

def search_test():
	d = init()
	#results = d.search('Capt By Night', type='release')
	#results = d.search(artist='Captain Not Responsible', type='artist')
	#results = d.search('Captain Not Responsible', type='artist')
	results = d.search('So Much Hate', type='artist')
	return results

def so_much_hate__seein_red():
	"""
In [18]: smh1 = D.release(3658445)                                                                                                                             

In [19]: smh1.tracklist                                                                                                                                        
Out[19]: 
[<Track '1' 'Jerk'>,
 <Track '2' 'Warsong'>,
...
 <Track '14' 'Progress'>,
 <Track '15' 'Purple Haze'>]

In [20]: t = smh1.tracklist[0]                                                                                                                                 
In [21]: t.title                                                                                                                                               
Out[21]: 'Jerk'
In [22]: t.position                                                                                                                                            
Out[22]: '1'
	"""
	D = init()
	smh1 = D.release(3658445)                                                                                                                             
	for t in smh1.tracklist:
		print("TRK:{} {}".format(t.position, t.title))

if __name__ == "__main__":
	d = init()


