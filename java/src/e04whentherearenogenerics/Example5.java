package e04whentherearenogenerics;

import java.util.ArrayList;
import java.util.List;

public class Example5 {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList();
        list.add(1);
        // Commented out so that build does not fail
//        String s = (String) list.get(0);
//        System.out.println(s);
    }
}
