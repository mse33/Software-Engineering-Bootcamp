// Project class.
// Create attributes
public class Project {

    int projectNum;
    String projectName;
    String buildingType;
    String address;
    int erfNum;
    double totalFee;
    double hasPaid;
    private String deadline;

    String status;

// Method section
// implement get() method for all
// implement set() method for due date and amount paid
    public Project() {

    }


    public int getProjectNum(){

        return projectNum;
    }

    public String getProjectName(){

        return projectName;
    }
    public String getBuildingType() {
        return buildingType;

    }
    public String getAddress(){

        return address;
    }

    public int getErfNum(){

        return erfNum;
    }

    public double getTotalFee() {

        return totalFee;
    }

    public double getHasPaid() {

        return hasPaid;
    }
    public String getDeadline(){
        return deadline;
    }
    public String getStatus(){
        return status;
    }

    public double setHasPaid(){
        return hasPaid;
    }
    public void setDeadline(String newDeadline){
        this.deadline = newDeadline;
    }
    public void setHasPaid(Double newHasPaid){
        this.hasPaid = newHasPaid;
    }
    public void setStatus(String newStatus){
        this.status = newStatus;
    }
// Constructor
    public Project(int projectNum, String projectName, String buildingType, String address, int erfNum, double totalFee, double hasPaid, String deadline, String status){
        this.projectNum = projectNum;
        this.projectName = projectName;
        this.buildingType = buildingType;
        this.address = address;
        this.erfNum = erfNum;
        this.totalFee = totalFee;
        this.hasPaid = hasPaid;
        this.deadline = deadline;
        this.status = this.status;

    }
// implement toString method

    public String toString(){
        String output = "Project Name: " + projectName;
        output += "\nProject number: " + projectNum;
        output += "\nBuilding Type : " + buildingType;
        output += "\nAddress:  " + address;
        output += "\nERF Number : " + erfNum;
        output += "\nTotal Project fee: " + totalFee;
        output += "\nAmount paid to date: " + hasPaid;
        output += "\nProject deadline: " + deadline;
        output += "\nProject Status: " + status;

        return output;
    }

}

// Architect class:


// Create class

public class Architect {

// Create 4 attributes

    String name;
    int telephoneNum;
    String email;
    String address;


//Methods:

    public String getName(){
        return name;
    }

    public int getTelephoneNum(){
        return telephoneNum;
    }

    public String getEmail(){
        return email;
    }

    public String getAddress(){
        return address;
    }


// Constructor

    public Architect(String name, int telephoneNum, String email, String address){

        this.name = name;
        this.telephoneNum = telephoneNum;
        this.email = email;
        this.address = address;

    }
// toString method

    public String toString(){

        String output = "Name: "+ name;
        output += "\nTelephone number: " + telephoneNum;
        output += "\nEmail Address: " + email;
        output += "\nPhysical Address: " + address;


        return output;
    }

}

// Contractor class:


// Create class

public class Contractor {

// Create 4 attributes

    String name;
    int telephoneNum;
    String email;
    String address;

    public Contractor() {

    }


//Methods:

    public String getName(){
        return name;
    }

    public int getTelephoneNum(){
        return telephoneNum;
    }

    public String getEmail(){
        return email;
    }

    public String getAddress(){
        return address;
    }

   public void setTelephoneNum(int newTelephoneNum){
        this.telephoneNum = newTelephoneNum;
   }
   public void setEmail(String newEmail){
        this.email = newEmail;
   }



// Constructor

    public Contractor(String name, int telephoneNum, String email, String address){

        this.name = name;
        this.telephoneNum = telephoneNum;
        this.email = email;
        this.address = address;

    }
// toString() methods

    public String toString(){

        String output = "Name: "+ name;
        output += "\nTelephone number: " + telephoneNum;
        output += "\nEmail Address: " + email;
        output += "\nPhysical Address: " + address;


        return output;
    }

}

// Customer class


// Create class

public class Customer {

// Create 4 attributes

    String name;
    int telephoneNum;
    String email;
    String address;


//Methods:

    public String getName(){
        return name;
    }

    public int getTelephoneNum(){
        return telephoneNum;
    }

    public String getEmail(){
        return email;
    }

    public String getAddress(){
        return address;
    }


// Constructor

    public Customer(String name, int telephoneNum, String email, String address){

        this.name = name;
        this.telephoneNum = telephoneNum;
        this.email = email;
        this.address = address;

    }
    
// toString() method 
    
    public String toString(){

        String output = "Name: "+ name;
        output += "\nTelephone number: " + telephoneNum;
        output += "\nEmail Address: " + email;
        output += "\nPhysical Address: " + address;


        return output;
    }

}

// Main METHOD

// This is the main method for the project management program

import java.util.Scanner;

// create class

public class poisedMain {

    public static void main(String[] args) {

// add a scanner and display choices to user

        Scanner selection = new Scanner(System.in);
        System.out.println("""
                Welcome to the Poised project management program. \s
                 Select an option:\s
                 A) To create a new Project.\s
                 B) To Update the due date of a project.\s
                 C) To update the total amount paid to date.
                 D) To update a contractors details
                 E) To finalise a project""");

        String opt = selection.nextLine();

// implement if and else if statements to check the user's answer
// Create a new project object based on user input

        if (opt.equalsIgnoreCase("A")) {

            System.out.println("""
                    You have chosen to create a new project.\s
                     Please enter the following:\s
                     Project Number:\s
                    Project Name:\s
                     Type of building:\s
                     Physical Address:\s
                     ERF number:\s
                     Total project fee:\s
                     Amount paid to date:\s
                    Project deadline:\s
                    Project Status: \s """);

            int projNum = selection.nextInt();
            String projName = selection.next();
            String buildType = selection.next();
            String address = selection.next();
            int erfNum = selection.nextInt();
            double total = Double.parseDouble(selection.next());
            double hasPaid = Double.parseDouble(selection.next());
            String deadline = selection.next();
            String status = selection.next();

            System.out.println(projName);
            System.out.println(projNum);
            System.out.println(buildType);
            System.out.println(address);
            System.out.println(erfNum);
            System.out.println(total);
            System.out.println(hasPaid);
            System.out.println(deadline);
            System.out.println(status);

            Project myObj = new Project(projNum, "projName", "buildType", "address", erfNum, total, hasPaid, "deadline", "status");

            System.out.println(myObj);


        }
        // change due date of a project
        else if (opt.equalsIgnoreCase("B")) {
            String deadlineSet = selection.next();
            System.out.println("Please enter the updated due date: ");
            Project update = new Project();
            update.setDeadline("deadlineSet");
            System.out.println(update.getDeadline());

        }
// change total fee paid up to date
        else if (opt.equalsIgnoreCase("C")) {
            Double newFee = selection.nextDouble();
            System.out.println("Please update the fee: ");
            Project updatedFee = new Project();
            updatedFee.setHasPaid(newFee);
            System.out.println(updatedFee.getDeadline());

        }
// Update contractors contact details

        else if (opt.equalsIgnoreCase("D")) {
            int newTel = selection.nextInt();
            String newMail = selection.next();
            System.out.println("Please enter a new Telephone number ad Email address");
            Contractor cell = new Contractor();
            cell.setTelephoneNum(newTel);
            Contractor mail = new Contractor();
            mail.setEmail("newMail");
            System.out.println(cell.getTelephoneNum());
            System.out.println(mail.getEmail());


        }
// Finalise the project

        else if (opt.equalsIgnoreCase("E")) {
            Project end = new Project();
            end.setStatus("FINALISED");
            System.out.println(end.getStatus());



        }

    }
}