# ============================================================
#   FUTBOL LIGASI BOSHQARUV TIZIMI — 10 ta sinf
# ============================================================

from abc import ABC, abstractmethod
import random


# ============================================================
# 1. SHAXS (asosiy abstrakt sinf)
# ============================================================
class Shaxs(ABC):
    def __init__(self, ism: str, yosh: int, millat: str):
        self.ism = ism
        self.yosh = yosh
        self.millat = millat

    @abstractmethod
    def rol(self) -> str:
        pass

    def __str__(self):
        return f"{self.ism} ({self.yosh} yosh) — {self.rol()}"


# ============================================================
# 2. O'YINCHI
# ============================================================
class Oyinchi(Shaxs):
    def __init__(self, ism: str, yosh: int, millat: str,
                 pozitsiya: str, raqam: int, narx_mln: float):
        super().__init__(ism, yosh, millat)
        self.pozitsiya = pozitsiya
        self.raqam = raqam
        self.narx_mln = narx_mln
        self.jamoa: "Jamoa | None" = None
        self._gol = 0
        self._assist = 0
        self._sariq_karta = 0
        self._qizil_karta = 0
        self._o_yinlar = 0

    def rol(self) -> str:
        return f"O'yinchi — {self.pozitsiya}"

    def gol_urish(self):
        self._gol += 1
        print(f"GOL! {self.ism} ({self.jamoa.nomi if self.jamoa else '?'}) — "
              f"jami: {self._gol} gol")

    def assist_berish(self):
        self._assist += 1
        print(f"Assist! {self.ism} — jami: {self._assist} assist")

    def sariq_karta(self):
        self._sariq_karta += 1
        print(f"Sariq karta! {self.ism} — jami: {self._sariq_karta} ta")
        if self._sariq_karta % 5 == 0:
            print(f"{self.ism} keyingi o'yinni o'tkazar!")

    def qizil_karta(self):
        self._qizil_karta += 1
        print(f"QIZIL KARTA! {self.ism} maydandan chiqarildi!")

    def statistika(self):
        print(f"\n#{self.raqam} {self.ism} ({self.pozitsiya}):")
        print(f"  Millat      : {self.millat}")
        print(f"  Narx        : €{self.narx_mln}M")
        print(f"  O'yinlar    : {self._o_yinlar}")
        print(f"  Gollar      : {self._gol}")
        print(f"  Assistlar   : {self._assist}")
        print(f"  Sariq karta : {self._sariq_karta}")
        print(f"  Qizil karta : {self._qizil_karta}")


# ============================================================
# 3. MURABBIY
# ============================================================
class Murabbiy(Shaxs):
    def __init__(self, ism: str, yosh: int, millat: str,
                 tajriba_yil: int, oylik_mln: float):
        super().__init__(ism, yosh, millat)
        self.tajriba_yil = tajriba_yil
        self.oylik_mln = oylik_mln
        self._g_alaba = 0
        self._durang = 0
        self._mag_lubiyat = 0

    def rol(self) -> str:
        return "Murabbiy"

    def taktika_belgilash(self, sxema: str):
        print(f"Murabbiy {self.ism} taktikani belgiladi: {sxema}")

    def natija_qoshish(self, natija: str):
        if natija == "g'alaba":
            self._g_alaba += 1
        elif natija == "durang":
            self._durang += 1
        else:
            self._mag_lubiyat += 1

    def statistika(self):
        jami = self._g_alaba + self._durang + self._mag_lubiyat
        print(f"\nMurabbiy {self.ism}:")
        print(f"  Tajriba     : {self.tajriba_yil} yil")
        print(f"  Oylik       : €{self.oylik_mln}M")
        print(f"  Jami o'yin  : {jami}")
        print(f"  G'alaba     : {self._g_alaba}")
        print(f"  Durang      : {self._durang}")
        print(f"  Mag'lubiyat : {self._mag_lubiyat}")


