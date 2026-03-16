from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()

# https://www.youtube.com/watch?v=wTT8QaE0nnw&t=2s
# https://youtu.be/wTT8QaE0nnw?si=9nWDXr4T-1R7UUNE
def get_transcript(url):
  if "youtube" in url: 
    video_id = url[url.index("=")+1:url.index("&t")]
  if "youtu.be" in url:
    video_id = url[url.index(".be/") + 4:url.index("?si")]

  transcript = ytt_api.fetch(video_id).to_raw_data()

  return "".join([i["text"] for i in transcript])

    