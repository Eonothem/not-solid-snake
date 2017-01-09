import twitter
import markovify
import sched, time

s = sched.scheduler(time.time, time.sleep)

#
api = twitter.Api(consumer_key="[insert ck here]",
                  consumer_secret="[insert cs here]",
                  access_token_key="[insert tk here]",
                  access_token_secret="[insert ts here]")

file = open("SnakeTextData.txt")

text_model = markovify.Text(file.read())

def tweet():
	status = api.PostUpdate(text_model.make_short_sentence(140))
	s.enter(300,1,tweet)
	s.run()

def init():
	 tweet()

init()