# ============================================================
# 4. HAKAM
# ============================================================
class Hakam(Shaxs):
    def __init__(self, ism: str, yosh: int, millat: str, daraja: str):
        super().__init__(ism, yosh, millat)
        self.daraja = daraja
        self._boshqargan_oyinlar = 0

    def rol(self) -> str:
        return f"Hakam — {self.daraja}"

    def oyinni_boshlash(self, oyun: "Oyun"):
        self._boshqargan_oyinlar += 1
        print(f"\nHakam {self.ism} o'yinni boshladi: "
              f"{oyun.uy_jamoa.nomi} vs {oyun.mehmon_jamoa.nomi}")

    def hushtakni_chalinish(self, sabab: str):
        print(f"Hushtак! Hakam {self.ism}: {sabab}")

    def statistika(self):
        print(f"\nHakam {self.ism}:")
        print(f"  Daraja      : {self.daraja}")
        print(f"  Boshqargan  : {self._boshqargan_oyinlar} o'yin")


# ============================================================
# 5. STADION
# ============================================================
class Stadion:
    def __init__(self, nomi: str, shahar: str, sig_im: int):
        self.nomi = nomi
        self.shahar = shahar
        self.sig_im = sig_im
        self._o_tkazilgan_oyinlar = 0

    def oyin_otkazish(self, oyun: "Oyun"):
        tomoshabin = random.randint(
            int(self.sig_im * 0.5), self.sig_im
        )
        self._o_tkazilgan_oyinlar += 1
        daromad = tomoshabin * random.uniform(20, 80)
        print(f"\nStadion: {self.nomi} ({self.shahar})")
        print(f"  Tomoshabinlar: {tomoshabin:,} / {self.sig_im:,}")
        print(f"  Chipta daromad: €{daromad:,.0f}")
        return tomoshabin

    def __str__(self):
        return f"{self.nomi} — {self.shahar} ({self.sig_im:,} o'rin)"


# ============================================================
# 6. JAMOA
# ============================================================
class Jamoa:
    def __init__(self, nomi: str, shahar: str,
                 stadion: Stadion, byudjet_mln: float):
        self.nomi = nomi
        self.shahar = shahar
        self.stadion = stadion
        self.byudjet_mln = byudjet_mln
        self.murabbiy: Murabbiy | None = None
        self.oyinchilar: list[Oyinchi] = []
        self._g_alaba = 0
        self._durang = 0
        self._mag_lubiyat = 0
        self._gol_urdi = 0
        self._gol_yedi = 0
        self._ochko = 0

    def murabbiy_biriktirish(self, murabbiy: Murabbiy):
        self.murabbiy = murabbiy
        print(f"{murabbiy.ism} → {self.nomi} murabbiysi bo'ldi.")

    def oyinchi_qoshish(self, oyinchi: Oyinchi):
        narx = oyinchi.narx_mln
        if narx > self.byudjet_mln:
            print(f"{oyinchi.ism} sotib olib bo'lmaydi! "
                  f"Narx: €{narx}M, Byudjet: €{self.byudjet_mln}M")
            return False
        self.byudjet_mln -= narx
        oyinchi.jamoa = self
        self.oyinchilar.append(oyinchi)
        print(f"{oyinchi.ism} (#{oyinchi.raqam}) → {self.nomi} "
              f"| €{narx}M | Qoldiq: €{self.byudjet_mln:.1f}M")
        return True

    def oyinchi_sotish(self, oyinchi: Oyinchi):
        if oyinchi in self.oyinchilar:
            self.oyinchilar.remove(oyinchi)
            self.byudjet_mln += oyinchi.narx_mln
            oyinchi.jamoa = None
            print(f"{oyinchi.ism} sotildi. Byudjet: €{self.byudjet_mln:.1f}M")

    def natija_yangilash(self, natija: str, gol_urdi: int, gol_yedi: int):
        self._gol_urdi += gol_urdi
        self._gol_yedi += gol_yedi
        if natija == "g'alaba":
            self._g_alaba += 1
            self._ochko += 3
        elif natija == "durang":
            self._durang += 1
            self._ochko += 1
        else:
            self._mag_lubiyat += 1
        if self.murabbiy:
            self.murabbiy.natija_qoshish(natija)

    def tarkib(self):
        print(f"\n{self.nomi} tarkibi ({len(self.oyinchilar)} o'yinchi):")
        for o in self.oyinchilar:
            print(f"  #{o.raqam:2} {o.ism:20} — {o.pozitsiya}")

    def jadval_satri(self) -> str:
        jami = self._g_alaba + self._durang + self._mag_lubiyat
        farq = self._gol_urdi - self._gol_yedi
        return (f"{self.nomi:20} | {jami:2} | {self._g_alaba:2} "
                f"{self._durang:2} {self._mag_lubiyat:2} | "
                f"{self._gol_urdi}:{self._gol_yedi} ({farq:+d}) | "
                f"{self._ochko:3} ochko")

    def __str__(self):
        return f"{self.nomi} ({self.shahar})"


