import csv
import snscrape.modules.twitter as sntwitter

# Set the query string
query = 'Kereta Cepat Jakarta-Bandung'

# Set the number of tweets you want to scrape
num_tweets = 10

# Create a list to store the tweets
tweets = []

# Use the snscrape TwitterSearchScraper to get tweets based on the query
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query + ' lang:id').get_items()):
    if i >= num_tweets:
        break
    tweets.append({
        'id': tweet.id,
        'content': tweet.content,
        'date': tweet.date,
        'username': tweet.user.username
    })

# Specify the CSV file path
csv_file_path = 'kereta_cepata_jakarta_bandung_tweets.csv'

# Write the scraped tweets to the CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'content', 'date', 'username']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for tweet in tweets:
        writer.writerow(tweet)

print(f"Scraped tweets about 'Kereta Cepat Jakarta-Bandung' have been saved to {csv_file_path}")
