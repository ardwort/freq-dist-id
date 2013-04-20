% Perbandingan distribusi frekuensi kata bahasa Indonesia di Kompas, Wikipedia, Twitter, dan Kaskus
% Ivan Lanin
  Jim Geovedi
  Wicak Soegijoko
% Ardwort

**Abstrak**. Dalam bahasa yang sama, kata yang paling sering digunakan, jumlah huruf per kata, serta berbagai statistik lain yang terkait dengan distribusi frekuensi sangat bergantung kepada ragam yang digunakan. Makalah ini menelaah perbandingan distribusi frekuensi kata antara empat ragam bahasa Indonesia yang populer di internet, yaitu Kompas (media massa), Wikipedia bahasa Indonesia (ensiklopedia), Twitter (mikroblog), dan Kaskus (forum). Kajian dilakukan dengan menggunakan korpus yang diambil dari data yang tersedia secara publik di internet serta diproses dengan menggunakan bahasa pemrograman Python serta beberapa pustaka pemrograman yang bersumber terbuka. Hasil kajian menunjukkan adanya perbedaan distribusi yang cukup tajam di antara keempat ragam bahasa Indonesia ini. Kompas banyak menggunakan kata *akan* karena sifat beritanya; Wikipedia banyak menggunakan kata *adalah* karena sifat deskriptifnya; Twitter banyak menggunakan kata *aku* karena sifat subjektifnya; Kaskus banyak menggunakan kata *gan* yang merupakan kata khas komunitas ini. Kajian ini juga memberikan beberapa hal yang harus diperhatikan dalam kajian serupa seperti penyiapan dan pembersihan data korpus dan leksikon. Kajian ini diharapkan dapat memberikan dasar penelitian lebih lanjut dalam bidang distribusi frekuensi dan analisis korpus bahasa Indonesia.

Kata kunci: distribusi frekuensi, korpus, NLP

## Pendahuluan

Frekuensi penggunaan kata dalam sebuah tulisan maupun percakapan sangat memengaruhi waktu tanggap penutur. Semakin sering suatu kata digunakan, semakin cepat kata pula tersebut dipahami [@Whaley1978; @Ford2003]. Frekuensi penggunaan sebuah kata juga sering menjadi variabel pembeda antara ragam lisan dan ragam tulis [@Tryk1968]. Di sisi lain, pemilihan kata dapat dianggap sebagai representasi pengetahuan penutur. Pengalaman penutur terhadap penggunaan sebuah kata harus dipertimbangkan pada semua modalitas yang berhubungan dengan kata tersebut [@Gernsbacher1984]. Hal yang sama berlaku untuk makna dari kata yang dimaksud. Keakraban penutur dengan kata tidak hanya diperoleh dari menghadapi dan merasakannya, namun juga dari operasi semantik yang terlibat dalam pengolahan, khususnya dalam pemahaman, yang kemudian mengharuskan penutur memahami representasi bentuk kata dan maknanya. Keakraban dengan kedua representasi bentuk kata dan maknanya dapat secara bersamaan meningkat setiap kali kata tersebut diproses. Makalah ini menyajikan peringkat 20 kata yang paling sering digunakan dalam beberapa empat ragam bahasa Indonesia, yaitu jurnalistik, ensiklopedia, mikroblog, dan forum daring. Analisis terhadap data tersebut menggambarkan keakraban penutur terhadap kata-kata tertentu berdasarkan sifat ragam bahasa yang dipilih.

## Metodologi

Korpus yang digunakan untuk keperluan penelitian ini diperoleh dari 4 situs daring berbahasa Indonesia yang populer di internet, yaitu Kompas (media massa), Wikipedia bahasa Indonesia (ensiklopedia, selanjutnya disingkat Wikipedia), Twitter (mikroblog), dan Kaskus (forum). Keempat korpus ini dipilih sebagai bahan penelitian karena mewakili ragam bahasa yang berbeda. Informasi detail data korpus dipaparkan pada Tabel 1.

