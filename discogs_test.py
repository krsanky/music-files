
_token = 'qwdqwdqwdqwdqwd'  

def init():
	import discogs_client
	d = discogs_client.Client('PeoplesApll/3.7', user_token=_token)
	return d

def search_test():
	d = init()
	#results = d.search('Capt By Night', type='release')
	#results = d.search(artist='Captain Not Responsible', type='artist')
	results = d.search('Captain Not Responsible', type='artist')
	return results

if __name__ == "__main__":
	d = init()


