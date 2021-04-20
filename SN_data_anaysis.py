import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader

mySoccerNetDownloader = SoccerNetDownloader(
    LocalDirectory="/path/to/SoccerNet")

mySoccerNetDownloader.downloadGames(files=["Labels-v2.json"], split=["train","valid","test"])