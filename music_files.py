import sys
import toml
import musicbrainzngs
import musicbrainzngs as m
import musicbrainzngs as mb

def init():
	mb.set_useragent("My Crazy Music App", "3.7", "http://d34d.net/music")

def system_example():
	flac_cmd = 'flac ...'
	r = system(flac_cmd)
	if r:
		failure(r, "error encoding %s" % outname)
		system("touch '%s/FAILURE'" % mp3_dir)
	return 0

def test_mb():
	# If you plan to submit data, authenticate
	#musicbrainzngs.auth("user", "password")

	#musicbrainzngs.set_hostname("beta.musicbrainz.org")

	result = musicbrainzngs.search_artists(artist="xx", type="group",
										   country="GB")
	for artist in result['artist-list']:
		print(u"{id}: {name}".format(id=artist['id'], name=artist["name"]))


def test_mb2():
	m.set_useragent("My Crazy Music App", "3.7", "http://d34d.net/music")
	print(m.get_artist_by_id("952a4205-023d-4235-897c-6fdb6f58dfaa", []))
	#print(m.get_label_by_id("aab2e720-bdd2-4565-afc2-460743585f16"))
	#print(m.get_release_by_id("e94757ff-2655-4690-b369-4012beba6114"))
	#print(m.get_release_group_by_id("9377d65d-ffd5-35d6-b64d-43f86ef9188d"))
	#print(m.get_recording_by_id("cb4d4d70-930c-4d1a-a157-776de18be66a"))
	#print(m.get_work_by_id("7e48685c-72dd-3a8b-9274-4777efb2aa75"))

	#print(m.get_releases_by_discid("BG.iuI50.qn1DOBAWIk8fUYoeHM-"))
	#print(m.get_recordings_by_isrc("GBAYE9300106"))

	m.auth("", "")
	#m.submit_barcodes({"e94757ff-2655-4690-b369-4012beba6114": "9421021463277"})
	#m.submit_tags(recording_tags={"cb4d4d70-930c-4d1a-a157-776de18be66a":["these", "are", "my", "tags"]})
	#m.submit_tags(artist_tags={"952a4205-023d-4235-897c-6fdb6f58dfaa":["NZ", "twee"]})

	#m.submit_ratings(recording_ratings={"cb4d4d70-930c-4d1a-a157-776de18be66a":20})

def main():
	print("hey %s" % sys.argv[0])
	d = toml.load("settings.toml")
	print(d)
	init()
	test_mb()

if __name__ == "__main__":
	main()


