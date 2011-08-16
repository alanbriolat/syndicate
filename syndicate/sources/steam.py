import os
import os.path
import glob
import logging
_log = logging.getLogger('syndicate.sources.steam')

from lxml import etree
import sqlobject as sql

from syndicate.util import fetch


class SteamCrawler(object):
    def __init__(self, steamid, prefix='steam/'):
        self._steamid = steamid
        self._prefix = prefix

        self.profile_url = 'http://steamcommunity.com/id/%s/?xml=1' % (steamid,)
        self.profile_file = prefix + steamid + '-profile.xml'
        self.gamelist_url = 'http://steamcommunity.com/id/%s/games?tab=all&xml=1' % (steamid,)
        self.gamelist_file = prefix + steamid + '-games.xml'

    def achievements_file(self, shortname):
        return self._prefix + self._steamid + '-achievements-' + shortname + '.xml'

    def crawl(self):
        dirname = os.path.abspath(os.path.dirname(self._prefix))
        if not os.path.exists(dirname):
            _log.debug('Creating directory %s' % (dirname,))
            os.makedirs(dirname)
        elif not os.path.isdir(dirname):
            raise Exception('%s not a directory' % (dirname,))

        fetch(self.profile_url, self.profile_file, _log.info)
        fetch(self.gamelist_url, self.gamelist_file, _log.info)
        gamelistxml = etree.parse(open(self.gamelist_file, 'r'))
        statlinks = [link.text for link in gamelistxml.xpath('/gamesList/games/game/statsLink')]
        for link in statlinks:
            shortname = link.rstrip('/').rsplit('/', 1)[1]
            link += '?tab=achievements&xml=1'
            fetch(link, self.achievements_file(shortname), _log.info)

    def process(self):
        for f in glob.iglob(self.achievements_file('*')):
            tree = etree.parse(open(f, 'r'))


class SteamGame(sql.SQLObject):
    shortname = sql.StringCol(unique=True)
    name = sql.StringCol()
    icon_url = sql.StringCol()
    logo_url = sql.StringCol()
    store_url = sql.StringCol()

    def from_etree(self, e):
        """Get instance from ``lxml.etree`` element, creating a new record if
        it doesn't already exist."""
        pass


class AchievementEvent(sql.SQLObject):
    game = sql.ForeignKey('SteamGame', cascade=True)
    apiname = sql.StringCol()
    achievementindex = sql.DatabaseIndex('game', 'apiname', unique=True)
    name = sql.StringCol()
    description = sql.StringCol()
    unlocked_at = sql.DateTimeCol()
