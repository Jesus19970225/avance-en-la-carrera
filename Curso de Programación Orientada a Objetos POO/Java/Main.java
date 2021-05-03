class Main {
    public static void main(String[] args) {
        System.out.println("Inicialixando...");
        UberX uberX = new UberX("AMQ123", new Account("Andrea Feran", "ANDA123", "andrea@hotmail.com", "12345"), "Chevrolet", "Sonic");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("FGH345", new Account("Andres Herrera", "AND123", "andres@hotmail.com", "12365"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();
        
        User user = new User("Andres Herrera", "AND123", "andres@hotmail.com", "12365");
        user.printDataUser();
    }

}