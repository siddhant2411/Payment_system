-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: ssip
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `mobile no.` int DEFAULT NULL,
  `amount` double NOT NULL,
  `payment_type` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `fk_payment_type_idx` (`payment_type`),
  CONSTRAINT `fk_payment_type` FOREIGN KEY (`payment_type`) REFERENCES `payment_method` (`payment_type`) ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,'2012-12-12 00:00:00',12,12,1),(2,'0001-01-01 00:00:00',123456789,12,2),(3,'0002-02-02 00:00:00',987654321,11,1),(4,'0003-03-03 00:00:00',321987654,15,2);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_id`
--

DROP TABLE IF EXISTS `order_id`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_id` (
  `number` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `quantity` double NOT NULL,
  `price_per_each` double NOT NULL,
  `unit` int NOT NULL,
  `total` double NOT NULL,
  PRIMARY KEY (`number`),
  KEY `fk_product_id_idx` (`product_id`),
  KEY `fk_unit_id_idx` (`unit`),
  CONSTRAINT `fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON UPDATE RESTRICT,
  CONSTRAINT `fk_unit_id` FOREIGN KEY (`unit`) REFERENCES `unit_identifire` (`unit_id`) ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_id`
--

LOCK TABLES `order_id` WRITE;
/*!40000 ALTER TABLE `order_id` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_id` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_method`
--

DROP TABLE IF EXISTS `payment_method`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_method` (
  `payment_type` int NOT NULL,
  `payment_name` varchar(45) NOT NULL,
  PRIMARY KEY (`payment_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_method`
--

LOCK TABLES `payment_method` WRITE;
/*!40000 ALTER TABLE `payment_method` DISABLE KEYS */;
INSERT INTO `payment_method` VALUES (1,'cash'),(2,'UPI');
/*!40000 ALTER TABLE `payment_method` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `price` double NOT NULL,
  `quantity` double NOT NULL,
  `unit` int NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `fk_unit_idx` (`unit`),
  CONSTRAINT `fk_unit` FOREIGN KEY (`unit`) REFERENCES `unit_identifire` (`unit_id`) ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (2,'rice',20,2,2),(3,'abc',30,3,1),(4,'bc',40,4,2),(5,'mc',30,5,1),(6,'xyz',20,4,1),(16,'xyz',20,4,1),(19,'xyz',20,4,1),(20,'xy',2,8,1),(21,'x',200,8,1),(22,'x',200,8,1),(23,'x',200,8,1);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unit_identifire`
--

DROP TABLE IF EXISTS `unit_identifire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unit_identifire` (
  `unit_id` int NOT NULL,
  `unit_name` varchar(45) NOT NULL,
  PRIMARY KEY (`unit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit_identifire`
--

LOCK TABLES `unit_identifire` WRITE;
/*!40000 ALTER TABLE `unit_identifire` DISABLE KEYS */;
INSERT INTO `unit_identifire` VALUES (1,'each'),(2,'kg');
/*!40000 ALTER TABLE `unit_identifire` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-11 10:20:35
