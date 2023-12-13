from googleapiclient.discovery import build
import os

def youtube_search(api_key, search_term, max_results):
    # Build a service object for interacting with the API
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Execute the search request
    search_response = youtube.search().list(
        q=search_term,
        part='id,snippet',
        maxResults=max_results,
        type='video'
    ).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of matching videos.
    for search_result in search_response.get('items', []):
        videos.append({
            'title': search_result['snippet']['title'],
            'videoId': id_to_embed_url(search_result['id']['videoId']),
            'description': search_result['snippet']['description'],
            'publishedAt': search_result['snippet']['publishedAt'],
            'channelTitle': search_result['snippet']['channelTitle']

        })

    return videos


def convert_to_embed_url(youtube_url):
    video_id = youtube_url.split("watch?v=")[1]
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    return embed_url

def id_to_embed_url(video_id):
    # video_id = youtube_url.split("watch?v=")[1]
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    return embed_url
# Example usage
# video_links = ["https://www.youtube.com/watch?v=VIDEO_ID1", "https://www.youtube.com/watch?v=VIDEO_ID2"]
# embed_links = [convert_to_embed_url(url) for url in video_links]

# for link in embed_links:
#     print(link)

# if __name__ == '__main__':
#     # Replace 'YOUR_API_KEY' with your actual API key
#     api_key = 'AIzaSyDOx6_xYze6XCB0PHwXJlWecMDTPP1krZ8'
#     search_query = 'Kwamé house battle'

#     results, ids = youtube_search(api_key, search_query)
#     # print(results)
#     embed_links = [id_to_embed_url(id) for id in ids]

#     for embed in embed_links:
#         print(embed)
    # for embed in embed_links:
    #     print(embed)