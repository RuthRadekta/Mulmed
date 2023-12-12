# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Guru = Character('Guru', color="#E03B8B")
define Suma = Character('Suma', color="#508D69")
define Stefan = Character('Stefan', color="#F3B664")
define Mbah = Character('Mbah', color="#872341")
define Kakek = Character('Kakek')
#image opening = "..."

#define sm = Character("Suma", image = "suma")

#image suma:
#    "side kusuma_restFace.png"

# The game starts here.

label splashscreen:
    scene black
    with Pause(1)

    show text "WELCOME TO THE PAST" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    $ renpy.movie_cutscene('flash.webm')
    scene fadeout white 0.5

    return

label start:
    centered "{color=#FFFFFF}(Bel pulang sekolah berbunyi){/color}"
    #play suara bel

label scene1:
    scene fadein 0.5
    scene ruangkelas_now
    #play suara riuh di kelas
    centered "{color=#FFFFFF}(Suara riuh di kelas){/color}"
    centered '{color=#FFF5C2}"Eh kata Pak Retno ulangan sejarah kapan?"{/color}'
    centered '{color=#FFF5C2}"Besok banget tuh"{/color}'
    show kusuma_suprisedface at left
    Suma "Huh?"
    Suma "(Menghela napas)"

label scene2:
    show kusuma_restface at left
    Suma "(Berjalan pulang dengan kesal)"
    Suma "Kenapa sih sejarah sok keras banget?"
    Suma "Toh, Sejarah kan yang penting tahu, "
    extend "gak harus WAJIB kek gini "
    extend "Ribet banget..."
    Suma "Mana pake ulangan segala lagi. "
    extend "Dikira mapel yang harus dipikir ini doang? "
    scene fadeout 1.5

label scene3:
    scene kamar suma 
    with fade
    centered "{color=#FFFFFF}(Sesampainya di rumah...){/color}"
    show kusuma_restface at left
    Suma "Ngantuk... "
    hide kusuma_restFace
    extend "Pen tidur..."
    scene fadeout 3.5

label scene4:
    scene kamar lama
    with fade
    show normal at left
    Suma "Loh? "
    extend "(Melihat sekitar) "
    extend "Kamar siapa ini? "
    centered '"Le, ijek durung tangi to?"'
    hide normal
    show kaget at left
    Suma "(Mendengar sesuatu) "
    extend "Huh? "
    extend "Ada orang jawa?! "
    Suma "Siapa?! "
    extend "Ayah ya? "
    extend "Tapi kok berat gitu... "
    centered "(Mbah Seno masuk ke kamar Suma dan berkacak pinggang)"
    Mbah "Le, le... turu teros! "
    extend "(Berjalan mendekati Suma) "
    show kaget at left
    Suma "(Membatin) Huh? "
    extend "Mbah Seno! "
    extend "Kok hidup lagi?! "
    Mbah "(Menepuk pipi Suma) "
    extend "Ngopo to koe ki? "
    extend "Ndang tangi, ngewangi simbah! "
    Mbah "(Lalu keluar dari kamar Suma) "
    Suma "(Kaget, tapi langsung nyusul)"
    scene fadeout 0.5

label scene5:
    hide kaget
    # nunjukin sekeliling rumah
    centered "(EDIT)entar nunjukin sekeliling rumah, kira-kira 4 gambar"
    centered "(Suma sampai halaman depan)"
    centered "(EDIT)entar nunjukin mbah seno yg berdiri dengan caping kepala dan bbrp peralatan berkebun"
    Mbah "Ayo! Gek ndang mangkat!"
    show kaget at left
    Suma "M-mau kemana mbah?"
    Mbah "Yo nyang ngendi neh? Sawah lah!"
    Suma "..."
    Suma "Ngapain ke sawah?"
    Mbah "Bosomu aneh"
    extend ". Pokoke awakdewe bakal noto sawah. "
    extend "(Melirik Suma) "
    extend "Lak takon neh"
    Suma "(Terkekeh malu)"
    extend "Anu, Mbah... "
    extend "Sebenarnya aku gak paham sama maksud mbah, "
    extend "noto sawah itu apa ya, Mbah?"
    Mbah "(entar nunjukin muka kaget atau sejenisnya)"
    Mbah "Ngene lho, le. "
    extend "Keluargane awakdewe kan nduwe sawah, makane kui awakdewe kudu njogo. "
    extend "Kui sawah iso dadi sumber awakdewe urip karo dadi lapang kerjane masyarakat kampung"
    Mbah "(Melihat Suma dengan curiga)"
    Mbah "Biasane yo ngene ki lho, le. Kok koe dadi aneh men to?"
    hide kaget
    show normal at left
    Suma "(Menceritakan semua yang telah terjadi)"
    centered "..."
    Mbah "(Tertawa kecil) "
    extend "Lah... pantes kok bedo. Jebule koe cicitku to"
    Suma "(Tertawa canggung)"
    Mbah "(Berhenti tertawa)"
    Mbah "Yowes, tetep kerjo. Ayo!"
    hide normal
    scene fadeout 0.5

