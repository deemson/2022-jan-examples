package e04whentherearenogenerics;

import java.util.ArrayList;
import java.util.List;

public class Example2 {
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add(1);
        list.add(2);
        Integer int1 = (Integer) list.get(0);
        Integer int2 = (Integer) list.get(1);
        System.out.println(int1 + int2);
    }
}
