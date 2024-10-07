# api_key api_key = "AIzaSyAlFcC7d6_JfcskrdnP7eQt2yOe4Esln44"
# search_word: "search word"
# Video Categroies: Education ("27"), Science & Technologie ("28"), People & Blogs ("22"), Howto & Style ("26")
# published: "YYYY-MM-DD"
# location: "latitude, longitute"
# radius: "miles"

def youtube_search(api_key, search_word, category_ids, published_after, published_before, location, radius):

    from googleapiclient.discovery import build
    import pandas as pd
    from IPython.display import JSON
    from pprint import pprint
    
    api_key = api_key
    
    api_service_name = "youtube"
    api_version = "v3"
        
    # API client   
    youtube = build(
        api_service_name, api_version, developerKey=api_key)
             
    category_ids = category_ids
    published_after = published_after  # Start of time range
    published_before = published_before  # End of time range


    # Calling youtube.search function
    all_results = []  
    
    for category_id in category_ids:
        # Initial request for each category
        request = youtube.search().list(
            part="snippet",
            location = location,
            locationRadius = radius,
            type="video",
            order="date",
            maxResults=50,
            q=search_word,  
            videoCategoryId=category_id,  
            publishedAfter=published_after,
            publishedBefore=published_before
        )
        response = request.execute()
        all_results.extend(response['items'])  
    
        # Pagination
        while 'nextPageToken' in response:
            request = youtube.search().list(
                part="snippet",
                location = "38.399588, -77.795914",
                locationRadius = "500mi",
                type="video",
                order="date",
                maxResults=50,
                q="health",
                videoCategoryId=category_id,
                publishedAfter=published_after,
                publishedBefore=published_before,
                pageToken=response['nextPageToken']  # Use the next page token
            )
            response = request.execute()
            all_results.extend(response['items'])  # Add paginated results to the list
    
    # Extracting videoIDs
    all_ids = [entry['id']['videoId'] for entry in all_results]

    # Iterating through the 'all_vids' list in steps of 50
    split_vids = []
    for i in range(0, len(all_ids), 50):
        split_vids.append(all_ids[i:i + 50])


    # Calling youtube.video function, looping through each list of video IDs
    responses = []
    for video_ids in split_vids:
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=video_ids
        )
        response = request.execute()
        responses.append(response)

    # Lists to store extracted data
    channel_title_list = []
    title_list = []
    published_at_list = []
    tags_list = []
    like_count_list = []
    view_count_list = []
    comment_count_list = []
    
    # Looping through each response in the list of responses
    for response in responses:
        # Accessing the 'items' in each response
        for item in response['items']:
            # Extracting items out of JSON
            channel_title = item['snippet']['channelTitle']
            title = item['snippet']['title']
            published_at = item['snippet']['publishedAt']
            tags = item['snippet'].get('tags', [])  # Use .get to handle missing tags
    
            # Appending the items into lists
            channel_title_list.append(channel_title)
            title_list.append(title)
            published_at_list.append(published_at)
            tags_list.append(tags)
    
            # Extracting statistics
            statistics = item.get('statistics', {})
            like_count = statistics.get('likeCount', 'N/A')  # Use .get to handle missing keys
            view_count = statistics.get('viewCount', 'N/A')  # Use .get to handle missing keys
            comment_count = statistics.get('commentCount', 'N/A')  # Use .get to handle missing keys
    
            # Appending statistics into lists
            like_count_list.append(like_count)
            view_count_list.append(view_count)
            comment_count_list.append(comment_count)

    # like count and view count ratio
    # ratio between 0 and 1, the higer the better the ratio, if > 0 likes are mor than views 
    # equation = 1 - ((view_count - like_count) / view_count)
    # basically the percentage of viewers that liked the video
    
    view_count_list_int = [float(count) if count != 'N/A' else 0 for count in view_count_list]
    like_count_list_int = [float(count) if count != 'N/A' else 0 for count in like_count_list]
    view_like_ratios = []
    
    for view_count, like_count in zip(view_count_list_int, like_count_list_int):
        if view_count != 0:
            view_like_ratio = (1 - ((view_count - like_count) / view_count))
        else:
            view_like_ratio = 0
        view_like_ratios.append(view_like_ratio)

    view_like_ratios_round = [round(num, 2) for num in view_like_ratios]
    
   # Creating dictionary and pd table
    data = {
        'title': title_list,
        'channel_title': channel_title_list,
        'like_count': like_count_list,
        'view_count': view_count_list,
        'comment_count': comment_count_list,
        'view_like_ratio': view_like_ratios_round,
        'published_at': published_at_list
    }
    
    df = pd.DataFrame(data)
    df = df.sort_values(by='published_at', ascending=True)
    
    return df