label scene6:
    centered "(EDIT)entar nampilin hamparan sawah hijau yang membentang"
    centered "(EDIT)terus nampilin petani yang lagi bekerja di sawah"    
    show normal at left
    Suma "Mbah, apa yang harus aku lakukan di sini?"
    hide normal
    Mbah "(Tersenyum)"
    Mbah "Yo seko kene ki, le. Lapang kerja masyarakat kampung, panggon kanggo wong-wong desa kerjo ning kene, garap sawah iki."
    extend " Iki yo bagian sekolah adat Jawa sing kudu koe reti, le. Koe bakal sinau cara garap sawah,"
    extend " nah seko kono koe bakal paham artine kerja keras karo gotong royong."
    Mbah "Kan yo manungsa urip gelem ra gelem akhire bakal bersosialisasi. Dadi ojo opo-opo ngeroso iso dewe ya, le."
    extend " Saiki, yoh mulai garap."
    show normal at left
    Suma "(Sedikit ragu, tetapi dia tetap mencoba beradaptasi dengan situasi yang dihadapi.)"
    centered "(Selama mereka bekerja, Mbah Seno menceritakan kisah-kisah tentang masa lalu bagaimana Belanda datang ke Indonesia dan perjuangan rakyat Indonesia saat melawan penjajahan Belanda)"
    centered "(Suma mendengarkan dengan penuh perhatian)"
    hide normal

    # sesi kuis
    # pertanyaan nih
    Mbah "Pie, Le? Wes paham?"
    menu:
        "Udah, mbah" :
            jump berikutnya
        "Belum..." :
            jump ulang 

    label berikutnya:
        Mbah "Yowes sip"
        jump scene7
    
    label ulang:
        Mbah "Waduh."
        Mbah "Dengerno ya, Le... "
        extend "Jadi intinya kamu harus mau bersosialisasi. Bukan masalah bakal menyebabkan ketergantungan..."
        Mbah "Tapi, "
        extend "begitulah cara manusia hidup. "
        extend "Saling tolong0-menolong dan gotong royong..."
        jump scene7

