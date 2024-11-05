import yt_dlp

def download_video(url, output_path='.'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download completed!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ").strip()
    download_video(video_url)
