#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import matplotlib.pyplot as plt
import functools
from nltk import FreqDist

maxfreq = 10**6


class funcobj(object):
    def __init__(self, mylen, f, *args, **kwargs):
        self.f = functools.partial(f, *args, **kwargs)
        self.mylen = mylen
    def __getitem__(self, idx):
        return self.f(idx + 1)
    def __len__(self):
        return self.mylen


def zipf(k, rank):
    return k / rank


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

    plt.loglog(ranks, funcobj(len(ranks), zipf, maxfreq), 
               label='zipf\'s law')

    plt.grid(True)
    plt.xlabel('rank', fontsize=14, fontweight='bold')
    plt.ylabel('frequency', fontsize=14, fontweight='bold')
    plt.legend(loc='upper right')
    plt.savefig('freqdist.png')

if __name__ == '__main__':
    main()
