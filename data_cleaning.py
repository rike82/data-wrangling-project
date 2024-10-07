def data_cleaning(df):

    import pandas as pd
    
    video_table['published_at'] = pd.to_datetime(video_table['published_at'])
    video_table['view_like_ratio'] = pd.to_numeric(video_table['view_like_ratio'], errors='coerce')
    video_table['view_count'] = pd.to_numeric(video_table['view_count'], errors='coerce')
    video_table['comment_count'] = pd.to_numeric(video_table['comment_count'], errors='coerce')
    
    # Extract year and month
    video_table['year_month'] = video_table['published_at'].dt.to_period('M')  # This gives 'YYYY-MM' format
    
    # Group by year and month, then summarize columns using sum, mean, etc.
    summary = video_table.groupby('year_month').agg({
        'title': 'count',
        'view_count': 'sum',
        'view_like_ratio': 'mean',
        'comment_count': 'sum',
    })
    
    return summary