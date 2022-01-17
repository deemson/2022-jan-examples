package e10covariance;

import java.util.ArrayList;
import java.util.List;

public class Example1 {
    static void printAnimalNames(List<Animal> animals) {
        for (Animal animal : animals) {
            System.out.println(animal.getName());
        }
    }

    public static void main(String[] args) {
        List<Cat> cats = new ArrayList<>();
        cats.add(new Cat("Rocky"));
        cats.add(new Cat("Teddy"));
//        printAnimalNames(cats);
    }
}
