from youtube_transcript_api import YouTubeTranscriptApi
from gilas import plist

ytt_api = YouTubeTranscriptApi()

# Replace 'VIDEO_ID' with the actual video ID (e.g., from https://www.youtube.com/watch?v=VIDEO_ID)
def get_transcript():
  video_id = "wTT8QaE0nnw"
  transcript = ytt_api.fetch(video_id).to_raw_data()

  return "".join([i["text"] for i in transcript])

    