package Salary_Exercise.application;

import Salary_Exercise.entities.Employee;

import java.util.Scanner;

public class Program {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Employee employee = new Employee();
        System.out.print("Name: ");
        employee.name = sc.nextLine();
        System.out.print("GlossSalary: ");
        employee.glossSalary = sc.nextDouble();
        System.out.print("Tax: ");
        employee.tax = sc.nextDouble();

        System.out.println("Employee: " + employee);
        System.out.print("Which percentage to increase salary? ");
        double perctTaxa = sc.nextDouble();
        employee.increaseSalary(perctTaxa);
        System.out.print("Update data: " + employee);

    }
}
