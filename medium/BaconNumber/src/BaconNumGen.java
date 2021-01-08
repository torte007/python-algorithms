//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

import cop3530.KevinBaconGame;
import java.io.IOException;

public class BaconNumGen {
    public BaconNumGen() {
    }

    public static void main(String[] args) throws IOException {
        int count = false;
        long start_time = System.currentTimeMillis();
        KevinBaconGame KBG = new KevinBaconGame("bacon.ser");
        System.out.println("Finished reading data file. Processing queries ...");
        System.out.println("Barkin, Ellen " + KBG.getBaconNumber("Barkin, Ellen"));
        System.out.println("Forbes, Gail " + KBG.getBaconNumber("Forbes, Gail"));
        System.out.println("Weidenheft, John " + KBG.getBaconNumber("Weidenheft, John"));
        System.out.println("Shepard, Joan " + KBG.getBaconNumber("Shepard, Joan"));
        System.out.println("McCabe, Elias " + KBG.getBaconNumber("McCabe, Elias"));
        System.out.println("Abrams, Katharine " + KBG.getBaconNumber("Abrams, Katharine"));
        System.out.println("Helfer, Tricia " + KBG.getBaconNumber("Helfer, Tricia"));
        System.out.println("Hedley, Hugo " + KBG.getBaconNumber("Hedley, Hugo"));
        System.out.println("Versace, Gianni " + KBG.getBaconNumber("Versace, Gianni"));
        System.out.println("Nakasone, Rino " + KBG.getBaconNumber("Nakasone, Rino"));
        System.out.println("Enright, Brock " + KBG.getBaconNumber("Enright, Brock"));
        System.out.println("Harvey, Don (I) " + KBG.getBaconNumber("Harvey, Don (I)"));
        System.out.println("Metelmann, Henry " + KBG.getBaconNumber("Metelmann, Henry"));
        System.out.println("Allan, Patti " + KBG.getBaconNumber("Allan, Patti"));
        System.out.println("Reece, Deborah " + KBG.getBaconNumber("Reece, Deborah"));
        Runtime rt = Runtime.getRuntime();
        int vmavail = (int)rt.totalMemory();
        int vmfree = (int)rt.freeMemory();
        int vmsize = vmavail - vmfree;
        System.out.println("Virtual machine available: " + vmavail + " Bytes");
        System.out.println("Virtual machine size: " + vmsize + " Bytes");
        long end_time = System.currentTimeMillis();
        System.out.println("Execution time = " + (end_time - start_time) + " milliseconds");
    }
}