+---------+-------------------------+--------+-----------+
|         |Informasi                |  Jumlah|     Jumlah|
|Korpus   |Pengambilan              |    Kata|       Kata|
|Data     |Data                     |    Unik|Keseluruhan|
+=========+=========================+========+===========+
|Kompas   |Diambil pada bulan       |343.532 | 32.724.503|
|         |Januari tahun 2013 untuk |        |           |
|         |artikel berita berbahasa |        |           |
|         |Indonesia                |        |           |
|         |daring tahun 2012.       |        |           |
+---------+-------------------------+--------+-----------+
|Wikipedia|Diambil dari             |936.288 | 43.545.242|
|         |salinan ["idwiki"][wiki] |        |           |
|         |bulan Januari tahun 2013.|        |           |
+---------+-------------------------+--------+-----------+
|Twitter  |Diambil pada bulan       |798.078 | 34.769.573|
|         |Januari tahun 2013 untuk |        |           |
|         |percakapan bulan         |        |           |
|         |Oktober-Desember 2012    |        |           |
|         |oleh pengguna Twitter    |        |           |
|         |yang berlokasi di        |        |           |
|         |Indonesia.               |        |           |
+---------+-------------------------+--------+-----------+
|Kaskus   |Diambil pada bulan       |761.795 |109.292.156|
|         |Januari tahun 2013 dan   |        |           |
|         |dari 1,000 threads       |        |           |
|         |terakhir sub-forum       |        |           |
|         |["The Lounge"][kaskus].  |        |           |
+---------+-------------------------+--------+-----------+

Table: Informasi Pengambilan Data Korpus

[wiki]: http://dumps.wikimedia.org/idwiki/20130115/
[kaskus]: http://www.kaskus.co.id/forum/21/

