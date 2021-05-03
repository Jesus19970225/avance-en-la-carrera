<?php

require_once('car.php');
require_once('uberX.php');
require_once('uberPool.php');
require_once('account.php');

$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolrt", "Spark");
$uberX->setPassenger(4);
$uberX->printDataCar();

$uberPool = new UberPool("TYU567", new Account("Andrea Ferran", "ANDA765"), "Dodge", "Attitude");
$uberPool->printDataCar();

$uberVan = new uberVan("OJL395", new Account("Raúl Ramirez", "AND456"), "Nissan", "Versa");
$uberVan->setPassenger(6);
$uberVan->printDataCar();
?>