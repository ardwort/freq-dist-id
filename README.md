# Perbandingan distribusi frekuensi kata bahasa Indonesia di Kompas, Wikipedia, Twitter, dan Kaskus

**Abstrak**. Dalam bahasa yang sama, kata yang paling sering digunakan, jumlah huruf per kata, serta berbagai statistik lain yang terkait dengan distribusi frekuensi sangat bergantung kepada ragam yang digunakan. Makalah ini menelaah perbandingan distribusi frekuensi kata antara empat ragam bahasa Indonesia yang populer di internet, yaitu Kompas (media massa), Wikipedia bahasa Indonesia (ensiklopedia), Twitter (mikroblog), dan Kaskus (forum). Kajian dilakukan dengan menggunakan korpus yang diambil dari data yang tersedia secara publik di internet serta diproses dengan menggunakan bahasa pemrograman Python serta beberapa pustaka pemrograman yang bersumber terbuka. Hasil kajian menunjukkan adanya perbedaan distribusi yang cukup tajam di antara keempat ragam bahasa Indonesia ini. Kompas banyak menggunakan kata *akan* karena sifat beritanya; Wikipedia banyak menggunakan kata *adalah* karena sifat deskriptifnya; Twitter banyak menggunakan kata *aku* karena sifat subjektifnya; Kaskus banyak menggunakan kata *gan* yang merupakan kata khas komunitas ini. Kajian ini juga memberikan beberapa hal yang harus diperhatikan dalam kajian serupa seperti penyiapan dan pembersihan data korpus dan leksikon. Kajian ini diharapkan dapat memberikan dasar penelitian lebih lanjut dalam bidang distribusi frekuensi dan analisis korpus bahasa Indonesia.

Frekuensi penggunaan kata dalam sebuah tulisan maupun percakapan sangat memengaruhi waktu tanggap penutur. Semakin sering suatu kata digunakan, semakin cepat kata pula tersebut dipahami[^1][^2]. Frekuensi penggunaan sebuah kata juga sering menjadi variabel pembeda antara ragam lisan dan ragam tulis[^3]. Di sisi lain, pemilihan kata dapat dianggap sebagai representasi pengetahuan penutur. Pengalaman penutur terhadap penggunaan sebuah kata harus dipertimbangkan pada semua modalitas yang berhubungan dengan kata tersebut[^4]. Hal yang sama berlaku untuk makna dari kata yang dimaksud. Keakraban penutur dengan kata tidak hanya diperoleh dari menghadapi dan merasakannya, namun juga dari operasi semantik yang terlibat dalam pengolahan, khususnya dalam pemahaman, yang kemudian mengharuskan penutur memahami representasi bentuk kata dan maknanya. Keakraban dengan kedua representasi bentuk kata dan maknanya dapat secara bersamaan meningkat setiap kali kata tersebut diproses. Makalah ini menyajikan peringkat 20 kata yang paling sering digunakan dalam beberapa empat ragam bahasa Indonesia, yaitu jurnalistik, ensiklopedia, mikroblog, dan forum daring. Analisis terhadap data tersebut menggambarkan keakraban penutur terhadap kata-kata tertentu berdasarkan sifat ragam bahasa yang dipilih.

[^1]: 	Whaley, C. P. (1978). Word-nonword classification time. *Journal Verbal Learning and Verbal Behavior*.

[^2]: 	Ford, M. A., Marslen-Wilson, W. D, & Davis, M. H. (2003). Morphology and frequency: Contrasting methodologies. *Trend in Linguistics. Morphological structure in language processing*. Mouton de Gruyter.

[^3]:	Tryk, H. E. (1969). Subjective scaling of word frequency. *American Journal of Psychology*.

[^4]:	Gernsbacher, M. A. (1984). Resolving 20 years of inconsistent interactions between lexical familiarity and orthography, concreteness and polysemy. *Journal of Experimental Psychology: General*.

## Data Olahan


### Corpora

Hanya 10,000 peringkat pertama kata saja dari setiap corpus yang ditampilkan di sini. 

* **idwiki** - 10,000 kata populer dari salinan situs Wikipedia bahasa Indonesia tanggal 15 Januari 2013.
    * idwiki.1gram - unigram (1-gram)
    * idwiki.csv - perhitungan kemunculan dan persentase kemunculan kata
* **kaskus** - 10,000 kata populer dari 1,000 *threads* terakhir sub-forum "The Lounge" pada situs forum Kaskus, yang diambil pada bulan Januari 2013.
    * kaskus.1gram - unigram (1-gram)
    * kaskus.csv - perhitungan kemunculan dan persentase kemunculan kata
* **kompas** - 10,000 kata populer dari arsip berita tahun 2012 situs berita Kompas.
    * kompas.1gram - unigram (1-gram)
    * kompas.csv - perhitungan kemunculan dan persentase kemunculan kata