label scene7:
    centered "(Setelah beberapa jam bekerja di sawah, Suma paham apa yang dimaksud Mbah Seno)"
    centered "(Selain itu, mereka mulai akrab layaknya keluarga)"
    Mbah "Bagus, le. Kau telah belajar banyak hari ini."
    Mbah "Ini adalah langkah awal dalam perjalananmu untuk memahami sejarah dan budaya kita. "
    extend "Ingatlah, kita harus menghargai warisan nenek moyang kita dan belajar dari mereka."
    Suma "(Mengangguk paham)"
    Suma "Terima kasih, Mbah. Aku akan mencoba yang terbaik."
    Mbah "(Mengangkat sebelah alisnya)" 
    extend "Sampai kapan kau akan tinggal di sini, le?"
    Suma "Aku belum tahu, Mbah... "
    extend "(Tersenyum) "
    extend "Tapi sepertinya aku bakal betah di sini"
    Mbah "(Tersenyum kembali)" 
    Mbah "Yowes, le. Ayo bali. Kita masih punya banyak yang harus kau pelajari."  
    centered "(Mereka berdua meninggalkan sawah dan kembali ke rumah yang jauh berbeda dari rumah Suma di masa kini)"
    scene fadeout 0.5
    Suma "Siapa tuh, mbah?"
    extend "(tanya Suma penasaran saat ada pemuda yang menyapa mbah Seno saat hendak masuk ke halaman rumahnya)"
    Mbah "Oh.. jenenge Sutan Syahrir. "
    extend "Tapi biasane aku nyeluk ‘Si Kancil’ "
    Suma "... (gak paham bahasa jawa)"
    Mbah "(Tertawa melihat wajah bingung Suma)"
    Mbah "Maksudnya, nama orang itu Sutan Syahrir. Tapi mbah biasanya manggil ‘Si Kancil’, paham?"
    Suma "Oh..."
    extend "Terus beliau mau pergi kemana itu, mbah?"
    Mbah "Rumahnya lah."
    Mbah "Katanya habis datang dari Konferensi Rijswijk yang berlangsung pada tahun ini, 1939. "
    extend "Tujuannya untuk membahas masalah dan perselisihan antara pemerintah kolonial Belanda dan para pemimpin Indonesia."
    Mbah "Masalah utama yang dibahas termasuk otonomi ekonomi untuk Hindia Belanda, peningkatan status politik, dan kemerdekaan."
    Mbah "Pemimpin konferensi ini ya Si Kancil, tapi di didampingi Tjarda van Starkenborgh, gubernur jendral dari Belanda."
    Mbah "Tapi katanya hasil konferensi ini belum mencapai kesepakatan konkret. "
    extend "Alhasil, kontrol Belanda di Indonesia masih erat dan pokoke waspada ae ya, le."
    Suma "(Mengangguk)"
    Mbah "(Duduk di teras setelah cuci kaki dan tangan)"
    Mbah "Oiyo le, rene sek."
    Suma "(Duduk di sebelahnya) Ya, mbah?"
    Mbah "Mbah sudah cerita tentang Pangeran Diponegoro belum to?"
    Suma "(Menggelengkan kepala)"
    Mbah "Pangeran Diponogoro itu pemimpinnya Perang Diponegoro, perang yang terjadi di Jawa pada masa kolonial Belanda (1825-1830). "
    extend "Pangeran Diponegoro memimpin perlawanan terhadap tindakan Belanda yang merampas tanahnya dan mengeksploitasi rakyat dengan pajak yang tinggi. "
    Mbah "Perlawanan Diponegoro mendapatkan dukungan dari rakyat dan berlangsung sengit di berbagai wilayah Jawa."
    Mbah "Perang ini melibatkan berbagai metode perang modern, termasuk perang terbuka dan gerilya. Belanda menggunakan berbagai cara licik untuk menangkap Diponegoro, "
    extend "termasuk mengeluarkan sayembara. "
    Mbah "Terus perubahan strategi Belanda terjadi ketika Gubernur Jenderal De Kock menggunakan strategi perbentengan untuk membatasi gerak Diponegoro. "
    Mbah "Perlawanan Diponegoro semakin melemah setelah beberapa pemimpinnya ditangkap. Pada akhirnya, Diponegoro ditangkap pada hari Idulfitri tahun 1830 dan diasingkan ke Manado, lalu Makassar, hingga meninggal di Benteng Rotterdam pada tahun 1855. "
    Mbah "Paham gak?"
    Suma "..."
    menu:
        "Paham, mbah!" :
            jump paham 
        "Enggak hehe..." :
            jump gakpaham
    
    label paham:
        Mbah "Mantap!"
        jump scene8

    label gakpaham:
        Mbah "Waduh waduh..."
        extend "Rungokne ya, le..."
        Mbah "Pangeran Diponogoro itu pemimpinnya Perang Diponegoro, perang yang terjadi di Jawa pada masa kolonial Belanda (1825-1830). "
        extend "Pangeran Diponegoro memimpin perlawanan terhadap tindakan Belanda yang merampas tanahnya dan mengeksploitasi rakyat dengan pajak yang tinggi. "
        Mbah "Perlawanan Diponegoro mendapatkan dukungan dari rakyat dan berlangsung sengit di berbagai wilayah Jawa."
        Mbah "Perang ini melibatkan berbagai metode perang modern, termasuk perang terbuka dan gerilya. Belanda menggunakan berbagai cara licik untuk menangkap Diponegoro, "
        extend "termasuk mengeluarkan sayembara. "
        Mbah "Terus perubahan strategi Belanda terjadi ketika Gubernur Jenderal De Kock menggunakan strategi perbentengan untuk membatasi gerak Diponegoro. "
        Mbah "Perlawanan Diponegoro semakin melemah setelah beberapa pemimpinnya ditangkap. Pada akhirnya, Diponegoro ditangkap pada hari Idulfitri tahun 1830 dan diasingkan ke Manado, lalu Makassar, hingga meninggal di Benteng Rotterdam pada tahun 1855. "
        Mbah "Dah paham?"
        Suma "(Mengangguk) Yup!"
        jump scene8

label scene8:
    Mbah "Sudah pernah lihat lukisannya yang di gambar Raden Saleh belum?"
    Suma "Belummm"
    centered "(Lalu mbah Seno pergi ke dalam dan mengambil gambaran kecil)"
    centered "(Beberapa menit kemudian, mbah Seno kembali dan menunjukkan gambaran itu kepada Suma)"
    centered "(Walaupun hanya duplikat, tapi masih tetap mirip)"

    #nah ini nunjukin gambarnya raden saleh

    #setelah itu kuis

