# importing regex and random libraries
import re
import random

class FemiChatBot:
  
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

  random_questions = (
        "Why are you here? ",
        "What do you like to do? ",
        "How’s your day going so far? ",
        "What’s your favorite food? ",
        "Do you have a favorite movie or series? ",
        "What hobbies do you enjoy the most? ",
        "If you could learn any skill instantly, what would it be? ",
        "What’s something new you tried recently? ",
        "If you were a superhero, what would your power be? ",
        "Would you rather fight 100 tiny robots or 1 giant chicken? ",
        "If animals could talk, which one would be the rudest? ",
        "Do you think robots like me should be allowed to tell jokes? "
    )

  def __init__(self):
    self.babble = {'describe_femi_intent': re.compile(r'\blearn\s+about\s+(femi|him)|who\s+femi|about\s+femi\b',re.IGNORECASE),
                        'fav_things_to_do': re.compile(r"\b(fav(?:ou)?rite|hobbies|likes?\s+(to\s+do)?)\b", re.IGNORECASE)
                            }

  def greet(self):
    name = input("What is your name ")
    will_help = input("Hi {}, I'm Femi's Chatbot. I'm here to entertain you. Say when, when ready to begin ".format(name))
    if will_help in self.negative_responses:
      print("Okay, goodbye")
      return 
    return self.chat()
  
  def make_exit(self, reply):
    words = reply.split()
    for word in words:
      if word in self.exit_commands:
        print('Ok, have a nice day!') 
        return True
    return False

  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      response = self.match_reply(reply) 
      print(response)  
      reply = input("Anything else? ").lower()  

  def match_reply(self, reply):
    for intent,regex_pattern in self.babble.items():
      found = re.search(regex_pattern,reply)
      if found and intent == 'describe_femi_intent': 
        return self.describe_femi_intent()
      elif found and intent == 'fav_things_to_do':
        return self.fav_things_to_do()
    return self.no_match_intent()

  def describe_femi_intent(self):
    responses = (
        "Femi is a hardworking guy. I'd know he built me! "
        "He wants to make the world a better place by building systems that help people.",
    )  
    return random.choice(responses)

  def fav_things_to_do(self):
    responses = (
        "He likes to watch movies and series, play games, and read books. "
        "He also finds happiness in learning about new developing technology.",
    )  
    return random.choice(responses)


  def no_match_intent(self):
    responses = ("Please tell me more. ",
                 "Tell me more! ",
                 "Why ",
                 "I see. Can you elaborate? ",
                 "Interesting. Can you tell me more? ",
                 "Why? ",
                 "How do you think I feel when you say that? "
                  )
    return random.choice(responses)


if __name__ == "__main__":
    bot = FemiChatBot()
    bot.greet()