# ============================================================
# 7. O'YIN
# ============================================================
class Oyun:
    def __init__(self, uy_jamoa: Jamoa, mehmon_jamoa: Jamoa,
                 stadion: Stadion, hakam: Hakam, tur: int):
        self.uy_jamoa = uy_jamoa
        self.mehmon_jamoa = mehmon_jamoa
        self.stadion = stadion
        self.hakam = hakam
        self.tur = tur
        self._uy_gol = 0
        self._mehmon_gol = 0
        self._voqealar: list[str] = []
        self._tugadi = False

    def _voqea_qoshish(self, daqiqa: int, matn: str):
        self._voqealar.append(f"  {daqiqa}' — {matn}")
        print(f"  {daqiqa}' — {matn}")

    def o_ynash(self):
        self.hakam.oyinni_boshlash(self)
        self.stadion.oyin_otkazish(self)

        print(f"\n{'─'*45}")
        print(f"  {self.tur}-tur: {self.uy_jamoa.nomi} vs {self.mehmon_jamoa.nomi}")
        print(f"{'─'*45}")

        # O'yin simulyatsiyasi
        for daqiqa in sorted(random.sample(range(1, 91), 8)):
            hodisa = random.random()

            if hodisa < 0.25 and self.uy_jamoa.oyinchilar:
                o = random.choice(self.uy_jamoa.oyinchilar)
                self._uy_gol += 1
                o.gol_urish()
                self._voqea_qoshish(daqiqa,
                    f"GOL! {o.ism} ({self.uy_jamoa.nomi}) "
                    f"[{self._uy_gol}:{self._mehmon_gol}]")

            elif hodisa < 0.50 and self.mehmon_jamoa.oyinchilar:
                o = random.choice(self.mehmon_jamoa.oyinchilar)
                self._mehmon_gol += 1
                o.gol_urish()
                self._voqea_qoshish(daqiqa,
                    f"GOL! {o.ism} ({self.mehmon_jamoa.nomi}) "
                    f"[{self._uy_gol}:{self._mehmon_gol}]")

            elif hodisa < 0.70:
                jamoa = random.choice([self.uy_jamoa, self.mehmon_jamoa])
                if jamoa.oyinchilar:
                    o = random.choice(jamoa.oyinchilar)
                    o.sariq_karta()
                    self._voqea_qoshish(daqiqa,
                        f"Sariq karta — {o.ism} ({jamoa.nomi})")

            elif hodisa < 0.80:
                jamoa = random.choice([self.uy_jamoa, self.mehmon_jamoa])
                if jamoa.oyinchilar:
                    o = random.choice(jamoa.oyinchilar)
                    o.qizil_karta()
                    self._voqea_qoshish(daqiqa,
                        f"QIZIL KARTA — {o.ism} ({jamoa.nomi})")

        # Natija
        print(f"\n{'─'*45}")
        print(f"  YAKUNIY NATIJA: {self.uy_jamoa.nomi} "
              f"{self._uy_gol}:{self._mehmon_gol} "
              f"{self.mehmon_jamoa.nomi}")
        print(f"{'─'*45}")

        if self._uy_gol > self._mehmon_gol:
            self.uy_jamoa.natija_yangilash("g'alaba",   self._uy_gol,     self._mehmon_gol)
            self.mehmon_jamoa.natija_yangilash("mag'lubiyat", self._mehmon_gol, self._uy_gol)
        elif self._uy_gol < self._mehmon_gol:
            self.uy_jamoa.natija_yangilash("mag'lubiyat", self._uy_gol,   self._mehmon_gol)
            self.mehmon_jamoa.natija_yangilash("g'alaba", self._mehmon_gol, self._uy_gol)
        else:
            self.uy_jamoa.natija_yangilash("durang", self._uy_gol, self._mehmon_gol)
            self.mehmon_jamoa.natija_yangilash("durang", self._mehmon_gol, self._uy_gol)

        for o in self.uy_jamoa.oyinchilar + self.mehmon_jamoa.oyinchilar:
            o._o_yinlar += 1

        self._tugadi = True

    def __str__(self):
        if self._tugadi:
            return (f"{self.tur}-tur: {self.uy_jamoa.nomi} "
                    f"{self._uy_gol}:{self._mehmon_gol} "
                    f"{self.mehmon_jamoa.nomi}")
        return f"{self.tur}-tur: {self.uy_jamoa.nomi} vs {self.mehmon_jamoa.nomi}"


