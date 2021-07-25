import random
from collections import defaultdict

def roll():
    raw = random.randint(1, 13)
    if raw in (10,11,12,13):
        return 10
    else:
        return raw

class Player:
    def __init__(self, thresh):
        self.threshold = thresh
    
    def play(self):
        score = 0
        while True:
            the_roll = roll()
            if the_roll == 1:
                # fucking ace
                if self.threshold <= score + 11 <= 21:
                    return score + 11
                else:
                    score += 1
            else:
                score += the_roll
            if score > 21:
                return 0
            if score >= self.threshold:
                return score

def play_game(player_thresh):
    player = Player(player_thresh)
    player_score = player.play()

    curtis = Player(player_score)
    curtis_score = curtis.play()
    if curtis_score > player_score:
        return 'Curtis'
    elif curtis_score == player_score:
        return play_game(player_thresh)
        #return 'Tie'
    else:
        return 'Player'

if __name__ == '__main__':
    import sys

    player_thresh = int(sys.argv[1])
    trials = int(sys.argv[2])
    
    c = defaultdict(int)
    for i in range(trials):
        c[play_game(player_thresh)] += 1
    print('Curtis', c['Curtis'])
    print('Player', c['Player'])
