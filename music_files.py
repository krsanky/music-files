import sys
from pathlib import Path
import toml
import musicbrainzngs
import musicbrainzngs as m
import musicbrainzngs as mb
import discogs_1 as dt
from mediafile import MediaFile 

def init():
	mb.set_useragent("My Crazy Music App", "3.7", "http://d34d.net/music")

def system_example():
	flac_cmd = 'flac ...'
	r = system(flac_cmd)
	if r:
		failure(r, "error encoding %s" % outname)
		system("touch '%s/FAILURE'" % mp3_dir)
	return 0

def find_capt_n_resp():
	result = musicbrainzngs.search_artists(artist="Captain Not Responsible", type="group")
	return result

def test_mb2():
	init()
	print(m.get_artist_by_id("952a4205-023d-4235-897c-6fdb6f58dfaa", []))
	#print(m.get_label_by_id("aab2e720-bdd2-4565-afc2-460743585f16"))
	#print(m.get_release_by_id("e94757ff-2655-4690-b369-4012beba6114"))
	#print(m.get_release_group_by_id("9377d65d-ffd5-35d6-b64d-43f86ef9188d"))
	#print(m.get_recording_by_id("cb4d4d70-930c-4d1a-a157-776de18be66a"))
	#print(m.get_work_by_id("7e48685c-72dd-3a8b-9274-4777efb2aa75"))

	#print(m.get_releases_by_discid("BG.iuI50.qn1DOBAWIk8fUYoeHM-"))
	#print(m.get_recordings_by_isrc("GBAYE9300106"))

def _tag_file(f, artist, album, trknum, songname):
	print("f:{} a:{} album:{} trknum:{} song:{}".format(f, artist, album, trknum, songname))
	mf = MediaFile(f)
	mf.artist = artist
	mf.albumartist = artist
	mf.album = album
	mf.track = trknum
	mf.title = songname
	mf.save()

def tag_capt_n_resp_ship_of_fools():
	"""
	Out[4]: <Artist 779504 'Captain Not Responsible'>
	Out[6]: <Release 1902686 'Captain Not Responsible'>
	Out[7]: <Release 1859831 'Ship Of Fools'>
	"""
	d = dt.init()
	a = d.artist(779504)
	release = a.releases[2] # this is probably bad, should match on album name
	tracklist = release.tracklist
	print("tracklist len:%d" % len(tracklist))
	srcd = "SOURCE/Capt-n-resp/"
	#srcd = "SOURCE/cap-n-resp/" #mp3

	filesd = Path(srcd)
	for file, track in zip(filesd.iterdir(), tracklist):
		print("file:{} trk:{} {}".format(file.name, track.position, track.title))
		_tag_file(file, a.name, release.title, track.position, track.title)

	return tracklist

def main():
	print("hey %s" % sys.argv[0])
	d = toml.load("settings.toml")
	print(d)
	init()

	tag_capt_n_resp_ship_of_fools()

if __name__ == "__main__":
	main()