* **twitter** - 10,000 kata populer dari situs mikroblog Twitter untuk percakapan bulan Oktober-Desember 2012 oleh pengguna Twitter yang berlokasi di Indonesia.
    * twitter.1gram - unigram (1-gram)
    * twitter.csv - perhitungan kemunculan dan persentase kemunculan kata

### Tabel


**Tabel 1**: Informasi Pengambilan Data Korpus

<table>
<colgroup>
<col style="text-align:left;"/>
<col style="text-align:left;"/>
<col style="text-align:right;"/>
<col style="text-align:right;"/>
</colgroup>

<thead>
<tr>
    <th style="text-align:left;">Korpus Data</th>
    <th style="text-align:left;">Informasi Pengambilan Data</th>
    <th style="text-align:right;">Jumlah Kata Unik</th>
    <th style="text-align:right;">Jumlah Kata Keseluruhan</th>
</tr>
</thead>

<tbody>
<tr>
    <td style="text-align:left;">Kompas</td>
    <td style="text-align:left;">Diambil pada bulan Januari tahun 2013 untuk artikel berita berbahasa Indonesia daring tahun 2012.</td>
    <td style="text-align:right;">343.532</td>
    <td style="text-align:right;">32.724.503</td>
</tr>
<tr>
    <td style="text-align:left;">Wikipedia</td>
    <td style="text-align:left;">Diambil dari <a href="http://dumps.wikimedia.org/idwiki/20130115/">salinan &quot;idwiki&quot;</a> bulan Januari tahun 2013.</td>
    <td style="text-align:right;">936.288</td>
    <td style="text-align:right;">43.545.242</td>
</tr>
<tr>
    <td style="text-align:left;">Twitter</td>
    <td style="text-align:left;">Diambil pada bulan Januari tahun 2013 untuk percakapan bulan Oktober-Desember 2012 oleh pengguna Twitter yang berlokasi di Indonesia.</td>
    <td style="text-align:right;">798.078</td>
    <td style="text-align:right;">34.769.573</td>
</tr>
<tr>
    <td style="text-align:left;">Kaskus</td>
    <td style="text-align:left;">Diambil pada bulan Januari tahun 2013 dan dari 1,000 threads terakhir sub-forum <a href="http://www.kaskus.co.id/forum/21/">&quot;The Lounge&quot;</a>.</td>
    <td style="text-align:right;">761.795</td>
    <td style="text-align:right;">109.292.156</td>
</tr>
</tbody>
</table>


**Tabel 2**: Peringkat dan persentase kemunculan kata

<table width="100%">
<colgroup>
<col style="text-align:left;"/>
<col style="text-align:left;"/>
<col style="text-align:right;"/>
<col style="text-align:left;"/>
<col style="text-align:right;"/>
<col style="text-align:left;"/>
<col style="text-align:right;"/>
<col style="text-align:left;"/>
<col style="text-align:right;"/>
</colgroup>

<thead>
<tr>
    <th style="text-align:left;">#</th>
    <th style="text-align:left;">Kompas</th>
    <th style="text-align:right;">%</th>
    <th style="text-align:left;">Wikipedia</th>
    <th style="text-align:right;">%</th>
    <th style="text-align:left;">Twitter</th>
    <th style="text-align:right;">%</th>
    <th style="text-align:left;">Kaskus</th>
    <th style="text-align:right;">%</th>
</tr>
</thead>

<tbody>
<tr>
    <td style="text-align:left;">1</td>
    <td style="text-align:left;">yang</td>
    <td style="text-align:right;">2,429</td>
    <td style="text-align:left;">yang</td>
    <td style="text-align:right;">2,239</td>
    <td style="text-align:left;">di</td>
    <td style="text-align:right;">1,162</td>
    <td style="text-align:left;">gan</td>
    <td style="text-align:right;">4,808</td>
</tr>
<tr>
    <td style="text-align:left;">2</td>
    <td style="text-align:left;">di</td>
    <td style="text-align:right;">2,168</td>
    <td style="text-align:left;">dan</td>
    <td style="text-align:right;">2,214</td>
    <td style="text-align:left;">yg</td>
    <td style="text-align:right;">0,803</td>
    <td style="text-align:left;">ane</td>
    <td style="text-align:right;">2,202</td>
</tr>
<tr>
    <td style="text-align:left;">3</td>
    <td style="text-align:left;">dan</td>
    <td style="text-align:right;">1,923</td>
    <td style="text-align:left;">di</td>
    <td style="text-align:right;">2,108</td>
    <td style="text-align:left;">ya</td>
    <td style="text-align:right;">0,778</td>
    <td style="text-align:left;">di</td>
    <td style="text-align:right;">1,194</td>
