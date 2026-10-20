from datetime import datetime
import boto3
import pandas as pd


def run_twitter_etl():
  fake_tweets = [
      {
          "user": "elonmusk",
          "text": (
              "Starship orbital flight test and booster catch scheduled for"
              " next week!"
          ),
          "favorite_count": 142000,
          "retweet_count": 21000,
          "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      },
      {
          "user": "elonmusk",
          "text": "Grok AI update is rolling out globally with new features.",
          "favorite_count": 89000,
          "retweet_count": 11500,
          "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      },
  ]

  df = pd.DataFrame(fake_tweets)
  file_name = "elon_musk_twitter_data.csv"
  df.to_csv(file_name, index=False)

  # Upload directly using boto3 (leveraging your EC2 IAM role permissions)
  s3 = boto3.client("s3", region_name="eu-north-1")
  s3.upload_file(file_name, "zenithpro-airflow-bucket", file_name)
  print("ETL Pipeline executed successfully and uploaded to S3 via boto3!"),
  print("ETL Pipeline executed successfully and saved to S3!")