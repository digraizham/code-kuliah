package UTS;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        try (Scanner sc = new Scanner(System.in)) {         

            System.out.println("Daftar Buku:");
            System.out.println("1. Buku Sekolah/Kuliah");
            System.out.println("2. Buku Novel");
            System.out.println("3. Cerita Pendek");
            System.out.println("4. Cerita Bergambar");
            System.out.println("5. Majalah");
            System.out.println("6. Jurnal Ilmiah");
            System.out.println("7. Surat Kabar");
            System.out.println("Masukkan Input (Angka): ");
            int inputbuku = sc.nextInt();

            System.out.println("Tujuan: ");
            System.out.println("1. Peminjaman");
            System.out.println("2. Baca di tempat");
            System.out.println("Masukkan Input (Angka): ");
            int tujuan = sc.nextInt();

            if (inputbuku == 1){
                if (tujuan == 1) {
                    System.out.println("Silahkan ini bukunya");
                }
                else if(tujuan == 2){
                    System.out.println("Silahkan ini bukunya");
                }
            }
            else if(inputbuku == 2){
                if (tujuan == 1) {
                    System.out.println("Silahkan ini bukunya");
                }
                else if(tujuan == 2){
                    System.out.println("Silahkan ini bukunya");
                }
            }
            else if(inputbuku == 3){
                if (tujuan == 1) {
                    System.out.println("Maaf buku ini tidak dapat dipinjam");
                }
                else if(tujuan == 2){
                    System.out.println("Silahkan ini bukunya");
                }
            }
            else if(inputbuku == 4){
                if (tujuan == 1) {
                    System.out.println("Maaf buku ini tidak dapat dipinjam");
                }
                else if(tujuan == 2){
                    System.out.println("Silahkan ini bukunya");
                }
            }
            else if(inputbuku == 5){
                if (tujuan == 1) {
                    System.out.println("Silahkan ini bukunya");
                }
                else if(tujuan == 2){
                    System.out.println("Silahkan ini bukunya");
                }
            }
            else if(inputbuku == 6){
                System.out.println("Masukkan nama anda:");
                String nama = sc.nextLine();

                if(Keanggotaan.main(args).containsKey(nama) == true){
                    if (Keanggotaan.main(args).containsValue("Anggota Ekslusif") == true){
                        System.out.println("Silahkan ini bukunya.");
                    }
                    else if(Keanggotaan.main(args).containsValue("Anggota Ekslusif") == false){
                        System.out.println("Maaf buku ini hanya bisa dibaca oleh anggota ekslusif.");
                    }
                }
                else if (Keanggotaan.main(args).containsKey(nama) == false){
                    System.out.println("Maaf buku ini hanya bisa dibaca oleh anggota perpustakaan yang termasuk anggota ekslusif.");
                }
            }
            else if(inputbuku == 7){
                if (tujuan == 1) {
                    System.out.println("Silahkan ini bukunya");
                }
                else if(tujuan == 2){
                    System.out.println("Silahkan ini bukunya");
                }
            }

        }  
    }
}