# ============================================================
# 8. TRANSFERLAR
# ============================================================
class TransferBozor:
    def __init__(self):
        self._transferlar: list[dict] = []

    def transfer_qilish(self, oyinchi: Oyinchi,
                        qayerdan: Jamoa, qayerga: Jamoa) -> bool:
        narx = oyinchi.narx_mln
        print(f"\nTransfer: {oyinchi.ism} | "
              f"{qayerdan.nomi} → {qayerga.nomi} | €{narx}M")
        if qayerga.byudjet_mln < narx:
            print(f"Byudjet yetmaydi! €{qayerga.byudjet_mln:.1f}M < €{narx}M")
            return False
        qayerdan.oyinchi_sotish(oyinchi)
        qayerga.oyinchi_qoshish(oyinchi)
        self._transferlar.append({
            "oyinchi": oyinchi.ism,
            "dan": qayerdan.nomi,
            "ga": qayerga.nomi,
            "narx": narx
        })
        return True

    def hisobot(self):
        print(f"\nTransfer bozori — {len(self._transferlar)} ta transfer:")
        jami = 0
        for t in self._transferlar:
            print(f"  {t['oyinchi']:20} | {t['dan']:15} → {t['ga']:15} | €{t['narx']}M")
            jami += t["narx"]
        print(f"  Jami transfer qiymati: €{jami:.1f}M")


# ============================================================
# 9. JADVAL (turniр taблицa)
# ============================================================
class Jadval:
    def __init__(self, liga_nomi: str):
        self.liga_nomi = liga_nomi
        self.jamoalar: list[Jamoa] = []

    def jamoa_qoshish(self, jamoa: Jamoa):
        self.jamoalar.append(jamoa)

    def chop_etish(self):
        tartiblangan = sorted(
            self.jamoalar,
            key=lambda j: (j._ochko, j._gol_urdi - j._gol_yedi),
            reverse=True
        )
        print(f"\n{'='*65}")
        print(f"  {self.liga_nomi} — TURNIR JADVALI")
        print(f"{'='*65}")
        print(f"  {'#':2} {'Jamoa':20} | {'O':2} | {'G':2} {'D':2} {'M':2} | "
              f"{'Farq':8} | {'Ochko':5}")
        print(f"{'─'*65}")
        for i, j in enumerate(tartiblangan, 1):
            jami = j._g_alaba + j._durang + j._mag_lubiyat
            farq = j._gol_urdi - j._gol_yedi
            print(f"  {i:2} {j.nomi:20} | {jami:2} | "
                  f"{j._g_alaba:2} {j._durang:2} {j._mag_lubiyat:2} | "
                  f"{j._gol_urdi}:{j._gol_yedi} ({farq:+d}) | "
                  f"{j._ochko:3}")
        print(f"{'='*65}")

    def bombardir(self):
        barcha = []
        for j in self.jamoalar:
            barcha.extend(j.oyinchilar)
        tartiblangan = sorted(barcha, key=lambda o: o._gol, reverse=True)
        print(f"\nBombardirlar:")
        print(f"{'─'*40}")
        for o in tartiblangan[:5]:
            print(f"  {o.ism:20} ({o.jamoa.nomi if o.jamoa else '?':15}) "
                  f"— {o._gol} gol")


