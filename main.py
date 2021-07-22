import random
from plyer import notification


Offline_quotes =[  
                    "All our dreams can come true, if we have the courage to pursue them.",
                    "The secret of getting ahead is getting started.",
                    "I’ve missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life and that is why I succeed.",
                    "Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve.",
                    "he best time to plant a tree was 20 years ago. The second best time is now.",
                    "Only the paranoid survive.",
                    "It’s hard to beat a person who never gives up.",
                    "I wake up every morning and think to myself, ‘how far can I push this company in the next 24 hours.",
                    "If people are doubting how far you can go, go so far that you can’t hear them anymore.",
                    "We need to accept that we won’t always make the right decisions, that we’ll screw up royally sometimes – understanding that failure is not the opposite of success, it’s part of success.",
                    "If people are doubting how far you can go, go so far that you can’t hear them anymore"
                ]

Persons = [
            "Walt Disney",
            "Mark Twain",
            "Michael Jordan",
            "Mary Kay Ash",
            "Chinese Proverb",
            "Andy Grove",
            "Babe Ruth",
            "Leah Busque",
            "Arianna Huffington",
            "Michele Ruiz"
          ]

Rando = random.randint(0,9)

notification.notify(
        title = Persons[Rando],
        message = Offline_quotes[Rando],
        timeout = 100,
        app_icon = "home/Codes/Python/Projects/Random_Quotes/smile.png"
        )

