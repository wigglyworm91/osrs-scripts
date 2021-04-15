import random
import sys

THRESHOLD = 1000

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
}

# completion criteria that can become impossible at some point
failable_criteria = {
        '3/4': ('exactly three out of four on all sets', lambda items: all((sum(items[i:i+4]) == 3) for i in range(0, len(items), 4))),
}

comp_criteria.update(failable_criteria)

# these will be set later
DESCRIPTION = ''
is_complete = lambda: True

def simulate(cutoff=float('inf')):
    items = [False] * 4 * 6
    num  = 0
    while not is_complete(items) and num <= cutoff:
        num += 1
        if random.random() < 1/14.57:
            items[random.randint(0, len(items)-1)] = True
    return num

def simulate2(chests):
    items = [False] * 4 * 6
    #for i in range(0, 5*4, 4):
    #    items[i:i+3] = [True]*3
    #items[20] = items[21] = True
    num  = 0
    while num < chests:
        num += 1
        if random.random() < 1/14.57:
            items[random.randint(0, len(items)-1)] = True
    return is_complete(items)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, default=400)
    parser.add_argument('--mode', choices=comp_criteria.keys(), default='all')
    parser.add_argument('--trials', type=int, default=10000)
    args = parser.parse_args()

    DESCRIPTION, is_complete = comp_criteria[args.mode]

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
