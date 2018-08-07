import os
import sqlite3
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt

def parse(url):
	try:
		parsed_url_components = url.split('//')
		sublevel_split = parsed_url_components[1].split('/', 1)
		domain = sublevel_split[0].replace("www.", "")
		return domain
	except IndexError:
		print("URL format error!")

def analyze(results):

	prompt = input("[.] Type <c> to print or <p> to plot\n[>] ")

	if prompt == "c":
		for site, count in list(sites_count_sorted.items()):
			print(site, count)
	elif prompt == "p":
		plt.bar(list(range(len(results))), list(results.values()), align='edge')
		plt.xticks(rotation=45)
		plt.xticks(list(range(len(results))), list(results.keys()))
		plt.show()
	else:
		print("[.] Uh?")
		quit()