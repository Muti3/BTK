public class Light extends Appliance {
    private int brightness; // 0-100 arası değer

    public void setBrightness(int brightness) {
        if (brightness < 0 || brightness > 100) {
            System.out.println("Brightness must be between 0 and 100.");
            return;
        }
        this.brightness = brightness;
        System.out.println("Brightness set to " + brightness + "%.");
    }
}
