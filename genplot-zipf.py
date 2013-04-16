#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import matplotlib.pyplot as plt
import numpy as np
from nltk import FreqDist


def main():
    corpora = ['idwiki', 'kaskus', 'kompas', 'twitter']
    for corpus in corpora:
        fd = FreqDist()
        for line in codecs.open(corpus + '.1gram', 'r', 'utf-8'):
            (word, freq) = line.split('\t')
            fd[word] = int(freq.strip())

        ranks = []
        freqs = []
        for rank, word in enumerate(fd):
            ranks.append(rank + 1)
            freqs.append(fd[word])

        plt.loglog(ranks, freqs, label=corpus)

        plt.loglog(ranks, 
                   list(reversed(sorted(np.random.zipf(2., len(ranks))))), 
                   label=corpus + '/zipf')

    plt.grid(True)
    plt.xlabel('rank', fontsize=14, fontweight='bold')
    plt.ylabel('frequency', fontsize=14, fontweight='bold')
    plt.legend(loc='upper right')
    plt.savefig('freqdist-zipf.png')
    plt.close()


if __name__ == '__main__':
    main()
