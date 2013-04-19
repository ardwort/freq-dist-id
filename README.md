# Perbandingan distribusi frekuensi kata bahasa Indonesia di Kompas, Wikipedia, Twitter, dan Kaskus

**Abstrak**. Dalam bahasa yang sama, kata yang paling sering digunakan, jumlah huruf per kata, serta berbagai statistik lain yang terkait dengan distribusi frekuensi sangat bergantung kepada ragam yang digunakan. Makalah ini menelaah perbandingan distribusi frekuensi kata antara empat ragam bahasa Indonesia yang populer di internet, yaitu Kompas (media massa), Wikipedia bahasa Indonesia (ensiklopedia), Twitter (mikroblog), dan Kaskus (forum). Kajian dilakukan dengan menggunakan korpus yang diambil dari data yang tersedia secara publik di internet serta diproses dengan menggunakan bahasa pemrograman Python serta beberapa pustaka pemrograman yang bersumber terbuka. Hasil kajian menunjukkan adanya perbedaan distribusi yang cukup tajam di antara keempat ragam bahasa Indonesia ini. Kompas banyak menggunakan kata *akan* karena sifat beritanya; Wikipedia banyak menggunakan kata *adalah* karena sifat deskriptifnya; Twitter banyak menggunakan kata *aku* karena sifat subjektifnya; Kaskus banyak menggunakan kata *gan* yang merupakan kata khas komunitas ini. Kajian ini juga memberikan beberapa hal yang harus diperhatikan dalam kajian serupa seperti penyiapan dan pembersihan data korpus dan leksikon. Kajian ini diharapkan dapat memberikan dasar penelitian lebih lanjut dalam bidang distribusi frekuensi dan analisis korpus bahasa Indonesia.

Frekuensi penggunaan kata dalam sebuah tulisan maupun percakapan sangat memengaruhi waktu tanggap penutur. Semakin sering suatu kata digunakan, semakin cepat kata pula tersebut dipahami[^fn-Whaley1978][^fn-Ford_etal2003]. Frekuensi penggunaan sebuah kata juga sering menjadi variabel pembeda antara ragam lisan dan ragam tulis[^fn-Tryk1969]. Di sisi lain, pemilihan kata dapat dianggap sebagai representasi pengetahuan penutur. Pengalaman penutur terhadap penggunaan sebuah kata harus dipertimbangkan pada semua modalitas yang berhubungan dengan kata tersebut[^fn-Gernsbacher_1984]. Hal yang sama berlaku untuk makna dari kata yang dimaksud. Keakraban penutur dengan kata tidak hanya diperoleh dari menghadapi dan merasakannya, namun juga dari operasi semantik yang terlibat dalam pengolahan, khususnya dalam pemahaman, yang kemudian mengharuskan penutur memahami representasi bentuk kata dan maknanya. Keakraban dengan kedua representasi bentuk kata dan maknanya dapat secara bersamaan meningkat setiap kali kata tersebut diproses. Makalah ini menyajikan peringkat 20 kata yang paling sering digunakan dalam beberapa empat ragam bahasa Indonesia, yaitu jurnalistik, ensiklopedia, mikroblog, dan forum daring. Analisis terhadap data tersebut menggambarkan keakraban penutur terhadap kata-kata tertentu berdasarkan sifat ragam bahasa yang dipilih.

[^fn-Whaley1978]: 	Whaley, C. P. (1978). Word-nonword classification time. *Journal Verbal Learning and Verbal Behavior*.

[^fn-Ford_etal2003]: 	Ford, M. A., Marslen-Wilson, W. D, & Davis, M. H. (2003). Morphology and frequency: Contrasting methodologies. *Trend in Linguistics. Morphological structure in language processing*. Mouton de Gruyter.

[^fn-Tryk1969]:	Tryk, H. E. (1969). Subjective scaling of word frequency. *American Journal of Psychology*.

[^fn-Gernsbacher_1984]:	Gernsbacher, M. A. (1984). Resolving 20 years of inconsistent interactions between lexical familiarity and orthography, concreteness and polysemy. *Journal of Experimental Psychology: General*.

## Data Olahan

Hanya 10,000 peringkat pertama kata saja dari setiap corpus yang ditampilkan di sini. 

### Corpora

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

