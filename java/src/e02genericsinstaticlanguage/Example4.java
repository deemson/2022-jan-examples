package e02genericsinstaticlanguage;

import java.util.ArrayList;
import java.util.List;

public class Example4 {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList();
        list.add(1);
        list.add(2);
        Integer int1 = list.get(0);
        Integer int2 = list.get(1);
        System.out.println(int1 + int2);
    }
}
