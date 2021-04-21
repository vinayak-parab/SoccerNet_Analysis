from SoccerNet.Downloader import SoccerNetDownloader

mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="C:/Python_Projects/Master_Thesis/Dataset_Sample")

# Download SoccerNet labels and features
mySoccerNetDownloader.downloadGames(files=["Labels.json"], split=["train","valid","test"]) # download labels
mySoccerNetDownloader.downloadGames(files=["Labels-v2.json"], split=["train","valid","test"]) # download labels SN v2
mySoccerNetDownloader.downloadGames(files=["Labels-cameras.json"], split=["train","valid","test"]) # download labels for camera shot
mySoccerNetDownloader.downloadGames(files=["1_ResNET_TF2.npy", "2_ResNET_TF2.npy"], split=["train","valid","test"]) # download Features
mySoccerNetDownloader.downloadGames(files=["1_ResNET_TF2_PCA512.npy", "2_ResNET_TF2_PCA512.npy"], split=["train","valid","test"]) # download Features reduced with PCA

# Download SoccerNet videos (require password from NDA to download videos)
mySoccerNetDownloader.password = input("s0cc3rn3t\n")
mySoccerNetDownloader.downloadGames(files=["1.mkv", "2.mkv"], split=["train","valid","test"]) # download LQ Videos
mySoccerNetDownloader.downloadGames(files=["1_HQ.mkv", "2_HQ.mkv", "video.ini"], split=["train","valid","test"]) # download HQ Videos

# Download SoccerNet Challenge set (require password from NDA to download videos)
mySoccerNetDownloader.downloadGames(files=["1_ResNET_TF2.npy", "2_ResNET_TF2.npy"], split=["challenge"]) # download Features
mySoccerNetDownloader.downloadGames(files=["1_ResNET_TF2_PCA512.npy", "2_ResNET_TF2_PCA512.npy"], split=["challenge"]) # download Features reduced with PCA
mySoccerNetDownloader.downloadGames(files=["1.mkv", "2.mkv", "video.ini"], split=["challenge"]) # download LQ Videos (require password from NDA)
mySoccerNetDownloader.downloadGames(files=["1_HQ.mkv", "2_HQ.mkv", "video.ini"], split=["challenge"]) # download HQ Videos (require password from NDA)