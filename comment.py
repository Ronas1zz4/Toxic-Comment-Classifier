# pip install google-api-python-client
import googleapiclient.discovery
import pandas as pd
import os

google_api_key = os.getenv('GOOGLE_API_KEY')

api_service_name = "youtube"
api_version = "v3"


youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="WNrB1Q9Rry0",
    maxResults=100
)
response = request.execute()

comments = []

for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']
    comments.append([
        comment['authorDisplayName'],
        comment['publishedAt'],
        comment['updatedAt'],
        comment['likeCount'],
        comment['textDisplay']
    ])

df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])
# df['text'] = df['text'].astype(str, errors='coerce')

df.head(10)
print(df)

