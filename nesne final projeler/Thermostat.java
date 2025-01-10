public class Thermostat extends Appliance {
    private double temperature;

    public void setTemperature(double temperature) {
        this.temperature = temperature;
        System.out.println("Temperature set to " + temperature + "°C.");
    }
}
