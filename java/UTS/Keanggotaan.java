package UTS;

import java.util.HashMap;

public class Keanggotaan {
    String nama;

    public static HashMap<String, String> main(String[] args) {
        HashMap<String, String> DaftarAnggota = new HashMap<String, String>();
        DaftarAnggota.put("daffa", "Anggota Ekslusif");
        DaftarAnggota.put("adi", "Anggota Gratis");
        DaftarAnggota.put("budi", "Anggota Ekslusif");

        
        return DaftarAnggota;
    }
}