</tr>
<tr>
    <td style="text-align:left;">4</td>
    <td style="text-align:left;">ini</td>
    <td style="text-align:right;">1,017</td>
    <td style="text-align:left;">pada</td>
    <td style="text-align:right;">1,007</td>
    <td style="text-align:left;">aku</td>
    <td style="text-align:right;">0,719</td>
    <td style="text-align:left;">yang</td>
    <td style="text-align:right;">1,097</td>
</tr>
<tr>
    <td style="text-align:left;">5</td>
    <td style="text-align:left;">itu</td>
    <td style="text-align:right;">0,958</td>
    <td style="text-align:left;">dari</td>
    <td style="text-align:right;">0,987</td>
    <td style="text-align:left;">yang</td>
    <td style="text-align:right;">0,690</td>
    <td style="text-align:left;">yg</td>
    <td style="text-align:right;">1,034</td>
</tr>
<tr>
    <td style="text-align:left;">6</td>
    <td style="text-align:left;">dengan</td>
    <td style="text-align:right;">0,953</td>
    <td style="text-align:left;">dengan</td>
    <td style="text-align:right;">0,927</td>
    <td style="text-align:left;">ini</td>
    <td style="text-align:right;">0,682</td>
    <td style="text-align:left;">ya</td>
    <td style="text-align:right;">0,998</td>
</tr>
<tr>
    <td style="text-align:left;">7</td>
    <td style="text-align:left;">untuk</td>
    <td style="text-align:right;">0,907</td>
    <td style="text-align:left;">ini</td>
    <td style="text-align:right;">0,791</td>
    <td style="text-align:left;">itu</td>
    <td style="text-align:right;">0,670</td>
    <td style="text-align:left;">ada</td>
    <td style="text-align:right;">0,854</td>
</tr>
<tr>
    <td style="text-align:left;">8</td>
    <td style="text-align:left;">dari</td>
    <td style="text-align:right;">0,858</td>
    <td style="text-align:left;">adalah</td>
    <td style="text-align:right;">0,749</td>
    <td style="text-align:left;">ada</td>
    <td style="text-align:right;">0,669</td>
    <td style="text-align:left;">itu</td>
    <td style="text-align:right;">0,786</td>
</tr>
<tr>
    <td style="text-align:left;">9</td>
    <td style="text-align:left;">dalam</td>
    <td style="text-align:right;">0,679</td>
    <td style="text-align:left;">dalam</td>
    <td style="text-align:right;">0,714</td>
    <td style="text-align:left;">d</td>
    <td style="text-align:right;">0,613</td>
    <td style="text-align:left;">tuh</td>
    <td style="text-align:right;">0,758</td>
</tr>
<tr>
    <td style="text-align:left;">10</td>
    <td style="text-align:left;">akan</td>
    <td style="text-align:right;">0,610</td>
    <td style="text-align:left;">untuk</td>
    <td style="text-align:right;">0,689</td>
    <td style="text-align:left;">aja</td>
    <td style="text-align:right;">0,498</td>
    <td style="text-align:left;">aja</td>
    <td style="text-align:right;">0,739</td>
</tr>
<tr>
    <td style="text-align:left;">11</td>
    <td style="text-align:left;">pada</td>
    <td style="text-align:right;">0,609</td>
    <td style="text-align:left;">kategori</td>
    <td style="text-align:right;">0,649</td>
    <td style="text-align:left;">ga</td>
    <td style="text-align:right;">0,481</td>
    <td style="text-align:left;">bisa</td>
    <td style="text-align:right;">0,701</td>
</tr>
<tr>
    <td style="text-align:left;">12</td>
    <td style="text-align:left;">tidak</td>
    <td style="text-align:right;">0,604</td>
    <td style="text-align:left;">tahun</td>
    <td style="text-align:right;">0,633</td>
    <td style="text-align:left;">dan</td>
    <td style="text-align:right;">0,470</td>
    <td style="text-align:left;">juga</td>
    <td style="text-align:right;">0,680</td>
</tr>
<tr>
    <td style="text-align:left;">13</td>
    <td style="text-align:left;">juga</td>
    <td style="text-align:right;">0,463</td>
    <td style="text-align:left;">sebagai</td>
    <td style="text-align:right;">0,476</td>
    <td style="text-align:left;">gak</td>
    <td style="text-align:right;">0,469</td>
    <td style="text-align:left;">kalo</td>
    <td style="text-align:right;">0,642</td>
</tr>
<tr>
    <td style="text-align:left;">14</td>
    <td style="text-align:left;">ke</td>
    <td style="text-align:right;">0,449</td>
    <td style="text-align:left;">oleh</td>
    <td style="text-align:right;">0,457</td>
    <td style="text-align:left;">i</td>
    <td style="text-align:right;">0,435</td>
    <td style="text-align:left;">keren</td>
    <td style="text-align:right;">0,626</td>
