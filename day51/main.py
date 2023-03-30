"""
Project Speed Twitter Complaint Bot
"""
from twitter_bot import InternetSpeedTwitterBot


def main():
    bot = InternetSpeedTwitterBot()
    
    bot.check_internet_and_tweet()
    

if __name__ == '__main__':
    main()

