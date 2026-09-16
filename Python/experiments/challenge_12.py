def insert_sponsored_post(feed, post_title):
    feed.insert(2, post_title)
    return feed

post_titles = ['Cheap mouse', 'Man cutting hair', 'Playing fortnite', 'In a relationship']
new_post = input('Enter your post title: ').strip()

updated_feed = insert_sponsored_post(post_titles, new_post)
formatted_posts = ', '.join(f'{post}' for post in updated_feed)

print(f'Added post title: {new_post}\n'
      f'Feed posts: {formatted_posts}')