label scene9:
    centered "Keesokkan harinya, Suma sedang berjalan di ruang tengah dan tidak sengaja menemukan sebuah buku terbuka yang tidak terlalu tebal."
    centered "Dikarenakan penasaran, dia mengambil buku tersebut dan membacanya."
    
    #nampilin bersatu kita teguh...

    Mbah "Moco gak izin sek. "
    extend "Kene"
    Suma "(Tertawa gugup)"
    extend "Hehe maaf, mbah. Sengaja."
    Mbah "Hm"
    Suma "Tapi mbah..."
    Mbah "Opo neh?"
    Suma "Itu karangan siapa?"
    Mbah "Oh, iki seko Nak Yamin. Iki diterbitne-"
    Suma "Mbahhh pake Bahasa Indonesia, dong. Ga paham akuuu"
    Mbah "Heleh. "
    extend "Gak tau nganggo boso kromo sih."
    Mbah "Ini sajak yang dibuat Muhammad Yamin, "
    extend "diterbitkan di Pasudan tanggal 26 Oktober 1928."
    Suma "26 Oktober 1928?!"
    extend "Sebelum Kongres Sumpah Pemuda II dong, mbah?"
    Mbah "Hiyo. Kok koe reti le?"
    Suma "Hehe ngerti dong, mbah"
    Mbah "Ndang cobo, kapan kui Kongres Pemudane?"
    menu:
        "benar":
            jump lanjut
        "salah":
            jump lanjut
    
    label lanjut:
        Mbah "Opo hasile?"
        menu:
            "benar":
                jump benar
            "salah":
                jump salah
    
    label benar:
        Mbah "Cucuku pinter tenan jebule"
        jump scene10
    
    label salah:
        Mbah "Heleh, jare ngerti?"
        jump scene10


label scene10:
    centered "(Setelah itu, Suma berpamitan untuk pergi ke sekolah karena ia mau tidak mau harus tetap pergi ke sekolah di zaman ini, walaupun harus tetap berpura-pura menjadi kakeknya)"
    
    # nanti muncul info ndek tengah
    # Kakeknya ini ternyata seorang yang ramah dan pekerja keras, berbanding balik dengan dirinya. Dia juga popular di kalangan sekolah dan sekitar karena kecerdasannya, selain itu dia adalah seorang ketua salah satu organisasi tersembunyi di sekolah yang ikut memperjuangkan kemerdekaan.  

    Suma "(Melihat sekitar) "
    extend "kok bule semua ya? cowo semua lagi (batinnya)"

    centered "..."

    Suma "(Duduk di bangkunya)"

    # Pertemuan dengan Stefan
    centered '"Hey!"'

    Suma "(Merasa bahunya ditepuk)"
    extend "(menoleh)"
    show torasumaji_suprisedFace at left
    Suma "Eh penjajah?!?"
    hide torasumaji_suprisedFace

    show stefan_restFace at left
    Stefan "“Ada apa?”"
    hide stefan_restFace

    show torasumaji_restFace at left
    Suma "(...)"

    centered "Karena Suma masih berusaha untuk tidak berurusan dengan hal-hal aneh di sini, akhirnya dia hanya diam dan mengobservasi laki-laki itu dengan tatapan dingin."
    hide torasumaji_restFace

    show stefan_giggleFace at left
    Stefan "“Aku hanya minta tolong kau ajarkan math ini. Bisa?”"
    extend " (tanyanya dengan aksen Belanda yang masih kental.)"
    hide stefan_giggleFace

    Suma "“Hah?” (Bingung)"
    Stefan "“Hah??” (Ikut bingung)"
    Suma "(Menunjuk dirinya sendiri, dan menoleh kanan kiri untuk memastikan jika dirinya betulan yang dimintai tolong)"
    Stefan "“Iya! Karena kau pintar,”"
    Suma "(berdeham dan merasa percaya diri.)"
    extend " “… Gak mau,” (ucapnya gengsi)"
    Stefan "“Come on! Kau bisa mengajar pada semua. Tapi, aku tidak, kenapa??”"
    Suma "(mendesah kesal karena ia hampir saja lupa bahwa dia berada dalam tubuh kakeknya yang ramah)"
    extend " “Gue bahkan ga kenal lo. Sokap banget,”"
    centered "(Suma melirik ke arah lain. Dia tahu bahwa orang Belanda itu tidak mengerti ejekkannya, jadi dia bisa bebas menggunakan kosakata gaul di zamannya.)"
    Stefan "“Maksudmu?”"
    extend "(menatap bingung)"
    Suma "“Aku tidak mengenalmu, ‘kay? Do you understand?”"
    Stefan "“Aneh sekali kau tidak tahu aku, teman sekelas,"
    extend " Aku Stefan. Stefan Driessen,”"
    Suma "“Stefan?”"
    Stefan "(mengangguk beberapa kali dan mengacungkan jempol.)"
    Suma "“Tapi, ini tidak gratis,” (bersedekap)"
    Stefan "(mengangguk)"
    extend "“Ya, aku akan membayar.”"
    Suma "(“Uang? Mungkin ini gak begitu buruk.” batinnya)"


