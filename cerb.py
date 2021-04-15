# ghost skip consistency calculator
import random
import sys

if 'bludgeon' in sys.argv:
    max_hit = 53
    accuracy = 0.8168
    speed = 4 # ticks
elif 'blowpipe' in sys.argv:
    max_hit = 31
    accuracy = 0.8316
    speed = 2
elif 'hasta' in sys.argv:
    max_hit = 53
    accuracy = 0.8041
    speed = 4
else:
    print 'Usage: %s (hasta|bludgeon|blowpipe)' % sys.argv[0]
    sys.exit()


N = 100000
success = 0

for i in range(N):
    # let's assume you try to avoid early ghosts
    hp = 420

    # cerb is on a 6t attack cycle and we have 15-16 of those to work with
    num_attacks = int(6 * 16 / speed)
    for atk in range(num_attacks):
        if random.random() < accuracy:
            hit = random.randint(0, max_hit)
            #hit = max_hit/2
            #print 'hit %d' % hit
            hp -= hit
            if hp <= 0: break

    if hp <= 0:
        success += 1

print 'succeeded %d times out of %d = %.2f%%' % (success, N, success*100.0/N)
