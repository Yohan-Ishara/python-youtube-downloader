from pytube import YouTube


def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print('Cannot fount video')
    print('Download Completed')

link = input('Put your link here: ')
download(link)
