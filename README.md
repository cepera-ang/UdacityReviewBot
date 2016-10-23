# UdacityReviewBot
This Telegram bot utilizes Udacity Review API to fetch new submissions for review.
It will query Udacity servers using latest API version and notify in Telegram when new submission available.
It will have the following functionality (work in progress):
- Quering Udacity servers given your Reviewer token
- You may select which of the projects you certified for review to assign automatically
- Quering can be paused for given period of time
- Anything else?

#Usage

- Register you bot in Telegram [here]() and receive bot token.
- Create `UdacityReview_bot.token' file and paste your bot and reviewer API tokens each on separate lines.
- Run UdacityReviewBot.py
`python3 UdacityReviewBot.py`
- Add bot to your Telegram contacts and `/start`
- You are done!

