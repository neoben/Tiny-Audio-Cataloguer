#!/usr/bin/python3
import os
from pathlib import Path

class Cataloguer:
	def __init__(self, path, dic, quiet=False):
		self.path = path
		self.dic = dic
		self.quiet = quiet

	def create_catalogue(self):
		for key, value in self.dic.items():
			d = value
			filepath = key
			file = d["file"]
			artist = d["artist"]
			album = d["album"]
			track = d["track"]
			
			artist_path = self.path + "/" + artist
			try:
				if not self.quiet:
					print("Create artist path:", artist_path)
				Path(artist_path).mkdir(parents=True, exist_ok=True)
			except OSError as e:
				print("ERROR: unable to create dir - errno:", e.errno)
			
			album_path = artist_path + "/" + album
			try:
				if not self.quiet:
					print("Create album path:", album_path)
				Path(album_path).mkdir(parents=True, exist_ok=True)
			except OSError as e:
				print("ERROR: unable to create dir - errno:", e.errno)

			# Rename file with track number (if any)
			if track:
				filename = track + "_" + file
			else:
				filename = file

			movepath = album_path + "/" + filename
			try:
				if not self.quiet:
					print("Moving", filepath, "to", movepath)
				os.rename(filepath, movepath)
			except:
				print("ERROR: unable to move file", filepath, "to", movepath)