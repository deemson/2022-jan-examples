package e04whentherearenogenerics;

import java.util.ArrayList;
import java.util.List;

public class Example3 {
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add(1);
        String aString = (String) list.get(0);
        System.out.println(aString);
    }
}
