<?php
require_once('account.php')
class Car {
    public $id;
    public $license;
    public $driver;
    protected $passenger;

    public function _construct($license, $driver){
        $this->license = $license;
        $this->driver = $driver;
    }

    public function PrintDataCar(){
        echo "
        Licencia: $this->license 
        Driver: {$this->driver->name} 
        Número de pasajeros: $this->passenger
        
        ";
    }

    public function getPassenger(){
        return$this->passenger;
    }

    public function setPassenger($passenger){
        if ($passenger == 4) {
            $this->passenger = $passenger;
        }else {
            echo "Necesitas asignar 4 pasajeros";
        }
    }
}
?>