</tr>
<tr>
    <td style="text-align:left;">15</td>
    <td style="text-align:left;">tersebut</td>
    <td style="text-align:right;">0,410</td>
    <td style="text-align:left;">indonesia</td>
    <td style="text-align:right;">0,426</td>
    <td style="text-align:left;">mau</td>
    <td style="text-align:right;">0,412</td>
    <td style="text-align:left;">ga</td>
    <td style="text-align:right;">0,624</td>
</tr>
<tr>
    <td style="text-align:left;">16</td>
    <td style="text-align:left;">ada</td>
    <td style="text-align:right;">0,378</td>
    <td style="text-align:left;">ke</td>
    <td style="text-align:right;">0,390</td>
    <td style="text-align:left;">ke</td>
    <td style="text-align:right;">0,410</td>
    <td style="text-align:left;">banget</td>
    <td style="text-align:right;">0,599</td>
</tr>
<tr>
    <td style="text-align:left;">17</td>
    <td style="text-align:left;">bisa</td>
    <td style="text-align:right;">0,359</td>
    <td style="text-align:left;">the</td>
    <td style="text-align:right;">0,349</td>
    <td style="text-align:left;">udah</td>
    <td style="text-align:right;">0,410</td>
    <td style="text-align:left;">nya</td>
    <td style="text-align:right;">0,567</td>
</tr>
<tr>
    <td style="text-align:left;">18</td>
    <td style="text-align:left;">saat</td>
    <td style="text-align:right;">0,352</td>
    <td style="text-align:left;">ia</td>
    <td style="text-align:right;">0,322</td>
    <td style="text-align:left;">lagi</td>
    <td style="text-align:right;">0,405</td>
    <td style="text-align:left;">wah</td>
    <td style="text-align:right;">0,532</td>
</tr>
<tr>
    <td style="text-align:left;">19</td>
    <td style="text-align:left;">jakarta</td>
    <td style="text-align:right;">0,344</td>
    <td style="text-align:left;">tidak</td>
    <td style="text-align:right;">0,318</td>
    <td style="text-align:left;">kalo</td>
    <td style="text-align:right;">0,389</td>
    <td style="text-align:left;">nih</td>
    <td style="text-align:right;">0,508</td>
</tr>
<tr>
    <td style="text-align:left;">20</td>
    <td style="text-align:left;">tahun</td>
    <td style="text-align:right;">0,337</td>
    <td style="text-align:left;">menjadi</td>
    <td style="text-align:right;">0,303</td>
    <td style="text-align:left;">the</td>
    <td style="text-align:right;">0,379</td>
    <td style="text-align:left;">jadi</td>
    <td style="text-align:right;">0,502</td>
</tr>
</tbody>
</table>


### Diagram

**Gambar 1**: Perbandingan distribusi frekuensi kemunculan kata

![Gambar 1: Perbandingan distribusi frekuensi kemunculan kata](https://raw.github.com/ardwort/freq-dist-id/master/makalah/freqdist.png)

**Gambar 2**: Perbandingan peringkat frekuensi kemunculan kata

![Gambar 2: Perbandingan peringkat frekuensi kemunculan kata](https://raw.github.com/ardwort/freq-dist-id/master/makalah/top10-words.png)

**Gambar 3**: Perbandingan distribusi jumlah huruf per kata

![Gambar 3: Perbandingan distribusi jumlah huruf per kata](https://raw.github.com/ardwort/freq-dist-id/master/makalah/chars.png)


## Publikasi

> Lanin, I., Geovedi, J., & Soegijoko. W. (2013). [Perbandingan distribusi frekuensi kata bahasa Indonesia di Kompas, Wikipedia, Twitter, dan Kaskus](https://github.com/ardwort/freq-dist-id/raw/master/makalah/freqdist.pdf). In Proceedings of Konferensi Linguistik Tahunan Atma Jaya Kesebelas (KOLITA11) (pp. 249-252).

```
@inproceedings{lanin-proc-kolita11-2013,
    author      = {Ivan Lanin and Jim Geovedi and Wicak Soegijoko},
    title       = {Perbandingan distribusi frekuensi kata bahasa Indonesia di Kompas, Wikipedia, Twitter, dan Kaskus},
    year        = {2013},
    booktitle   = {Proceedings of Konferensi Linguistik Tahunan Atma Jaya Kesebelas (KOLITA11)},
    pages       = {249--252}
}
```

Jika anda menggunakan data dan kode pemrograman yang terdapat dalam repositori ini dalam sebuah publikasi, harap sertakan kutipan makalah di atas.


## Kontak

Hubungi Erik, jika Anda ingin mentraktir kami.

Gen Erik. <gen.erik@ardwort.com>