# ============================================================
# 10. LIGA (hamma narsani birlashtiradi)
# ============================================================
class Liga:
    def __init__(self, nomi: str, mamlakat: str, mavsum: str):
        self.nomi = nomi
        self.mamlakat = mamlakat
        self.mavsum = mavsum
        self.jadval = Jadval(nomi)
        self.transfer_bozor = TransferBozor()
        self.oyinlar: list[Oyun] = []
        self.hakamlar: list[Hakam] = []

    def jamoa_qoshish(self, jamoa: Jamoa):
        self.jadval.jamoa_qoshish(jamoa)
        print(f"Liga: {jamoa.nomi} qo'shildi.")

    def hakam_qoshish(self, hakam: Hakam):
        self.hakamlar.append(hakam)

    def oyun_utkazish(self, uy: Jamoa, mehmon: Jamoa, tur: int):
        hakam = random.choice(self.hakamlar)
        oyun = Oyun(uy, mehmon, uy.stadion, hakam, tur)
        oyun.o_ynash()
        self.oyinlar.append(oyun)
        return oyun

    def mavsum_hisoboti(self):
        print(f"\n{'='*65}")
        print(f"  {self.nomi} — {self.mavsum} MAVSUM YAKUNI")
        print(f"{'='*65}")
        print(f"  Jami o'yinlar: {len(self.oyinlar)}")
        jami_gol = sum(o._uy_gol + o._mehmon_gol for o in self.oyinlar)
        print(f"  Jami gollar  : {jami_gol}")
        self.jadval.chop_etish()
        self.jadval.bombardir()


