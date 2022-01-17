package e02genericsinstaticlanguage;

import java.util.ArrayList;
import java.util.List;

public class Example1 {
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add(1);
        list.add(2);
        // Commented out so that build does not fail
//        Integer int1 = list.get(0);
//        Integer int2 = list.get(1);
//        System.out.println(int1 + int2);
    }
}
