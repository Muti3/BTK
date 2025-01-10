public abstract class Appliance implements Controllable {
    private boolean isOn;

    @Override
    public void turnOn() {
        isOn = true;
        System.out.println(getClass().getSimpleName() + " turned on.");
    }

    @Override
    public void turnOff() {
        isOn = false;
        System.out.println(getClass().getSimpleName() + " turned off.");
    }

    @Override
    public boolean isOn() {
        return isOn;
    }
}