# ============================================================
# ISHLATISH
# ============================================================
if __name__ == "__main__":

    # --- Stadionlar ---
    st1 = Stadion("Milliy stadion",    "Toshkent",   35000)
    st2 = Stadion("Bunyodkor Arena",   "Toshkent",   34000)
    st3 = Stadion("Lokomotiv stadion", "Toshkent",   25000)
    st4 = Stadion("Pakhtakor stadion", "Toshkent",   45000)

    # --- Jamoalar ---
    print("\n--- JAMOALAR ---")
    pakhtakor  = Jamoa("Pakhtakor",  "Toshkent", st4, 50.0)
    bunyodkor  = Jamoa("Bunyodkor",  "Toshkent", st2, 40.0)
    lokomotiv  = Jamoa("Lokomotiv",  "Toshkent", st3, 30.0)
    nasaf      = Jamoa("Nasaf",      "Qarshi",   st1, 25.0)

    # --- Murabbiylar ---
    print("\n--- MURABBIYLAR ---")
    m1 = Murabbiy("Srecko Katanec",  62, "Xorvatiya",  30, 1.5)
    m2 = Murabbiy("Vadim Abramov",   55, "O'zbekiston", 20, 0.8)
    m3 = Murabbiy("Bakhrom Tursunov",50, "O'zbekiston", 15, 0.6)
    m4 = Murabbiy("Zafar Xolmatov", 48, "O'zbekiston", 12, 0.5)

    pakhtakor.murabbiy_biriktirish(m1)
    bunyodkor.murabbiy_biriktirish(m2)
    lokomotiv.murabbiy_biriktirish(m3)
    nasaf.murabbiy_biriktirish(m4)

    # --- O'yinchilar ---
    print("\n--- O'YINCHILAR SOTIB OLINMOQDA ---")
    # Pakhtakor
    pakhtakor.oyinchi_qoshish(Oyinchi("Eldor Shomurodov", 28, "O'zbekiston", "FWD", 9,  15.0))
    pakhtakor.oyinchi_qoshish(Oyinchi("Jaloliddin Masharipov", 30, "O'zbekiston", "MID", 7, 8.0))
    pakhtakor.oyinchi_qoshish(Oyinchi("Sarvarbek Tursunov", 24, "O'zbekiston", "DEF", 5, 4.0))

    # Bunyodkor
    bunyodkor.oyinchi_qoshish(Oyinchi("Dostonbek Xasanov",  25, "O'zbekiston", "FWD", 10, 6.0))
    bunyodkor.oyinchi_qoshish(Oyinchi("Ibrohim Rabimov",    27, "O'zbekiston", "MID", 8,  5.0))
    bunyodkor.oyinchi_qoshish(Oyinchi("Sherzod Nasimov",    22, "O'zbekiston", "GK",  1,  3.0))

    # Lokomotiv
    lokomotiv.oyinchi_qoshish(Oyinchi("Otabek Yunusov",   26, "O'zbekiston", "FWD", 11, 4.0))
    lokomotiv.oyinchi_qoshish(Oyinchi("Firdavs Toshev",   23, "O'zbekiston", "MID", 6,  3.0))

    # Nasaf
    nasaf.oyinchi_qoshish(Oyinchi("Behruz Mirzayev", 29, "O'zbekiston", "FWD", 9, 3.0))
    nasaf.oyinchi_qoshish(Oyinchi("Alisher Djalolov",25, "O'zbekiston", "DEF", 4, 2.0))

    # --- Hakamlar ---
    print("\n--- HAKAMLAR ---")
    h1 = Hakam("Ravshan Irmatov",  45, "O'zbekiston", "FIFA")
    h2 = Hakam("Abduxamid Rasulov",38, "O'zbekiston", "Milliy")
    liga_uz = Liga("O'zbekiston Superligasi", "O'zbekiston", "2025/26")
    liga_uz.hakam_qoshish(h1)
    liga_uz.hakam_qoshish(h2)

    # --- Liga ---
    print("\n--- LIGA TUZILMOQDA ---")
    liga_uz.jamoa_qoshish(pakhtakor)
    liga_uz.jamoa_qoshish(bunyodkor)
    liga_uz.jamoa_qoshish(lokomotiv)
    liga_uz.jamoa_qoshish(nasaf)

    # --- Tarkib ---
    pakhtakor.tarkib()
    bunyodkor.tarkib()

    # --- Transfer ---
    print("\n--- TRANSFER BOZORI ---")
    liga_uz.transfer_bozor.transfer_qilish(
        nasaf.oyinchilar[0], nasaf, bunyodkor
    )

    # --- O'yinlar ---
    print("\n--- 1-TUR ---")
    liga_uz.oyun_utkazish(pakhtakor, bunyodkor, 1)
    liga_uz.oyun_utkazish(lokomotiv, nasaf,     1)

    print("\n--- 2-TUR ---")
    liga_uz.oyun_utkazish(bunyodkor, lokomotiv, 2)
    liga_uz.oyun_utkazish(nasaf,     pakhtakor, 2)

    print("\n--- 3-TUR ---")
    liga_uz.oyun_utkazish(pakhtakor, lokomotiv, 3)
    liga_uz.oyun_utkazish(nasaf,     bunyodkor, 3)

    # --- Transfer hisoboti ---
    liga_uz.transfer_bozor.hisobot()

    # --- Statistika ---
    print("\n--- O'YINCHI STATISTIKASI ---")
    for j in [pakhtakor, bunyodkor]:
        for o in j.oyinchilar:
            o.statistika()

    # --- Murabbiy ---
    print("\n--- MURABBIY STATISTIKASI ---")
    m1.statistika()
    m2.statistika()

    # --- Hakam ---
    h1.statistika()

    # --- Mavsum hisoboti ---
    liga_uz.mavsum_hisoboti()