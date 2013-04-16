import matplotlib.pyplot as plt
import numpy as np

# hard data.
corpora = {
    'idwiki': [
        2.23940884288,
        2.21496300331,
        0.27787421643,
        0.31834247241,
        0.927272375705,
        0.987788746242,
        0.689489795464,
        0.714245657425,
        0.791301148355,
        0.173412746219
    ],
    'kaskus': [
        1.09707873271,
        0.43766544417,
        0.786955836062,
        0.089278136301,
        0.144290318511,
        0.332207738678,
        0.147138647352,
        0.0764345796234,
        0.445880123364,
        0.0672811322342
    ],
    'kompas': [
        2.4295250565,
        1.923757253,
        0.95821164954,
        0.604088624356,
        0.953707379452,
        0.858579884315,
        0.907781548279,
        0.679881983234,
        1.01714302582,
        0.610906145771
    ],
    'twitter': [
        0.690592317599,
        0.470903108301,
        0.670083006196,
        0.102650095818,
        0.123124894286,
        0.251193766458,
        0.125713364383,
        0.0661756760717,
        0.682570936376,
        0.0888708066677
    ]
}

words = [
    'yang',
    'dan',
    'itu',
    'tidak',
    'dengan',
    'dari',
    'untuk',
    'dalam',
    'ini',
    'akan'
]

color_list = ['c', 'm', 'y', 'g']
width_bar = 1
width_space = 0.5
n_measure = len(corpora)
n_words = len(words)

total_space = n_words * (n_measure * width_bar) + (n_words - 1) * width_space
ind_space = n_measure * width_bar
step = ind_space / 2.
pos = np.arange(step, total_space + width_space, ind_space + width_space)

fig = plt.figure()
ax = fig.add_subplot(111)

for i, corpus in enumerate(corpora.keys()):
    ax.bar(pos - step + i * width_bar, corpora[corpus], width_bar,
           facecolor=color_list[i], label=corpus)

ax.set_xticks(pos)
ax.set_xticklabels(words, fontsize=10, multialignment='center')
ax.set_yticklabels([0., 0.5, 1.0, 1.5, 2.0, 2.5], fontsize=10)
ax.set_ylabel('occurrences (%)', fontsize=14, fontweight='bold')

plt.legend(loc='upper right')
plt.savefig('top10-words.png')


