#!/usr/bin/python3
import os
from tinytag import TinyTag

class Tagger:
	def __init__(self, path, quiet=False):
		self.path = path
		self.quiet = quiet
		self.global_dic = {}

	def scan_audio_files(self):
		for dirpath,_,filenames in os.walk(self.path):
			for f in filenames:
				filepath = os.path.abspath(os.path.join(dirpath, f))
				if not self.quiet:
					print("Scanning file:", filepath)
				try:
					tag = TinyTag.get(filepath)
					artist = tag.artist
					album = tag.album
					title = tag.title
					track = tag.track
					if not artist or not album:
						if not self.quiet:
							print("WARNING: tag not available, skipping file...")
					else:
						dic = {"file": f, "artist": artist, "album": album, "title": title, "track": track}
						self.global_dic[filepath] = dic
						if not self.quiet:
							print("ARSTIST:", artist)
							print("ALBUM:", album)
							print("TITLE:", title)
							print("TRACK:", track)
							print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
				except:
					if not self.quiet:
						print("WARNING: no supported tag, skipping file...")
						print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

	def get_scanned_dic(self):
		return self.global_dic
