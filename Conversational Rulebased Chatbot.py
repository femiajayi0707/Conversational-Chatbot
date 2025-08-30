# importing regex and random libraries
import re
import random

class FemiChatBot:

  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

  #questions for the user
  random_questions = (
        "Why are you here? ",
        "What do you like to do? ",
        "How's your day going so far? ",
        "What's your favorite food? ",
        "Do you have a favorite movie or series? ",
        "What hobbies do you enjoy the most? ",
        "If you could learn any skill instantly, what would it be? ",
        "What's something new you tried recently? ",
        "If you were a superhero, what would your power be? ",
        "Would you rather fight 100 tiny robots or 1 giant chicken? ",
        "Do you think robots like me should be allowed to tell jokes? "
    )

  def __init__(self):
    #dictionary mapping user intents to regex patterns
    self.babble = {
      'describe_femi_intent': re.compile(r'\blearn\s+about\s+(femi|him)|who\s+femi|about\s+femi\b',re.IGNORECASE),
      'fav_things_to_do': re.compile(r"\b(fav(?:ou)?rite|hobbies|likes?\s+(to\s+do)?)\b", re.IGNORECASE),
      'where_is_femi_from': re.compile(r"(where\s+is\s+femi\s+from|femi\w+\s+home\w+)", re.IGNORECASE),
      'femi_skills': re.compile(r"(what\s+can\s+femi\s+do|femi\w+\s+skills|femi\s+knows)", re.IGNORECASE),
      'why_femi_built_me': re.compile(r"(why\s+did\s+femi\s+build\s+you|femi\s+made\s+you)", re.IGNORECASE),
      'tell_joke': re.compile(r"(tell\s+me\s+a\s+joke|joke|make\s+me\s+laugh)", re.IGNORECASE)
      }

  # asks for user's name and checks if they want to chat
  def greet(self):
    name = input("What is your name ")
    will_help = input("Hi {}, I'm Femi's Chatbot. I'm here to entertain you and answer any questions you may have on Femi. Say when, when ready to begin ".format(name))
    if will_help in self.negative_responses:
      print("Okay, goodbye")
      return 
    return self.chat()
  
  #checks if user wants to exit the convo
  def make_exit(self, reply):
    words = reply.split()
    for word in words:
      if word in self.exit_commands:
        print("Ok, have a nice day!") 
        return True
    return False

  #starts chat with a random question
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      response = self.match_reply(reply) 
      print(response)  
      reply = input("Anything else? ").lower()  

  # matches user reply to intents using regex
  def match_reply(self, reply):
    for intent,regex_pattern in self.babble.items():
      found = re.search(regex_pattern,reply)
      if found and intent == 'describe_femi_intent': 
        return self.describe_femi_intent()
      elif found and intent == 'fav_things_to_do':
        return self.fav_things_to_do()
      elif found and intent == 'where_is_femi_from':
        return self.fav_things_to_do()
      elif found and intent == 'femi_skills':
        return self.fav_things_to_do()
      elif found and intent == 'why_femi_built_me':
        return self.fav_things_to_do()
      elif found and intent == 'tell_joke':
        return self.fav_things_to_do()
    return self.no_match_intent()

  #responses for who is femi
  def describe_femi_intent(self):
    responses = (
        "Femi is a hardworking guy. I'd know he built me! "
        "He wants to make the world a better place by building systems that help people.",
        "Femi built me for fun, to practice coding and to entertain people like you!",
        "He wanted to learn more about chatbots and thought I'd be a good project.",
    )
    return random.choice(responses)

  #response about femi's fav things to do
  def fav_things_to_do(self):
    responses = (
        "He likes to watch movies, series, and play games."
        "He finds happiness in learning about new developing technology.",
    )  
    return random.choice(responses)

  #response about femi's origin
  def where_is_femi_from(self):
    responses = (
        "Femi is from Nigeria. ",
        "He grew up in Nigeria and is proud of his roots!",
    )
    return random.choice(responses)

  #responses for femi's skills
  def femi_skills(self):
    responses = (
        "Femi loves coding and building cool systems with Python and other tech.",
        "He's skilled in problem-solving, coding, and learning new technologies.",
    )
    return random.choice(responses)

  #joke responses
  def tell_joke(self):
    responses = (
      "What did the horse say after it tripped? Help! I've fallen and I can't giddy-up!",
      "Why can't you hear a pterodactyl going to the bathroom? Because the 'P' is silent.",
      "What do you call a well-balanced horse? Stable.",
      "What do you call an angry carrot? A steamed veggie.",
      "Where do polar bears keep their money? In a snowbank.",
      "How do you make an egg roll? You push it!",
      "What would bears be without bees? Ears.",
      "Why did the bicycle fall over? Because it was two tired."
      )
    return random.choice(responses)

  #backup response when no regex inetent matches
  def no_match_intent(self):
    responses = (
      "Please tell me more. ",
      "Tell me more! ",
      "Why ",
      "I see. Can you elaborate? ",
      "Interesting. Can you tell me more? ",
      "Why? ",
      "My code doesn't give me an answer so ask another question. "
                )
    return random.choice(responses)


if __name__ == "__main__":
    bot = FemiChatBot()
    bot.greet()
