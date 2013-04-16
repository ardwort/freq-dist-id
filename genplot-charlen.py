#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import matplotlib.pyplot as plt
import numpy as np
from nltk import FreqDist


def main():
    corpora = ['idwiki', 'kaskus', 'kompas', 'twitter']
    corpora_dict = {}

    for corpus in corpora:
        fd = FreqDist()
        for line in codecs.open(corpus + '.1gram-top10k', 'r', 'utf-8'):
            (word, freq) = line.split('\t')
            fd[len(word)] += int(freq.strip())

        sorted_fd = sorted(fd.iteritems(), key=operator.itemgetter(0))
        lengths = [0] + [x for x, y in sorted_fd]
        freqs = [0] + [y for x, y in sorted_fd]
        plt.plot(lengths, freqs, label=corpus)

    plt.grid(True)
    plt.xlabel('length', fontsize=14, fontweight='bold')
    plt.ylabel('frequency', fontsize=14, fontweight='bold')
    plt.legend(loc='upper right')
    plt.savefig('char.png')
    plt.close()


if __name__ == '__main__':
    main()