Data mentah diperoleh melalui teknik scraping untuk situs Kaskus dan Kompas, ekstraksi salinan data XML dari Wikipedia, dan [*API query*](https://dev.twitter.com/docs/api/1.1) pada layanan Twitter. Data mentah tersebut selanjutnya dibersihkan dari kode HTML, nama pengguna (pada korpus Twitter dan Kaskus), templat atau pola acu (pada korpus Wikipedia), alamat URL (Uniform Resource Locator) internet, serta sebagian besar tanda baca, kecuali tanda hubung (“-”) pada kata ulang. Data korpus diproses dengan menggunakan bahasa pemrograman Python serta pustaka NLTK, NumPy, dan SciPy.

Frekuensi kemunculan kata dihitung dengan menggunakan rumus dari  @Ramisch2011 yang menyatakan bahwa frekuensi (*fréquence*, $f$) merupakan hasil pembagian jumlah kemunculan suatu kata atau token (*nombre d’occurrences*, $C_w(\cdot)$) dengan jumlah total kata atau token ($n$). Sebagai contoh, berikut rumus penghitungan kemunculan kata yang dalam korpus data Wikipedia: 
$$\Large f = \frac{C_w(\cdot)}{N}  = \frac{C_{wikipedia}(yang)}{N} = \frac{975156}{43545242}  = 0.02239408842876565$$


Namun hasil perhitungan ini tidak dapat langsung digunakan sebagai model linguistik karena banyaknya kata yang jarang digunakan (*low-rank words*) memiliki frekuensi sama. Statistik suatu korpus data sangat bergantung pada besar korpus, jenis bahasa, dan ragam yang digunakan. Walaupun demikian, kaitan logaritmik antara jumlah kata (token) dan jumlah jenis kata (token) biasanya akan mengikuti Hukum Zipf [@Zipf1932; @Baayen2001]. Hukum Zipf menyatakan bahwa pada korpus data bahasa alami, peringkat ($r$) dari sebuah kata adalah berdasarkan frekuensinya ($f$) yang diformulakan menjadi
$$\Large f \propto \frac{1}{r}$$
dan formula ini  ekuivalen dengan 
$$\Large f = \frac{k}{r}$$
untuk $k$ sebagai konstanta faktor.


## Hasil dan Analisis

Jumlah keseluruhan kata dari keempat korpus adalah sebanyak 220.331.474 kata dengan distribusi jumlah kata unik dan jumlah keseluruhan kata per korpus disajikan pada tabel 1. Karena keterbatasan tempat, tabel penghitungan yang ditampilkan dalam makalah ini dibatasi hanya 20 kata teratas dari masing-masing korpus (Tabel 2). Data contoh yang lebih besar tersedia daring di repositori [Github](https://github.com/ardwort/freq-dist-id). 

No|Kompas  |%   |Wikipedia|%   |Twitter|%   |Kaskus|%   
--|--------|----+---------|----|-------|----|------|----
1 |yang    |2,42|yang     |2,23|di     |1,16|gan   |4,80
2 |di      |2,16|dan      |2,21|yg     |0,80|ane   |2,20
3 |dan     |1,92|di       |2,10|ya     |0,77|di    |1,19
4 |ini     |1,01|pada     |1,00|aku    |0,71|yang  |1,09
5 |itu     |0,95|dari     |0,98|yang   |0,69|yg    |1,03
6 |dengan  |0,95|dengan   |0,92|ini    |0,68|ya    |0,99
7 |untuk   |0,90|ini      |0,79|itu    |0,67|ada   |0,85
8 |dari    |0,85|adalah   |0,74|ada    |0,66|itu   |0,78
9 |dalam   |0,67|dalam    |0,71|d      |0,61|tuh   |0,75
10|akan    |0,61|untuk    |0,68|aja    |0,49|aja   |0,73
11|pada    |0,60|kategori |0,64|ga     |0,48|bisa  |0,70
12|tidak   |0,60|tahun    |0,63|dan    |0,47|juga  |0,68
13|juga    |0,46|sebagai  |0,47|gak    |0,46|kalo  |0,64
14|ke      |0,44|oleh     |0,45|i      |0,43|keren |0,62
15|tersebut|0,41|indonesia|0,42|mau    |0,41|ga    |0,62
16|ada     |0,37|ke       |0,39|ke     |0,41|banget|0,59
17|bisa    |0,35|the      |0,34|udah   |0,41|nya   |0,56
18|saat    |0,35|ia       |0,32|lagi   |0,40|wah   |0,53
19|jakarta |0,34|tidak    |0,31|kalo   |0,38|nih   |0,50
20|tahun   |0,33|menjadi  |0,30|the    |0,37|jadi  |0,50


Table: Peringkat dan persentase kemunculan kata


Gambar-gambar di bawah ini memberikan ilustrasi dari analisis yang akan diuraikan selanjutnya.

![Perbandingan distribusi frekuensi kemunculan kata][img-freqdist]

![Perbandingan peringkat frekuensi kemunculan kata][img-top10words]

![Perbandingan distribusi jumlah huruf per kata][img-chars]

[img-freqdist]: img-freqdist.pdf
[img-top10words]: img-top10-words.pdf
[img-chars]: img-chars.pdf

### Kata yang tersering digunakan

Beberapa penelitian terdahulu [@Kirby2001; @Roberts2005]  mengusulkan model linguistik yang dapat menjelaskan fenomena ketidakteraturan dalam bahasa. Fenomena itu dapat diketahui lewat distribusi Zipf (Gambar 1) dan korelasi frekuensi kata dengan konstruksi dan ketidakteraturan morfologi atau sintaksis dari kata yang dimaksud. Hal tersebut dapat menjelaskan bahwa kata yang sering muncul di sejumlah korpus adalah kata yang tidak teratur bentuknya. Berikut akan disoroti beberapa hal menarik seputar 20 kata yang tersering digunakan dalam tiap korpus.

Semua kata teratas di Kompas merupakan ragam baku dengan satu kata nama tempat. Kata *akan* (#10) banyak dipakai karena ragam jurnalistik yang memberitakan hal-hal di masa depan. Kata *Jakarta* (#19) muncul untuk menjelaskan tempat, sedangkan kata *tahun* (#20) muncul untuk menjelaskan waktu.

Korpus Wikipedia banyak mengandung kata *adalah* (#8) karena sifat deskriptif ensiklopedia. Kata bahasa Inggris, *the* (#17), berasal dari nama yang dicantumkan dalam artikel. Kata *kategori* (#11) berasal dari kategorisasi artikel yang muncul hampir di semua artikel.

Korpus Twitter banyak mengandung kata *aku* (#4) dan *mau* (#15) karena sifat subjektif media sosial. Pemendekan kata seperti *yg* (#2), *d* (#9), dan *ga* (#11) banyak dipakai karena pembatasan jumlah huruf pada media ini. Ragam cakapan *aja* (#10), *gak* (#13), *udah* (#17), dan *kalo* (#19) muncul sesuai dengan sifat percakapan pada Twitter. Kata *i* (#14) merupakan cerminan campur kode (*code-mixing*) atau alih kode (*code-switching*) pada Twitter.

Dua kata teratas pada korpus Kaskus adalah *gan* (#1) dan *ane* (#2) yang merupakan pronomina persona khas komunitas ini. Pemendekan seperti *yg* (#5) dan *ga* (#15), serta ragam cakapan seperti *kalo* (#13) dan *banget* (#16) juga muncul dalam korpus ini. Partikel *tuh* (#9), *wah* (#18), dan *nih* (#19), serta kata *keren* (#14) menggambarkan sifat ekspresif media ini. Pronomina *-nya* yang merupakan bentuk terikat yang ditulis serangkai dengan kata sebelumnya muncul sebagai kata terpisah *nya* (#17).

### Perbandingan peringkat frekuensi kemunculan kata

Sebagai perbandingan, kata yang tersering digunakan pada empat korpus dibandingkan dengan hasil penelitian @Tala2003 yang menggunakan korpus kepala berita Kompas pada tahun 2001. Dari perbandingan pada Gambar 2, terlihat bahwa korpus Kompas dan Wikipedia memberikan hasil yang cukup serupa dengan penelitian Tala. Namun, korpus Twitter dan Kaskus memberikan hasil yang sangat berbeda. Hal ini menunjukkan adanya perbedaan kata yang tersering digunakan dalam dua kelompok ragam bahasa yang berbeda, yaitu ragam formal (Kompas dan Wikipedia) dan ragam informal (Twitter dan Kaskus).

Dari 20 kata yang tersering digunakan menurut penelitian Tala, ada dua kata (*yang* dan *di*) yang juga masuk peringkat 20 besar dalam empat korpus dalam penelitian ini. Lima kata lain (*ada*, *dan*, *ini*, *itu*, dan *ke*) masuk dalam peringkat 20 besar dalam tiga dari empat korpus. Hal ini menunjukkan bahwa meskipun ada perbedaan antarragam bahasa, ada beberapa kata yang kerap digunakan bersama dalam semua ragam bahasa Indonesia.

### Jumlah huruf per kata

Analisis jumlah huruf per kata yang diilustrasikan dalam Gambar 3 sejalan dengan pendapat @Zipf1936 bahwa kata pendek (jumlah huruf sedikit) lebih sering digunakan daripada kata panjang (jumlah huruf banyak). Hal ini disebabkan oleh dorongan penutur untuk meminimalkan waktu dan upaya yang diperlukan dalam penuturan atau penulisan kata [@Piantadosi2011].

Sebaran frekuensi kemunculan kata menurut jumlah huruf per kata pada keempat korpus menunjukkan pola distribusi Gauss yang condong ke kiri ke arah kata pendek. Wikipedia dan Twitter sama-sama paling sering menggunakan kata dengan empat huruf, sedangkan Kompas paling sering menggunakan kata dengan lima huruf. Kaskus paling sering menggunakan kata dengan tiga huruf dengan kurva distribusi Gauss yang cukup curam. Hal ini menunjukkan kecenderungan yang cukup tinggi dari komunitas Kaskus untuk meminimalkan waktu dan upaya dalam penulisan kata.


## Kesimpulan

Kata yang tersering dipakai di Kompas, Wikipedia, Twitter, dan Kaskus berbeda. Perbedaan ini timbul karena perbedaan ragam bahasa dan sifat khas masing-masing. Walaupun demikian, frekuensi kemunculan kata di keempat korpus ini secara umum tetap mengikuti hukum Zipf. Di samping itu, hasil analisis sebaran jumlah huruf per kata pada keempat korpus ini juga sesuai dengan hukum Zipf yang menyatakan kecenderungan penutur untuk menggunakan kata dengan jumlah huruf sedikit demi meminimalkan upaya untuk berkomunikasi.

Metode pemrosesan data korpus yang telah dikembangkan di sini akan digunakan untuk melakukan penelitian-penelitian lain yang lebih aplikatif dan langsung dapat dimanfaatkan, seperti kamus kata bahasa Indonesia sederhana berdasarkan kata yang paling sering muncul dalam berbagai korpus, kamus variasi ejaan (atau salah eja) kata, serta penerjemahan otomatis antarragam bahasa Indonesia (misalnya dari SMS ke ragam formal). Penyempurnaan yang perlu dilakukan dalam metode ini antara lain adalah identifikasi nama diri (*named-entity*) dan *stopwords*.

## Referensi

