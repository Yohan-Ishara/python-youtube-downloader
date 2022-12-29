from pytube import YouTube


def download_video(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print('Cannot fount video')
    print('Download Completed')


link = input('Put your link here: ')
download_video(link)