label scene11:
    centered "(Sebelum pulang sekolah, Suma sedang melihat-lihat sekitar di kelas ini karena rasa kagumnya belum sirna. Salah satu benda yang menarik perhatiannya adalah sebuah pajangan kata-kata yang berfigurakan kayu.)"

    centered "Ing ngarsa sung tuladha. Ing madya mangun Karsa. Tut wuri handayani.  ~ Ki Hadjar Dewantara"

    Suma "(membaca kata-kata tersebut)"
    extend " “Hah?”"
    Stefan "“Hah?”"
    extend " (menoleh dari samping Suma)"
    Suma "(menatap Stefan)" 
    extend "“Itu… pajangan itu didapat darimana?”"
    Stefan "“Oh! Benda itu dibuat oleh salah satu guru."
    extend "Katanya dia suka dan terkesan dengan semboyan Ki Hadjar Dewantara.”"
    Suma "“Kenapa? Emang artinya apa?”"
    Stefan "“Ing Ngarso Sung Tulodo artinya nmenjadi seorang pemimpin harus mampu memberikan suri tauladan."
    extend "Ing Madyo Mbangun Karso, artinya seseorang ditengah kesibukannya harus juga mampu membangkitkan atau menggugah semangat."
    extend "Tut wuri handayani, artinya di belakang bisa memberi dorongan”"
    Suma "“Kok kamu tahu?”"
    Stefan "“Guru itu yang mengartikannya untukku,”"
    extend "(menjawab dengan bangga.)"
    Suma "“Oh. Ya sudah. Thanks,”"

    centered "(Suma mulai berjalan dari kelas untuk pulang dan diikuti oleh Stefan.)"


label scene12:
    centered "(Saat ini mereka berada di rumah Stefan pada sore hari karena Suma sudah setuju untuk membantu Stefan dengan Pelajaran matematika. Rumah itu terletak di dekat sekolah, tetapi Suma merasa tidak familiar dengan bangunan tua ini, yang jauh berbeda dari rumah-rumah modern yang dia kenal.)"

    centered "(Stefan membawa buku matematika yang tebal, dan mereka duduk di meja belajar di ruang keluarga. Suma mulai menjelaskan pelajaran matematika dengan tekun, sementara Stefan dengan penuh semangat mencoba mengerti dan mengikuti penjelasan Suma. Meskipun ada perbedaan bahasa dan budaya di antara mereka, mereka akhirnya mulai bekerja sama dengan baik.)"

    centered "(Selama proses belajar, Suma mulai merasa bahwa Stefan tidak begitu buruk seperti yang dia kira awalnya. Dia melihat kegigihan Stefan untuk memahami pelajaran matematika dan bagaimana dia mencoba keras untuk belajar, meskipun bahasanya bukan bahasa ibunya. Mereka mulai berbicara tentang hal-hal lain di luar pelajaran, dan akhirnya, mereka mulai berbagi cerita tentang kehidupan mereka masing-masing di masa kini)"






label bgm:
    #play music "audio/suma_theme.mp3" fadein 1.0 volume 10
    show kaget at left
    Suma "Buset? Londo!"
    hide kaget

    show stefan_restface at left
    Stefan "Huh?"

    hide stefan_restface
    
label sfx:

label choices:
    #default learned = False
    show kaget at left
    Suma "Dee londo kan ya?"
    menu:
        "Hoo":
            jump hoo
        "Lah embuh":
            jump embuh

label hoo:
    hide kaget
    show stefan_giggleface at left
    Stefan "Apa itu 'Londo'?"
    jump lanjutan_hoo

label lanjutan_hoo:
    Suma "..."
    scene black
    jump end

label embuh:
    hide kaget
    show stefan_restface at left
    Stefan "Embuh? Apa itu 'embuh'?"
    jump lanjutan_embuh

label lanjutan_embuh:
    Suma "(His jaw dropped)"
    scene black
    jump end

label end:
    #with fade
    $renpy.full_restart()
    return

    

    return