| Korpus Data | Informasi Pengambilan Data                                                                                                            | Jumlah Kata Unik | Jumlah Kata Keseluruhan | 
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------: | ----------------------: |
| Kompas      | Diambil pada bulan Januari tahun 2013 untuk artikel berita berbahasa Indonesia daring tahun 2012.                                     |          343.532 |              32.724.503 |
| Wikipedia   | Diambil dari [salinan "idwiki"](http://dumps.wikimedia.org/idwiki/20130115/) bulan Januari tahun 2013.                                |          936.288 |              43.545.242 |
| Twitter     | Diambil pada bulan Januari tahun 2013 untuk percakapan bulan Oktober-Desember 2012 oleh pengguna Twitter yang berlokasi di Indonesia. |          798.078 |              34.769.573 |
| Kaskus      | Diambil pada bulan Januari tahun 2013 dan dari 1,000 threads terakhir sub-forum ["The Lounge"](http://www.kaskus.co.id/forum/21/).    |          761.795 |             109.292.156 |

**Tabel 2**: Peringkat dan persentase kemunculan kata

|  # | Kompas   |     % | Wikipedia |     % | Twitter |     % | Kaskus |     % |
| -- | -------- | ----: | --------- | ----: | ------- | ----: | ------ | ----: |
|  1 | yang     | 2,429 | yang      | 2,239 | di      | 1,162 | gan    | 4,808 |
|  2 | di       | 2,168 | dan       | 2,214 | yg      | 0,803 | ane    | 2,202 |
|  3 | dan      | 1,923 | di        | 2,108 | ya      | 0,778 | di     | 1,194 |
|  4 | ini      | 1,017 | pada      | 1,007 | aku     | 0,719 | yang   | 1,097 | 
|  5 | itu      | 0,958 | dari      | 0,987 | yang    | 0,690 | yg     | 1,034 | 
|  6 | dengan   | 0,953 | dengan    | 0,927 | ini     | 0,682 | ya     | 0,998 |
|  7 | untuk    | 0,907 | ini       | 0,791 | itu     | 0,670 | ada    | 0,854 |
|  8 | dari     | 0,858 | adalah    | 0,749 | ada     | 0,669 | itu    | 0,786 |
|  9 | dalam    | 0,679 | dalam     | 0,714 | d       | 0,613 | tuh    | 0,758 |
| 10 | akan     | 0,610 | untuk     | 0,689 | aja     | 0,498 | aja    | 0,739 |
| 11 | pada     | 0,609 | kategori  | 0,649 | ga      | 0,481 | bisa   | 0,701 |
| 12 | tidak    | 0,604 | tahun     | 0,633 | dan     | 0,470 | juga   | 0,680 |
| 13 | juga     | 0,463 | sebagai   | 0,476 | gak     | 0,469 | kalo   | 0,642 |
| 14 | ke       | 0,449 | oleh      | 0,457 | i       | 0,435 | keren  | 0,626 |
| 15 | tersebut | 0,410 | indonesia | 0,426 | mau     | 0,412 | ga     | 0,624 |
| 16 | ada      | 0,378 | ke        | 0,390 | ke      | 0,410 | banget | 0,599 |
| 17 | bisa     | 0,359 | the       | 0,349 | udah    | 0,410 | nya    | 0,567 |
| 18 | saat     | 0,352 | ia        | 0,322 | lagi    | 0,405 | wah    | 0,532 |
| 19 | jakarta  | 0,344 | tidak     | 0,318 | kalo    | 0,389 | nih    | 0,508 |
| 20 | tahun    | 0,337 | menjadi   | 0,303 | the     | 0,379 | jadi   | 0,502 |



### Diagram

![Gambar 1: Perbandingan distribusi frekuensi kemunculan kata](https://raw.github.com/ardwort/freq-dist-id/master/freqdist.png)

![Gambar 2: Perbandingan peringkat frekuensi kemunculan kata](https://raw.github.com/ardwort/freq-dist-id/master/top10-words.png)

![Gambar 3: Perbandingan distribusi jumlah huruf per kata](https://raw.github.com/ardwort/freq-dist-id/master/chars.png)



## Publikasi

* Lanin, I., Geovedi, J., & Soegijoko. W. (2013). Perbandingan distribusi frekuensi kata bahasa Indonesia di Kompas, Wikipedia, Twitter, dan Kaskus. *Konferensi Linguistik Tahunan Atma Jaya 11 (KOLITA11)*.

Jika anda menggunakan data dan kode pemrograman yang terdapat dalam repositori ini dalam sebuah publikasi, harap sertakan kutipan di atas.


## Kontak

Hubungi Eric, jika Anda ingin mentraktir kami.

Gen Eric. <gen.eric@ardwort.com>
