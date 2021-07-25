import random
import sys

class Player:
    def __init__(self, style):
        self.hp = 99
        self.style = style

    def hit(self, p2):
        maxhit = 25
        accuracy = {
            "flick flick": 50.9,
            "flick lash": 50.45,
            "flick deflect": 49.55,
            "lash flick": 49.54,
            "lash lash": 49.54,
            "lash deflect": 48.64,
            "deflect flick": 49.54,
            "deflect lash": 49.08,
            "deflect deflect": 48.2,
        }["%s %s" % (self.style, p2.style)]
        
        if random.uniform(0, 100) < accuracy:
            p2.hp -= random.randint(0, maxhit)

    def alive(self):
        return self.hp > 0

if __name__ == '__main__':
    import sys
    wins = losses = ties = 0
    num_trials = 100000
    for i in xrange(num_trials):
        p1 = Player(sys.argv[1])
        p2 = Player(sys.argv[2])

        while True:
            #p1.style = "lash"
            #p2.style = "deflect"
            p1.hit(p2)
            if not p2.alive(): break

            #p1.style = "deflect"
            #p2.style = "flick"
            p2.hit(p1)
            if not p1.alive(): break

        if p1.alive():
            wins += 1
        elif p2.alive():
            losses += 1
        else:
            ties += 1

    print "Win:  %0.5f" % (wins*1.0 / num_trials)
    print "Loss: %0.5f" % (losses*1.0 / num_trials)
    print "Tie:  %0.5f" % (ties*1.0 / num_trials)
