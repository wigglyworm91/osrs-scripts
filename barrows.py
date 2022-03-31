import random
import sys

THRESHOLD = 1000

sets = lambda items: (items[i:i+4] for i in range(0, len(items), 4))

def onedub(items):
    for s in sets(items):
        if all(item >= 2 for item in s):
            return True

def onedubnoother(items):
    if not onedub(items): return False
    num_sets = 0
    for s in sets(items):
        if all(s):
            num_sets += 1
    return num_sets == 1

comp_criteria = {
        'fullset': ('one full set', lambda items: any(all(items[i:i+4]) for i in range(0, len(items), 4)) ),
        'all': ('all pieces', lambda items: all(items) ),
        'one': ('one specific piece', lambda items: items[0]),
        'two': ('two specific pieces', lambda items: all(items[0:2])),
        'three': ('three specific pieces', lambda items: all(items[0:3])),
        '2full': ('two full sets', lambda items: sum(all(items[i:i+4]) for i in range(0, len(items), 4)) >= 2),
        '3full': ('three full sets', lambda items: sum(all(items[i:i+4]) for i in range(0, len(items), 4)) >= 3),
        '4full': ('four full sets', lambda items: sum(all(items[i:i+4]) for i in range(0, len(items), 4)) >= 4),
        '5full': ('five full sets', lambda items: sum(all(items[i:i+4]) for i in range(0, len(items), 4)) >= 5),
        'anyof6': ('any of six specific pieces', lambda items: any(items[:6])),
        'onedub': ('one double set', lambda items: any(all(item >= 2 for item in items[i:i+4]) for i in range(0, len(items), 4)) ),
}

# completion criteria that can become impossible at some point
failable_criteria = {
        '3/4': ('exactly three out of four on all sets', lambda items: all((sum(items[i:i+4]) == 3) for i in range(0, len(items), 4))),
        'onedubnoother': ('one double set and no other sets', onedubnoother),
}

comp_criteria.update(failable_criteria)

# these will be set later
DESCRIPTION = ''
is_complete = lambda: True
CHANCE = 1/1

def simulate(cutoff=float('inf')):
    items = [0] * 4 * 6
    num  = 0
    while not is_complete(items) and num <= cutoff:
        num += 1
        if random.random() < CHANCE:
            items[random.randint(0, len(items)-1)] += 1
    return num

def simulate2(chests):
    items = [0] * 4 * 6
    #for i in range(0, 5*4, 4):
    #    items[i:i+3] = [True]*3
    #items[20] = items[21] = True
    num  = 0
    while num < chests:
        num += 1
        if random.random() < CHANCE:
            items[random.randint(0, len(items)-1)] += 1
    return is_complete(items)


if __name__ == '__main__':
    import argparse
    from datetime import datetime
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, default=400)
    parser.add_argument('--mode', choices=comp_criteria.keys(), default='all')
    parser.add_argument('--trials', type=int, default=10000)
    parser.add_argument('--chance', type=eval, default=eval('1/14.57'))
    args = parser.parse_args()

    start_time = datetime.now()

    DESCRIPTION, is_complete = comp_criteria[args.mode]
    CHANCE = args.chance

    # this simulation does not make any sense if the completion criterion can be failed
    if args.mode not in failable_criteria:
        by_thresh = 0
        tot = 0
        N = args.trials
        for i in range(N):
            num = simulate(cutoff=args.threshold*10)
            tot += num
            if num <= args.threshold:
                by_thresh += 1

        print(f'Expected barrows chests to get {DESCRIPTION}: {tot * 1.0 / N}')

        print(f'Of those who go for {DESCRIPTION}, {by_thresh * 100.0 / N}% have it by chest {args.threshold}')

    tot2 = 0
    N = args.trials
    for i in range(N):
        result = simulate2(args.threshold)
        tot2 += result

    print(f'Of those who do {args.threshold} chests, {tot2 * 100.0 / N}% have {DESCRIPTION}')
    end_time = datetime.now()
    print(f'Script ran in {end_time - start_time}')
