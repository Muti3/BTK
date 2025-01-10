import java.util.Scanner;

public class SmartHomeApp {
    public static void main(String[] args) {
        Light light = new Light();
        Thermostat thermostat = new Thermostat();
        SecuritySystem securitySystem = new SecuritySystem();

        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("Select an option:");
            System.out.println("1. Control Light");
            System.out.println("2. Control Thermostat");
            System.out.println("3. Control Security System");
            System.out.println("4. Exit");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("1. Turn On, 2. Turn Off, 3. Set Brightness");
                    int lightOption = scanner.nextInt();
                    if (lightOption == 1) light.turnOn();
                    else if (lightOption == 2) light.turnOff();
                    else if (lightOption == 3) {
                        System.out.println("Enter brightness (0-100):");
                        int brightness = scanner.nextInt();
                        light.setBrightness(brightness);
                    }
                    break;

                case 2:
                    System.out.println("1. Turn On, 2. Turn Off, 3. Set Temperature");
                    int thermoOption = scanner.nextInt();
                    if (thermoOption == 1) thermostat.turnOn();
                    else if (thermoOption == 2) thermostat.turnOff();
                    else if (thermoOption == 3) {
                        System.out.println("Enter temperature:");
                        double temp = scanner.nextDouble();
                        thermostat.setTemperature(temp);
                    }
                    break;

                case 3:
                    System.out.println("1. Turn On, 2. Turn Off, 3. Activate Alarm, 4. Deactivate Alarm");
                    int secOption = scanner.nextInt();
                    if (secOption == 1) securitySystem.turnOn();
                    else if (secOption == 2) securitySystem.turnOff();
                    else if (secOption == 3) securitySystem.activateAlarm();
                    else if (secOption == 4) securitySystem.deactivateAlarm();
                    break;

                case 4:
                    exit = true;
                    break;

                default:
                    System.out.println("Invalid option!");
            }
        }
        scanner.close();
    }
}
