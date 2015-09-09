# if bot restarts, posts are not saved locally and bot will reply again
import praw
import time
r = praw.Reddit('subreddit commenting robo by /u/nachozombie v0.1')

def startup():
	r.login()
	
def target():
	x = 1
	prawWords = []
	words = input("How many keywords or phrases are you looking for? ")
	while x <= int(words):
		print("Enter the keyword or phrase that you want to look out for. Phrase/Word #", x)
		interests  = input()
		prawWords.append(interests)
		x = x + 1

def get_subreddit():
	sub = input("Subreddit: ")
	return sub
	
def get_comment():
	response = input("Comment: ")
	return response
	
def loop():	
	already_done = []
	while True:
		subreddit = r.get_subreddit(get_subreddit)
		for submission in subreddit.get_new(limit = 5):
			if submission.id not in already_done:
				submission.add_comment(get_comment())
				already_done.append(submission.id)
	time.sleep(15)			
	
def main():
	startup()
	target()
	loop()
	
main()