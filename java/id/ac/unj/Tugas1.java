package id.ac.unj;
import java.util.Scanner;

public class Tugas1{
    public static void main(String[] args){
        Scanner name = new Scanner(System.in);
        System.out.print("Masukkan nama Anda: ");
        String user_name = name.nextLine();
    
        Scanner age = new Scanner(System.in);
        System.out.print("Tahun berapa Anda dilahirkan: ");
        int user_age = 2022 - age.nextInt();
        
        name.close();
        age.close();

        System.out.println();
        System.out.println("Selamat datang " + user_name);
        System.out.println("Anda berumur " + user_age + " tahun");
    }
}
//Digra Murtaza Izham - 1313621010
// Tugas1 - DPBO 117