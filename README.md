# Perbandingan distribusi frekuensi kata bahasa Indonesia di Kompas, Wikipedia, Twitter, dan Kaskus

**Abstrak**. Dalam bahasa yang sama, kata yang paling sering digunakan, jumlah huruf per kata, serta berbagai statistik lain yang terkait dengan distribusi frekuensi sangat bergantung kepada ragam yang digunakan. Makalah ini menelaah perbandingan distribusi frekuensi kata antara empat ragam bahasa Indonesia yang populer di internet, yaitu Kompas (media massa), Wikipedia bahasa Indonesia (ensiklopedia), Twitter (mikroblog), dan Kaskus (forum). Kajian dilakukan dengan menggunakan korpus yang diambil dari data yang tersedia secara publik di internet serta diproses dengan menggunakan bahasa pemrograman Python dan pustaka NLTK yang bersumber terbuka. Hasil kajian menunjukkan adanya perbedaan distribusi yang cukup tajam di antara keempat ragam bahasa Indonesia ini. Kompas banyak menggunakan kata "akan" karena sifat beritanya; Wikipedia banyak menggunakan kata "adalah" karena sifat deskriptifnya; Twitter banyak menggunakan kata "aku" karena sifat subjektifnya; Kaskus banyak menggunakan kata "gan" yang merupakan kata khas komunitas ini. Kajian ini juga memberikan beberapa hal yang harus diperhatikan dalam kajian serupa seperti penyiapan dan pembersihan data korpus dan leksikon. Kajian ini diharapkan dapat memberikan dasar penelitian lebih lanjut dalam bidang distribusi frekuensi dan analisis korpus bahasa Indonesia.

Frekuensi penggunaan kata dalam sebuah tulisan maupun percakapan sangat memengaruhi waktu tanggap penggunanya. Semakin sering suatu kata digunakan, semakin cepat kata pula tersebut dipahami. (Whaley, 1978; Ford et al., 2003). Menurut Tryk (1969), frekuensi penggunaan sebuah kata juga sering menjadi variabel pembeda antara ragam lisan dan ragam tulis. Di sisi lain, pemilihan kata dapat dianggap sebagai representasi pengetahuan penutur. Pengalaman penutur terhadap penggunaan sebuah kata harus dipertimbangkan di semua modalitas yang berhubungan dengan kata tersebut (Gernsbacher, 1984). Hal yang sama berlaku untuk makna dari kata yang dimaksud. Penutur memperoleh keakraban (*familiarity*) dengan kata tidak hanya dari menghadapi dan merasakannya, namun juga dari operasi semantik yang terlibat dalam pengolahan, khususnya dalam pemahaman, yang kemudian mengharuskan penutur memahami representasi bentuk kata dan maknanya. Keakraban dengan kedua representasi bentuk kata dan maknanya dapat secara bersamaan meningkat setiap kali kata tersebut diproses. Melalui makalah ini, kami juga menampilkan data-data yang menunjang asumsi keakraban penutur terhadap suatu kata melibatkan dua komponen yang berhubungan dengan bentuk kata (baik secara umum maupun secara spesifik) dan makna dari kata yang dimaksud.

## Publikasi

* Lanin, I., Geovedi, J., & Soegijoko. W. (2013). Perbandingan distribusi frekuensi kata bahasa Indonesia di Kompas, Wikipedia, Twitter, dan Kaskus. *Konferensi Linguistik Tahunan Atma Jaya 11 (KOLITA11)*.


## Data Olahan

Jika anda menggunakan data dan kode pemrograman yang terdapat dalam repositori ini dalam sebuah publikasi, harap sertakan kutipan makalah di atas.

Hanya 10,000 peringkat pertama kata saja dari setiap corpus yang ditampilkan di sini. 

### Corpora

* **idwiki** - 10,000 kata populer dari salinan situs Wikipedia bahasa Indonesia tanggal 15 Januari 2013.
    * idwiki.1gram - unigram (1-gram)
    * idwiki.csv - perhitungan kemunculan dan persentase Kemunculan Kata
* **kaskus** - 10,000 kata populer dari 1,000 *threads* terakhir sub-forum "The Lounge" pada situs forum Kaskus, yang diambil pada bulan Januari 2013.
    * kaskus.1gram - unigram (1-gram)
    * kasku.csv - perhitungan kemunculan dan persentase Kemunculan Kata
* **kompas** - 10,000 kata populer dari arsip berita tahun 2012 situs berita Kompas.
    * kompas.1gram - unigram (1-gram)
    * kompas.csv - perhitungan kemunculan dan persentase Kemunculan Kata
* **twitter** - 10,000 kata populer dari situs mikroblog Twitter untuk percakapan bulan Oktober-Desember 2012 oleh pengguna Twitter yang berlokasi di Indonesia.
    * twitter.1gram - unigram (1-gram)
    * twitter.csv - perhitungan kemunculan dan persentase Kemunculan Kata



## Kontak

Gen Eric. <gen.eric@ardwort.com>
