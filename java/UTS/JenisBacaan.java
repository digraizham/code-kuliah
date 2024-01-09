package UTS;

import java.util.ArrayList;

public class JenisBacaan {

    public static ArrayList<String> main(String[] args) {

        ArrayList<String> DaftarBacaan = new ArrayList<String>();
        DaftarBacaan.add("Buku Sekolah");
        DaftarBacaan.add("Buku Novel");
        DaftarBacaan.add("Cerita Pendek");
        DaftarBacaan.add("Cerita Bergambar");
        DaftarBacaan.add("Majalah");
        DaftarBacaan.add("Jurnal Ilmiah");
        DaftarBacaan.add("Surat Kabar");

        System.out.println(DaftarBacaan);
        return DaftarBacaan;
    }
}