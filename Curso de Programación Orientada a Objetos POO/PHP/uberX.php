<?php
require_once('car.php');
class UberX extends Car {
    public $brand;
    public $model;

    public function _construct($license, $driver, $brand, $model){
        parent::__construct($license, $driver);
        $this->licence =$license;
        $this->driver = $driver
        $this->brand = $brand;
        $this->model = $model;
    }

    public function PrintDataCar(){
        parent::PrintDataCar();
            echo"Modelo: $this->model Marca: $this->brand ";
    }

}
?>