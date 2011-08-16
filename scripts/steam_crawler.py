#!/usr/bin/env python
import os.path
import sys
import argparse
import logging
logging.basicConfig(level=logging.DEBUG)

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '..'))

from syndicate.sources.steam import SteamCrawler

parser = argparse.ArgumentParser()
parser.add_argument('--prefix', default='data/steam/',
        help='Output path prefix (default: %(default)s)')
parser.add_argument('steamid', help='Steam user ID')
args = parser.parse_args()

crawler = SteamCrawler(args.steamid, args.prefix)
crawler.crawl()
