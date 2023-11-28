-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: cardb
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin`
--

DROP TABLE IF EXISTS `Admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Admin` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `role` varchar(50) NOT NULL DEFAULT 'Admin',
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
INSERT INTO `Admin` VALUES (1,'rockposedon','87654321abc','Admin'),(2,'HarshYadav','GoutamiYadav','Admin'),(3,'AnilGehlot','anil@2303','Admin'),(4,'LokeshDangi','lokesh12345','Admin');
/*!40000 ALTER TABLE `Admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Car`
--

DROP TABLE IF EXISTS `Car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Car` (
  `CarID` int NOT NULL AUTO_INCREMENT,
  `VariantID` int DEFAULT NULL,
  `CategoryID` int DEFAULT NULL,
  `EngineID` int DEFAULT NULL,
  `ColorID` int DEFAULT NULL,
  `ModelID` int DEFAULT NULL,
  `VIN` varchar(17) DEFAULT NULL,
  `Mileage` float DEFAULT NULL,
  `YearOfManufacture` int DEFAULT NULL,
  `BrandCompany` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CarID`),
  UNIQUE KEY `VIN` (`VIN`),
  KEY `VariantID` (`VariantID`),
  KEY `CategoryID` (`CategoryID`),
  KEY `EngineID` (`EngineID`),
  KEY `ColorID` (`ColorID`),
  KEY `ModelID` (`ModelID`),
  CONSTRAINT `Car_ibfk_1` FOREIGN KEY (`VariantID`) REFERENCES `CarVariant` (`VariantID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Car_ibfk_2` FOREIGN KEY (`CategoryID`) REFERENCES `CarCategory` (`CategoryID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Car_ibfk_3` FOREIGN KEY (`EngineID`) REFERENCES `CarEngine` (`EngineID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Car_ibfk_4` FOREIGN KEY (`ColorID`) REFERENCES `CarColor` (`ColorID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Car_ibfk_5` FOREIGN KEY (`ModelID`) REFERENCES `CarModel` (`ModelID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Car`
--

LOCK TABLES `Car` WRITE;
/*!40000 ALTER TABLE `Car` DISABLE KEYS */;
INSERT INTO `Car` VALUES (1,1,1,3,3,7,'1938806887600475',22.53,2017,'Maruti Suzuki New'),(2,4,2,2,7,12,'7347179548259018',18.56,2014,'Maruti Suzuki'),(3,8,2,3,7,13,'6428304711133280',19.13,2017,'Maruti Suzuki'),(4,1,2,4,7,14,'5445957166442227',17.28,2015,'Maruti Suzuki'),(5,6,2,4,7,5,'7961931082323363',21.49,2018,'Maruti Suzuki'),(6,7,3,1,9,10,'1027969279671104',22.8,2017,'Maruti Suzuki'),(7,2,2,4,5,11,'3555548647476628',20.79,2014,'Maruti Suzuki'),(8,8,4,4,3,6,'2968110685490280',20.77,2016,'Maruti Suzuki'),(9,4,1,1,4,15,'5457533843842094',16.45,2023,'Maruti Suzuki'),(10,4,4,1,1,10,'2329004191377140',21.28,2019,'Maruti Suzuki'),(11,5,4,4,10,6,'7034468318558590',14.96,2018,'Maruti Suzuki'),(12,2,4,4,5,4,'9680689834992333',12.43,2021,'Maruti Suzuki'),(13,8,2,4,4,9,'6264460763415729',13.62,2022,'Maruti Suzuki'),(14,1,5,3,4,13,'8136348243025423',22.88,2020,'Maruti Suzuki'),(15,8,3,2,2,2,'3835895117032237',16.9,2022,'Maruti Suzuki'),(16,5,3,2,10,2,'4574520409110174',12.13,2021,'Maruti Suzuki'),(17,7,2,1,9,14,'3760991574917260',17.05,2017,'Maruti Suzuki'),(18,7,1,4,1,12,'4948179807893746',19.93,2023,'Maruti Suzuki'),(19,6,2,2,2,10,'9862488695001325',18.38,2015,'Maruti Suzuki'),(20,4,2,1,5,2,'4008202343546844',13.67,2014,'Maruti Suzuki'),(21,1,2,4,7,5,'9237720319743745',15.87,2021,'Maruti Suzuki'),(22,2,5,2,8,10,'6510328316537060',22.09,2023,'Maruti Suzuki'),(23,7,1,1,2,9,'4212218504905616',16.84,2022,'Maruti Suzuki'),(24,8,4,4,6,4,'8467099449406683',21.59,2020,'Maruti Suzuki'),(25,7,2,2,8,9,'4707662770922294',24.57,2017,'Maruti Suzuki'),(26,4,5,3,7,2,'2969247625239606',24.04,2018,'Maruti Suzuki'),(27,8,1,4,1,10,'8570849836356177',13.04,2017,'Maruti Suzuki'),(28,2,2,4,1,9,'5743335996497912',14.1,2017,'Maruti Suzuki'),(29,6,3,3,8,4,'9913417768797732',24.13,2015,'Maruti Suzuki'),(30,4,5,4,8,4,'1918073140431133',15.66,2019,'Maruti Suzuki'),(31,2,2,4,1,4,'5089343680535987',17.5,2023,'Maruti Suzuki'),(32,8,5,4,1,2,'5605677425758721',21,2014,'Maruti Suzuki'),(33,1,3,1,10,12,'5482093229550722',24.53,2019,'Maruti Suzuki'),(34,4,3,3,6,15,'3867022431022084',13.72,2015,'Maruti Suzuki'),(35,2,1,4,5,7,'2532039186383961',18.17,2019,'Maruti Suzuki'),(36,7,4,4,5,12,'9700709689626958',13.63,2015,'Maruti Suzuki'),(37,5,5,3,3,7,'3662050289045929',17.22,2018,'Maruti Suzuki'),(38,4,1,2,6,13,'2138847446639935',20.98,2016,'Maruti Suzuki'),(39,3,2,1,2,3,'7087986233666945',13.21,2017,'Maruti Suzuki'),(40,1,5,3,8,6,'6950685721132936',24.86,2021,'Maruti Suzuki'),(41,3,3,1,10,4,'5768805567262058',13,2022,'Maruti Suzuki'),(42,7,3,3,5,15,'9136643769946971',20.96,2018,'Maruti Suzuki'),(43,5,5,2,10,1,'9528405747911273',16.09,2019,'Maruti Suzuki'),(44,8,2,2,4,5,'1380834714463441',19.7,2017,'Maruti Suzuki'),(45,2,3,4,1,1,'6845830400836662',21.19,2017,'Maruti Suzuki'),(46,5,1,3,10,10,'7018278582507606',24,2021,'Maruti Suzuki'),(47,7,4,4,5,11,'7610819075057946',13.16,2020,'Maruti Suzuki'),(48,6,5,2,3,6,'8201510228503653',18.49,2018,'Maruti Suzuki'),(49,8,4,3,4,3,'5375122640871433',20.76,2014,'Maruti Suzuki'),(50,6,4,3,6,4,'2538345612774601',24,2014,'Maruti Suzuki'),(51,3,2,2,8,14,'6218258282602635',18.56,2019,'Maruti Suzuki'),(52,6,1,2,7,9,'2123583393268661',15.46,2018,'Maruti Suzuki'),(53,7,4,4,7,6,'4510442593980385',12.66,2020,'Maruti Suzuki'),(54,6,4,3,9,3,'5952556675331730',19.55,2021,'Maruti Suzuki'),(55,2,1,4,3,10,'6172510528558964',19.16,2014,'Maruti Suzuki'),(56,3,1,3,2,12,'5669276849352833',23.07,2023,'Maruti Suzuki'),(57,4,1,3,5,9,'2211573011283360',22.37,2017,'Maruti Suzuki'),(58,6,1,3,3,10,'3143498119013949',19.17,2022,'Maruti Suzuki'),(59,1,4,1,4,13,'3381426186522311',18.44,2023,'Maruti Suzuki'),(60,5,3,3,8,12,'2250745954055784',17.09,2015,'Maruti Suzuki'),(61,8,3,1,4,12,'5668001078192038',13.97,2017,'Maruti Suzuki'),(62,6,1,4,7,1,'1175986916767567',15.8,2016,'Maruti Suzuki'),(63,1,4,4,1,5,'6718073001100775',14.84,2017,'Maruti Suzuki'),(64,8,3,1,4,4,'7021601770322699',21.65,2016,'Maruti Suzuki'),(65,1,3,2,9,2,'9861483933000187',16.47,2023,'Maruti Suzuki'),(66,3,4,2,9,9,'7069861370944400',15.19,2015,'Maruti Suzuki'),(67,7,3,4,4,4,'1803720769923120',24.18,2014,'Maruti Suzuki'),(68,1,5,3,4,13,'3599468921028191',14.69,2020,'Maruti Suzuki'),(69,1,3,1,6,12,'9327537059286597',24.81,2015,'Maruti Suzuki'),(70,4,1,3,7,15,'9161291521784861',24.79,2017,'Maruti Suzuki'),(71,1,2,1,10,1,'1102689022420391',15.94,2018,'Maruti Suzuki'),(72,6,4,2,10,13,'8768045730466552',23.93,2023,'Maruti Suzuki'),(73,7,5,2,10,8,'9970051965885282',19.63,2016,'Maruti Suzuki'),(74,8,1,3,10,6,'7329124757801615',19.61,2015,'Maruti Suzuki'),(75,6,5,1,8,3,'2887304853398955',16.61,2017,'Maruti Suzuki'),(76,8,4,3,6,10,'2586618634194311',21.79,2021,'Maruti Suzuki'),(77,5,3,1,1,3,'7283368364979364',20.38,2019,'Maruti Suzuki'),(78,1,2,2,6,3,'3069473706288254',12.31,2015,'Maruti Suzuki'),(79,6,1,4,6,9,'9394102683572254',15.45,2019,'Maruti Suzuki'),(80,5,2,4,6,13,'1153053651178815',16.63,2014,'Maruti Suzuki'),(81,3,2,2,8,10,'7907919795859806',15.9,2016,'Maruti Suzuki'),(82,8,4,2,7,3,'7476584755040931',12.99,2016,'Maruti Suzuki'),(83,5,2,3,3,12,'8903816101199791',17.35,2021,'Maruti Suzuki'),(84,4,2,4,2,4,'5088258580759161',24.65,2020,'Maruti Suzuki'),(85,7,4,3,1,2,'9349889508461649',13.01,2021,'Maruti Suzuki'),(86,1,4,1,6,5,'6794354183188857',23.09,2020,'Maruti Suzuki'),(87,6,4,4,2,2,'3471933446066699',13.05,2023,'Maruti Suzuki'),(88,1,3,1,4,6,'9673365157535315',20.83,2016,'Maruti Suzuki'),(89,3,5,3,6,10,'2274699737408160',20.58,2022,'Maruti Suzuki'),(90,5,3,2,7,14,'5019076949852257',12.62,2019,'Maruti Suzuki'),(91,3,5,3,9,13,'7843068451232041',20.26,2019,'Maruti Suzuki'),(92,6,2,3,8,6,'7629105688197427',12.93,2022,'Maruti Suzuki'),(93,3,2,4,1,5,'9571692679004014',24.36,2023,'Maruti Suzuki'),(94,4,1,1,2,7,'5216851857227650',16.85,2016,'Maruti Suzuki'),(95,2,3,3,9,5,'5395204899393884',14.45,2016,'Maruti Suzuki'),(96,7,3,4,7,8,'6727967287438741',24.1,2017,'Maruti Suzuki'),(97,1,4,2,10,15,'5188464837487727',21.18,2019,'Maruti Suzuki'),(98,7,1,3,4,9,'6437763736760324',16.31,2020,'Maruti Suzuki'),(99,3,4,4,3,1,'4015970226405486',17.38,2017,'Maruti Suzuki'),(100,7,2,2,2,7,'1260083637573922',15.31,2014,'Maruti Suzuki');
/*!40000 ALTER TABLE `Car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CarCategory`
--

DROP TABLE IF EXISTS `CarCategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CarCategory` (
  `CategoryID` int NOT NULL AUTO_INCREMENT,
  `CategoryName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CategoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CarCategory`
--

LOCK TABLES `CarCategory` WRITE;
/*!40000 ALTER TABLE `CarCategory` DISABLE KEYS */;
INSERT INTO `CarCategory` VALUES (1,'SUV'),(2,'Sedan'),(3,'Hatchback'),(4,'Convertible'),(5,'Sport');
/*!40000 ALTER TABLE `CarCategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CarColor`
--

DROP TABLE IF EXISTS `CarColor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CarColor` (
  `ColorID` int NOT NULL AUTO_INCREMENT,
  `ColorName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ColorID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CarColor`
--

LOCK TABLES `CarColor` WRITE;
/*!40000 ALTER TABLE `CarColor` DISABLE KEYS */;
INSERT INTO `CarColor` VALUES (1,'White'),(2,'Black'),(3,'Silver'),(4,'Gray'),(5,'Red'),(6,'Blue'),(7,'Green'),(8,'Brown'),(9,'Yellow'),(10,'Orange');
/*!40000 ALTER TABLE `CarColor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CarEngine`
--

DROP TABLE IF EXISTS `CarEngine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CarEngine` (
  `EngineID` int NOT NULL AUTO_INCREMENT,
  `EngineName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`EngineID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CarEngine`
--

LOCK TABLES `CarEngine` WRITE;
/*!40000 ALTER TABLE `CarEngine` DISABLE KEYS */;
INSERT INTO `CarEngine` VALUES (1,'CNG'),(2,'Diesel'),(3,'Petrol'),(4,'Electric');
/*!40000 ALTER TABLE `CarEngine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CarModel`
--

DROP TABLE IF EXISTS `CarModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CarModel` (
  `ModelID` int NOT NULL AUTO_INCREMENT,
  `ModelName` varchar(100) DEFAULT NULL,
  `CategoryID` int DEFAULT NULL,
  `EngineID` int DEFAULT NULL,
  `ModelSpecifications` text,
  PRIMARY KEY (`ModelID`),
  KEY `CategoryID` (`CategoryID`),
  KEY `EngineID` (`EngineID`),
  CONSTRAINT `CarModel_ibfk_1` FOREIGN KEY (`CategoryID`) REFERENCES `CarCategory` (`CategoryID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `CarModel_ibfk_2` FOREIGN KEY (`EngineID`) REFERENCES `CarEngine` (`EngineID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CarModel`
--

LOCK TABLES `CarModel` WRITE;
/*!40000 ALTER TABLE `CarModel` DISABLE KEYS */;
INSERT INTO `CarModel` VALUES (1,'Alto K10',2,4,'President tell like fill free.'),(2,'Celerio',5,3,'They phone east what.'),(3,'Ignis',1,4,'Care worry certainly store authority idea east.'),(4,'Swift',1,3,'Ahead operation take smile according ok.'),(5,'Baleno',4,2,'Song effort everybody past or trip simply.'),(6,'Dzire',5,1,'Food single happen camera season about others.'),(7,'Ciaz',2,3,'Second thing class other big her.'),(8,'Ertiga',1,1,'Only force manage.'),(9,'XL6',1,4,'Try kid offer but institution avoid may say.'),(10,'Brezza',4,1,'Single change pattern past health accept.'),(11,'Grand Vitara',5,2,'Participant song after student best world.'),(12,'Fronx',1,4,'Back leg national couple institution.'),(13,'Jimny',1,3,'Set nature dog care everybody others.'),(14,'Alto 800',5,1,'Window clear join possible factor research carry.'),(15,'Wagon R',5,4,'Wear difficult himself nothing trouble develop foreign forward.'),(16,'S-Presso',2,4,'Nice mean leader appear manager per.');
/*!40000 ALTER TABLE `CarModel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CarVariant`
--

DROP TABLE IF EXISTS `CarVariant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CarVariant` (
  `VariantID` int NOT NULL AUTO_INCREMENT,
  `ModelID` int DEFAULT NULL,
  `ColorID` int DEFAULT NULL,
  `CategoryID` int DEFAULT NULL,
  `VariantName` varchar(100) DEFAULT NULL,
  `Mileage` float DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`VariantID`),
  KEY `ModelID` (`ModelID`),
  KEY `ColorID` (`ColorID`),
  KEY `CategoryID` (`CategoryID`),
  CONSTRAINT `CarVariant_ibfk_1` FOREIGN KEY (`ModelID`) REFERENCES `CarModel` (`ModelID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `CarVariant_ibfk_2` FOREIGN KEY (`ColorID`) REFERENCES `CarColor` (`ColorID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `CarVariant_ibfk_3` FOREIGN KEY (`CategoryID`) REFERENCES `CarCategory` (`CategoryID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CarVariant`
--

LOCK TABLES `CarVariant` WRITE;
/*!40000 ALTER TABLE `CarVariant` DISABLE KEYS */;
INSERT INTO `CarVariant` VALUES (1,2,10,5,'Sigma',36.6759,849718.96),(2,13,10,5,'Delta',29.1557,1218975.67),(3,12,4,5,'Delta AT',26.1517,934589.91),(4,8,9,4,'Zeta',21.3381,1693781.72),(5,15,7,1,'Zeta AT',22.2057,1146183.54),(6,16,2,1,'Alpha',30.3401,1077707.08),(7,14,8,3,'Alpha AT',22.5112,1787389.74),(8,8,1,2,'Zeta+',13.2806,1102188.22);
/*!40000 ALTER TABLE `CarVariant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `C_Name` varchar(50) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Address1` varchar(100) NOT NULL,
  `Address2` varchar(100) NOT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `PinCode` varchar(20) NOT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'Whitney Fox','Female','2000-11-11','928.371.853','matthew57@example.com','9716 Brian Pine Apt. 853','Apt. 798','North Thomas','Pennsylvania','30450'),(2,'Donald Young','Female','1991-11-03','628.983.693','wjohnson@example.org','208 Benjamin Mall','Suite 894','Frenchhaven','Nebraska','67023'),(3,'Brenda Duarte','Female','2004-01-21','610-457-746','kbush@example.com','3824 Jeffrey Village','Apt. 923','South Paige','South Dakota','00607'),(4,'Michael Crawford','Female','1961-09-21','+1-895-988-','nathanhoover@example.org','8169 Matthew Meadow Apt. 945','Suite 196','South Jessicachester','Georgia','70573'),(5,'Jessica Combs','Female','1996-05-25','(313)772-56','jillstrickland@example.org','9843 Allison Tunnel Apt. 873','Apt. 565','Robinsonfurt','Illinois','57762'),(6,'Michelle Carroll','Male','1998-06-23','+1-272-335-','rickygreen@example.com','238 Stacy Falls Suite 755','Apt. 452','Margaretview','Hawaii','82051'),(7,'Ann Kennedy','Male','1998-05-20','+1-467-966-','leslie38@example.net','0236 Jones Plains','Suite 937','Christyshire','Idaho','94005'),(8,'Andrew Lee','Male','1997-03-22','832.554.343','kevincannon@example.net','56940 Barton Key Apt. 262','Apt. 085','Garyland','New Mexico','79798'),(9,'Christine Garcia','Female','1993-05-20','001-818-433','igriffin@example.com','52465 Henry Canyon Apt. 254','Suite 765','Jameshaven','Massachusetts','63611'),(10,'Kelsey Washington','Male','1988-08-31','2396038622','cherylhaley@example.net','97343 Clark Valley Apt. 140','Apt. 574','Munoztown','New Hampshire','95592'),(11,'Shane Dalton','Female','1973-01-08','(577)278-46','john60@example.net','71044 Kimberly Wells','Suite 188','New Lanceburgh','West Virginia','13224'),(12,'Rachel Rhodes','Female','1977-07-08','(718)229-26','jamestaylor@example.net','59814 Collier Mews','Apt. 535','West Dakotaberg','Arizona','24665'),(13,'Rachel Choi','Female','1970-02-09','(906)936-29','orodriguez@example.org','24189 Sandra Skyway Apt. 457','Apt. 137','Hoffmanhaven','Alabama','66015'),(14,'Sherry Richardson','Male','2001-12-29','655.410.779','astewart@example.com','425 Neal Corner Apt. 972','Suite 076','Port Andrew','Idaho','50549'),(15,'Anthony Miranda','Female','1962-09-29','298-289-150','roberto93@example.net','266 Torres Inlet','Suite 056','South Aaronville','Connecticut','43327'),(16,'Corey Burns','Male','1971-12-22','(576)420-28','lisaholmes@example.net','0704 Pope Cape Suite 619','Apt. 044','Port Amandaborough','Oklahoma','93749'),(17,'David Morgan','Female','2000-12-05','719.880.437','christinejohnson@example.com','028 Perry Center Suite 306','Apt. 030','East Randyview','Georgia','64943'),(18,'Joseph Arnold','Male','1969-12-12','(722)426-08','kevinrichards@example.net','277 Mike Circles Apt. 009','Suite 288','Lake Robert','Massachusetts','54568'),(19,'Mary Escobar','Female','1991-08-31','(870)361-33','sullivanemily@example.com','6832 Barrera Roads Apt. 439','Suite 952','Shelleymouth','Kansas','03052'),(20,'Christina Costa','Male','1999-02-13','505-645-841','ipittman@example.net','306 Holland Rapid Apt. 465','Suite 593','Andreaview','Oklahoma','92084'),(21,'Michelle Baker','Female','2004-09-04','+1-983-822-','vazquezjuan@example.org','89572 Little Loaf','Apt. 873','Lake Jesse','New Hampshire','57300'),(22,'Daniel Campbell','Male','1960-04-28','603.253.836','brenda63@example.net','588 Hill Plaza','Suite 716','Mccarthyton','Texas','97249'),(23,'Martin Gonzales','Male','1981-08-14','(901)580-51','cbrooks@example.org','5802 Michael Fords Apt. 243','Suite 806','Fullershire','Rhode Island','08061'),(24,'Rodney Hall','Male','1988-06-29','8699250391','rogerssteven@example.com','3548 Cooke Bridge Suite 876','Apt. 475','West Gregoryside','Maryland','45523'),(25,'Katelyn Day','Female','1965-04-08','698.731.744','cynthia65@example.org','042 David Corners Apt. 497','Apt. 042','Calhounbury','Connecticut','40827'),(26,'Christy Pham','Female','2002-05-30','602-440-960','stephen77@example.com','01058 Howard Mews','Apt. 992','Brandonhaven','New Mexico','58854'),(27,'Sarah Roach','Male','1989-11-05','437-786-315','psutton@example.net','532 Oliver Summit Suite 433','Apt. 813','Lake Nicoleton','New Mexico','20675'),(28,'Paul Miller','Male','1988-02-23','534-434-256','smithgerald@example.net','004 Hill Forest Apt. 680','Apt. 043','Paulview','South Dakota','84807'),(29,'Michael James','Male','1993-06-15','241.456.124','brycebaker@example.com','33970 Rodriguez Bridge Suite 679','Apt. 612','Ramosmouth','Hawaii','08113'),(30,'Laura Patterson','Female','2002-09-18','(722)545-19','johnsonmarie@example.org','41634 Kristin Vista','Suite 472','Barneshaven','South Carolina','86590'),(31,'Natalie Gomez','Male','1982-07-04','712.484.252','joshua32@example.com','950 Williams Points Apt. 672','Suite 549','Olsonfurt','Montana','97909'),(32,'Edward Doyle','Female','2003-07-29','001-294-815','myerspatricia@example.com','57565 Sutton Orchard','Apt. 817','East Stevenstad','Nebraska','50627'),(33,'Steven Nichols','Male','1988-12-28','219.227.096','wking@example.com','17979 Singleton Flat','Apt. 152','Williamborough','Delaware','80060'),(34,'Kellie Bentley','Female','1988-10-19','467.789.918','bmcdowell@example.com','6051 Meadows Stream Suite 338','Suite 628','Port Julialand','Wyoming','57891'),(35,'Meredith Fowler','Male','1983-06-24','545-657-836','valerie31@example.org','4531 Clarke Courts Suite 458','Apt. 488','South Elizabeth','Kentucky','60671'),(36,'Laura Carroll','Female','1982-02-11','4817441826','christopherhenson@example.org','25876 Williams Overpass Apt. 538','Suite 187','East Russell','North Dakota','37963'),(37,'Brianna Obrien','Female','1988-02-09','001-486-268','eugene16@example.com','596 Lane Plaza Apt. 803','Suite 223','Sabrinahaven','Kentucky','87088'),(38,'Benjamin Baker','Female','1963-05-10','(224)847-37','whitekristin@example.net','18195 Richard Forest Suite 382','Suite 226','East Deborahburgh','Washington','94326'),(39,'Kevin Sandoval Jr.','Male','1992-06-04','933-700-647','chandleralisha@example.net','7790 Ann Crest Suite 850','Suite 885','Port Dennis','Oklahoma','26013'),(40,'Diana Cordova','Male','1968-06-19','+1-860-402-','kenneth69@example.com','590 Jackson Field Apt. 260','Suite 747','Campbellfurt','Texas','51380'),(41,'Martha Humphrey','Male','1995-03-08','217-846-640','imclaughlin@example.com','9537 Dustin Rapids','Apt. 409','South Danielle','Minnesota','34199'),(42,'Theodore Barnes','Female','1995-06-08','(931)407-42','vthompson@example.com','0509 Melissa Spur','Apt. 272','Lake Jennifershire','Massachusetts','15027'),(43,'Dawn Garcia','Female','2005-07-26','407.463.535','shepardjason@example.net','4533 Espinoza Roads Apt. 799','Apt. 193','East Sarahchester','Missouri','81406'),(44,'Steve Brown','Female','1974-05-16','621.478.525','marshmichael@example.org','494 Allen Inlet Suite 623','Suite 598','Williamsshire','Alabama','20679'),(45,'Terry Atkinson DDS','Female','1999-07-18','505-340-622','aaron38@example.net','9653 Tim Hill','Suite 086','Joseton','South Carolina','42078'),(46,'Emily Lopez','Male','2004-07-16','(314)545-11','bmartinez@example.org','4579 Mclaughlin Valleys Apt. 414','Suite 221','Gillhaven','Idaho','79973'),(47,'Kimberly Mclean','Male','1987-03-02','+1-465-289-','courtneyortiz@example.net','725 Huff Path','Suite 603','Powellburgh','Arizona','54711'),(48,'Elizabeth Smith','Female','1979-12-09','287.756.550','smithashley@example.org','03172 Marquez Squares','Apt. 321','Catherinebury','South Carolina','07244'),(49,'Jesse Hardy','Male','1972-02-02','(949)265-90','qmorton@example.net','8452 Stanley Villages Apt. 669','Suite 099','North Patrickchester','South Carolina','13790'),(50,'Anthony Jenkins','Male','1972-07-13','001-266-276','john80@example.org','1794 Lewis Ranch','Suite 466','East Kyle','Utah','71713');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Finance`
--

DROP TABLE IF EXISTS `Finance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Finance` (
  `FinanceID` int NOT NULL AUTO_INCREMENT,
  `SaleID` int DEFAULT NULL,
  `PaymentID` int DEFAULT NULL,
  `InstallmentID` int DEFAULT NULL,
  `FinancingTerm` int DEFAULT NULL,
  `InterestRate` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`FinanceID`),
  KEY `SaleID` (`SaleID`),
  KEY `PaymentID` (`PaymentID`),
  KEY `InstallmentID` (`InstallmentID`),
  CONSTRAINT `Finance_ibfk_1` FOREIGN KEY (`SaleID`) REFERENCES `Sale` (`SaleID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Finance_ibfk_2` FOREIGN KEY (`PaymentID`) REFERENCES `Payment` (`PaymentID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Finance_ibfk_3` FOREIGN KEY (`InstallmentID`) REFERENCES `Installment` (`InstallmentID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Finance`
--

LOCK TABLES `Finance` WRITE;
/*!40000 ALTER TABLE `Finance` DISABLE KEYS */;
INSERT INTO `Finance` VALUES (1,55,81,54,46,0.70),(2,74,54,52,52,3.40),(3,8,38,41,46,3.90),(4,51,39,62,26,0.40),(5,57,46,94,38,0.20),(6,56,80,7,19,6.00),(7,84,98,94,28,4.70),(8,54,46,27,61,0.90),(9,1,100,18,68,4.70),(10,71,6,87,19,6.40),(11,12,53,3,53,3.80),(12,71,5,12,55,4.00),(13,78,79,26,46,4.00),(14,35,74,22,71,6.90),(15,79,31,17,19,5.40),(16,69,25,26,50,1.00),(17,44,89,19,48,8.60),(18,11,31,32,70,7.50),(19,68,62,24,28,7.50),(20,78,45,84,21,9.40),(21,5,4,68,36,3.90),(22,1,25,24,22,3.60),(23,68,37,83,62,5.00),(24,94,10,71,46,7.60),(25,27,16,72,36,0.90),(26,75,96,47,68,2.80),(27,88,52,38,29,1.90),(28,53,31,25,63,5.40),(29,1,48,84,69,4.30),(30,48,28,34,36,6.40),(31,70,63,33,34,5.50),(32,41,21,78,63,4.20),(33,92,17,30,68,1.10),(34,94,54,25,60,2.30),(35,72,84,7,13,3.60),(36,44,59,70,22,8.90),(37,73,62,98,16,3.10),(38,10,21,74,16,1.40),(39,56,50,72,63,3.60),(40,89,3,57,40,3.80),(41,18,9,28,39,6.30),(42,48,44,64,55,7.90),(43,16,38,71,20,7.20),(44,41,7,65,59,8.50),(45,89,75,84,18,0.70),(46,6,91,35,24,6.70),(47,42,43,17,29,6.00),(48,26,52,65,43,2.40),(49,20,43,68,42,3.30),(50,12,20,30,13,0.90),(51,73,29,50,41,7.70),(52,30,30,84,56,2.10),(53,85,41,59,22,1.80),(54,50,45,17,64,7.80),(55,5,31,47,32,7.80),(56,61,23,56,53,8.40),(57,89,61,92,34,2.30),(58,41,54,72,60,7.70),(59,45,100,12,27,5.30),(60,4,6,21,54,8.80),(61,4,66,10,55,1.30),(62,76,70,28,16,6.70),(63,45,8,71,44,3.80),(64,28,43,21,20,5.20),(65,46,87,63,56,8.60),(66,22,4,89,50,9.90),(67,95,12,75,40,8.40),(68,12,93,30,27,9.70),(69,84,22,56,27,9.50),(70,22,63,11,42,3.50),(71,40,67,94,51,0.10),(72,68,94,97,72,9.60),(73,31,84,92,44,7.10),(74,1,94,55,50,2.40),(75,67,54,95,21,6.70),(76,84,78,67,56,7.20),(77,99,50,7,19,6.40),(78,37,79,88,56,0.90),(79,3,43,39,47,9.20),(80,79,84,66,30,7.10),(81,92,31,35,58,0.40),(82,38,29,31,15,5.30),(83,95,15,86,46,7.00),(84,53,79,87,29,8.40),(85,98,9,16,66,0.50),(86,59,1,66,21,5.50),(87,43,29,58,43,2.50),(88,30,5,3,21,2.60),(89,75,90,28,14,0.30),(90,98,67,65,30,0.90),(91,74,76,79,17,3.90),(92,74,28,26,41,3.10),(93,58,33,75,67,2.40),(94,86,86,25,26,9.30),(95,1,23,39,64,6.80),(96,33,49,2,55,8.60),(97,16,74,38,22,2.60),(98,95,7,61,36,1.40),(99,96,97,74,37,6.40);
/*!40000 ALTER TABLE `Finance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Installment`
--

DROP TABLE IF EXISTS `Installment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Installment` (
  `InstallmentID` int NOT NULL AUTO_INCREMENT,
  `InstallmentNumber` int DEFAULT NULL,
  `DueDate` date DEFAULT NULL,
  `InstallmentAmount` int DEFAULT NULL,
  `RemainingAmount` int DEFAULT NULL,
  `TotalInstallment` int DEFAULT NULL,
  PRIMARY KEY (`InstallmentID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Installment`
--

LOCK TABLES `Installment` WRITE;
/*!40000 ALTER TABLE `Installment` DISABLE KEYS */;
INSERT INTO `Installment` VALUES (1,7,'2024-04-12',15533,379699,33),(2,7,'2024-07-10',16080,795036,33),(3,2,'2024-01-04',24687,586497,47),(4,1,'2024-05-07',25030,711514,19),(5,4,'2024-01-02',23676,1173763,54),(6,8,'2024-07-24',19598,368653,36),(7,12,'2024-04-04',43193,1176411,21),(8,6,'2024-05-19',17246,1092504,16),(9,8,'2024-08-24',44837,1046410,31),(10,6,'2023-11-28',22835,1110695,13),(11,10,'2024-06-20',34486,729191,18),(12,2,'2024-04-19',47346,916072,15),(13,3,'2024-04-10',49377,666886,51),(14,2,'2024-02-18',23184,1029584,36),(15,7,'2024-06-09',48570,368247,54),(16,6,'2024-05-28',23486,907857,28),(17,11,'2023-12-03',22962,907588,56),(18,12,'2024-03-07',37021,360651,22),(19,4,'2024-01-14',26813,394292,16),(20,2,'2024-06-05',26501,741586,35),(21,10,'2024-08-26',20565,496752,36),(22,7,'2024-10-17',49011,723979,37),(23,2,'2024-06-27',15483,861611,26),(24,9,'2024-05-29',30431,489185,43),(25,5,'2024-08-26',41568,325449,57),(26,4,'2024-05-21',36068,394658,12),(27,9,'2024-03-21',20437,746892,53),(28,10,'2024-07-13',17810,536567,55),(29,7,'2023-11-11',23195,899447,21),(30,1,'2024-07-12',34954,518299,57),(31,2,'2024-07-08',35158,556127,38),(32,12,'2023-10-30',22274,1071846,25),(33,9,'2024-05-26',22411,1096274,41),(34,10,'2024-05-26',49668,447304,19),(35,2,'2024-10-10',25801,344795,16),(36,5,'2024-06-05',38942,1034771,50),(37,7,'2023-12-07',20907,1085219,59),(38,1,'2024-09-09',35122,1177795,52),(39,5,'2024-10-23',21100,545609,42),(40,2,'2024-08-24',28799,326262,57),(41,2,'2024-06-26',45860,640160,46),(42,10,'2024-03-20',30954,724969,55),(43,3,'2023-11-16',40028,1006473,24),(44,7,'2024-06-27',37696,357366,22),(45,1,'2024-02-05',37232,415396,57),(46,10,'2024-05-06',35344,1149189,29),(47,4,'2024-04-04',41908,827980,32),(48,5,'2023-11-25',20214,931889,37),(49,7,'2024-08-07',17090,1115425,59),(50,10,'2024-04-27',47428,391552,55),(51,9,'2024-01-26',47809,832554,37),(52,3,'2024-10-08',30334,643484,20),(53,12,'2023-12-25',21829,431393,14),(54,10,'2024-01-20',43400,1174651,40),(55,1,'2023-11-12',31055,333044,12),(56,4,'2024-05-20',41480,530012,53),(57,8,'2024-10-12',49462,505709,12),(58,1,'2024-10-12',21402,375336,12),(59,3,'2024-10-01',15286,704073,25),(60,10,'2024-09-21',31310,356735,47),(61,12,'2024-04-16',48085,627588,36),(62,4,'2024-01-22',22858,971486,12),(63,4,'2024-03-07',40707,1098451,30),(64,10,'2023-12-23',19629,926017,42),(65,4,'2024-05-03',24740,1140209,20),(66,1,'2024-03-18',38979,1127055,54),(67,4,'2024-10-22',33112,1008444,24),(68,5,'2024-06-23',34807,586147,22),(69,11,'2024-06-22',34076,671262,42),(70,5,'2024-06-09',30387,1001906,22),(71,7,'2024-04-08',37543,634669,16),(72,7,'2024-08-14',20906,895642,45),(73,4,'2024-07-21',20796,1133067,28),(74,11,'2024-08-03',33667,337057,32),(75,4,'2024-10-05',33450,602799,16),(76,8,'2024-05-09',15785,307710,15),(77,3,'2024-01-14',42915,331099,20),(78,8,'2024-03-13',46304,765866,50),(79,10,'2024-07-26',30201,313120,28),(80,9,'2024-06-22',19826,1084417,36),(81,4,'2024-02-20',21886,347313,31),(82,9,'2024-07-15',42658,303432,56),(83,10,'2024-03-25',17537,663639,15),(84,1,'2024-06-15',35185,1175085,39),(85,7,'2024-03-05',31700,816445,12),(86,7,'2024-07-02',25998,795746,55),(87,5,'2023-12-09',17329,629700,37),(88,9,'2023-12-21',40591,805535,36),(89,10,'2024-06-09',47090,500417,34),(90,10,'2023-11-27',25806,1183274,54),(91,9,'2024-04-26',37923,434100,31),(92,5,'2024-01-31',46050,929275,30),(93,6,'2024-04-07',21060,963913,54),(94,7,'2024-03-03',25874,1170315,29),(95,7,'2024-03-31',28247,926608,26),(96,9,'2023-11-21',32828,986535,48),(97,8,'2024-03-17',36838,500050,50),(98,8,'2024-10-07',42472,683202,31),(99,9,'2024-04-24',49785,917337,53),(100,8,'2023-12-13',48078,340264,26);
/*!40000 ALTER TABLE `Installment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Payment`
--

DROP TABLE IF EXISTS `Payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Payment` (
  `PaymentID` int NOT NULL AUTO_INCREMENT,
  `InstallmentID` int DEFAULT NULL,
  `PaymentAmount` int DEFAULT NULL,
  `PaymentDate` date DEFAULT NULL,
  `PaymentMethod` varchar(50) DEFAULT NULL,
  `TransactionID` varchar(100) DEFAULT NULL,
  `PaymentDue` date DEFAULT NULL,
  `DownPayment` int DEFAULT NULL,
  PRIMARY KEY (`PaymentID`),
  KEY `InstallmentID` (`InstallmentID`),
  CONSTRAINT `Payment_ibfk_1` FOREIGN KEY (`InstallmentID`) REFERENCES `Installment` (`InstallmentID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Payment`
--

LOCK TABLES `Payment` WRITE;
/*!40000 ALTER TABLE `Payment` DISABLE KEYS */;
INSERT INTO `Payment` VALUES (1,89,1829007,'2024-01-01','Cash','758b663a-c160-4ea2-a109-45f7be5e700a','2024-10-16',490915),(2,30,997394,'2024-07-05','Credit Card','0e601281-3efc-457c-9add-c4bf55c61f40','2024-06-28',240615),(3,19,1487543,'2024-06-06','Debit Card','65aac03e-ca82-4f2e-b04d-3efe21ee2c56','2024-08-19',138543),(4,46,565982,'2024-08-11','Cash','a9dd8278-afea-4a05-be58-f082c0b58632','2024-06-05',182082),(5,62,1886706,'2024-08-08','Debit Card','2e052c06-1583-4dd7-8198-3eff4c8f9193','2023-11-30',274948),(6,71,1642141,'2024-07-17','Cash','39abf86c-4b54-4b49-9485-668aeeb70669','2024-10-17',72882),(7,66,979677,'2023-11-19','Debit Card','c21a32f4-edc0-4477-9bcd-d8d4e8245974','2023-10-27',263933),(8,31,1077515,'2024-10-07','Credit Card','a63e4e10-3001-45ee-8ae4-e5f7cb87eab5','2023-11-06',468925),(9,11,1011594,'2024-08-06','Credit Card','46efd264-8a44-40d0-9c43-1d4ac00749a6','2024-09-19',386725),(10,86,1400982,'2024-02-15','Credit Card','5ba0c3c9-39b0-46d6-bc77-21d604151b1d','2024-04-15',251379),(11,43,1413998,'2024-02-14','Cash','1713eb16-37a7-4e25-8c77-e106cc8b3ca3','2024-01-14',256901),(12,67,1746118,'2024-01-17','Debit Card','f567e99d-f289-4ee2-afcd-25aa635e7f5a','2024-04-23',105225),(13,7,1102267,'2024-03-19','Debit Card','f8915b9a-f9d4-4874-9e54-81a200c668ab','2024-07-28',109711),(14,6,697524,'2023-12-28','Debit Card','66bb2002-5130-4798-9bc0-51f6231b81cf','2024-06-21',323069),(15,50,1641530,'2024-10-13','Cash','118490ff-36c9-41ba-90e3-1f4ef60cef00','2024-09-16',176520),(16,33,1980480,'2023-12-23','Credit Card','cde4a2cb-eb40-414c-9bd0-b6e38b7160af','2023-11-20',494166),(17,70,2080542,'2024-03-15','Cash','a801d538-abd6-433d-a4e8-26a0ce7b8a36','2024-09-07',444541),(18,61,845060,'2023-11-17','Debit Card','b9ac8c02-2f7c-425d-bab1-e3e60fe952a6','2024-08-16',351146),(19,69,2098663,'2024-03-27','Cash','eb1fe3ee-833c-480e-9f9c-69923f69d30d','2024-09-03',234991),(20,5,807269,'2023-12-13','Cash','e78abf4d-1e02-494c-bd1c-bde1f0eb7d3a','2023-11-18',401030),(21,92,1693808,'2024-09-16','Debit Card','8d06f902-21de-4393-989f-bac0b4078ca8','2024-07-02',466987),(22,35,554434,'2024-09-04','Debit Card','d0e75ac0-f8c8-41f0-ac7a-f56daf62cae8','2024-01-22',383712),(23,17,2034034,'2024-01-11','Cash','77a66ef2-5aaf-4815-9c76-40f71cdf4eef','2023-11-02',162838),(24,74,1893860,'2024-07-11','Debit Card','cc70c8db-6522-4236-8467-426db47f5908','2024-05-21',115606),(25,26,1512523,'2024-09-16','Debit Card','b7b6de15-9fd2-4ba2-9454-b1f15f28894e','2024-09-15',499275),(26,49,511107,'2024-04-25','Debit Card','ebbf9150-c01c-43ce-9dbe-b9adfb88fcba','2024-05-22',364604),(27,83,1411801,'2024-05-31','Debit Card','f73e919c-914f-49d5-913e-7b48fb5a540f','2023-12-12',206886),(28,96,681118,'2024-07-13','Credit Card','2b9c51d8-1295-479c-80a4-bd763cf3e687','2024-03-31',65592),(29,10,1467779,'2024-03-10','Credit Card','d9b4ca01-33ed-4dd5-957f-3f4d7ae18573','2024-08-17',257897),(30,41,1748647,'2024-02-12','Debit Card','2d3a4bc0-06b1-4a60-a6af-b4aeec07f334','2024-09-11',454540),(31,91,674406,'2024-05-29','Debit Card','df3f5ddf-e2b2-4375-bc6f-9483bc4fcdf4','2024-08-21',61168),(32,99,770831,'2023-12-17','Credit Card','13f78f6b-bd64-40b5-a4e5-f277d5023790','2024-09-08',470668),(33,58,1646037,'2024-01-16','Credit Card','8fa5e98f-39a4-423a-953b-5fcaec3bcf2c','2024-07-24',483344),(34,80,1608986,'2023-12-08','Cash','d6502a5a-8e67-4f0d-a72b-c29532cef98e','2024-03-01',484466),(35,49,1034900,'2024-06-27','Debit Card','e70d5a70-f8ea-4485-8061-c2007a2dee87','2023-11-07',216473),(36,37,1388127,'2024-08-19','Cash','35ce28bf-8994-42bd-be8f-e3899335ad26','2023-11-20',65487),(37,17,1160248,'2024-08-09','Credit Card','94fae6d0-b242-4f01-973c-94b49938848d','2024-09-26',106655),(38,71,804480,'2024-05-12','Credit Card','26362772-9180-4edb-8d6a-339202446c31','2023-11-16',72062),(39,83,803835,'2024-01-20','Credit Card','8c0d614c-6236-47a8-b046-f3535fe32934','2024-06-25',295538),(40,62,898290,'2023-12-12','Debit Card','49985362-2620-4c55-a76c-57b832173e7d','2024-07-19',302431),(41,14,1737930,'2024-05-17','Cash','24978444-165f-4407-a53e-0bdc4c8b2090','2024-07-11',375342),(42,18,1008433,'2024-08-17','Debit Card','87f16cdf-86fd-45d1-8778-49cf5bebde71','2024-03-13',288220),(43,45,1159039,'2024-09-06','Cash','5d942a4c-625f-4d2c-bd51-abb517316d94','2024-01-25',232361),(44,81,677758,'2024-07-15','Debit Card','aedf4ce7-37d0-4e84-a919-e3e793a34ac6','2024-01-27',486757),(45,86,2014274,'2023-12-23','Cash','e9f10a1f-a6ce-4aea-8591-77c241f46f53','2024-03-16',329718),(46,100,1951423,'2024-06-13','Debit Card','e9c773e8-f0df-46e7-8384-65831c189d77','2023-11-02',474240),(47,71,1472332,'2024-06-14','Cash','b3c53c2e-30c7-47a5-817f-629f7edbfc8b','2024-01-23',286295),(48,86,1637522,'2024-06-22','Credit Card','1eb762fc-ed6a-49d0-8c64-b9557cb43c8d','2024-10-20',394740),(49,68,993532,'2024-03-13','Debit Card','0c5355a1-56f5-42a2-9027-a9a1f77d7054','2024-01-03',432701),(50,50,1529699,'2024-04-17','Credit Card','8c4061a0-6ec4-46d6-ad07-b5adade1d1f2','2023-12-22',318827),(51,65,1910164,'2024-10-11','Debit Card','6611fbf1-eea2-4f16-948a-af7962e57f15','2024-08-16',152040),(52,90,1273909,'2023-12-29','Cash','3c653405-1196-40df-bf7c-d4d94cc1301f','2024-02-21',331326),(53,50,1996075,'2024-05-15','Credit Card','ee042926-0305-42b9-98ed-95863ea437ef','2024-07-26',305834),(54,65,1802203,'2024-01-10','Credit Card','363495fe-a51b-45e3-9f02-44c34f8bfcf7','2024-01-09',142374),(55,40,807899,'2024-03-06','Debit Card','1d45612c-c638-4402-812a-2450ae29c46e','2024-03-02',342416),(56,61,976735,'2024-01-27','Cash','9c44f921-8060-4ae5-8c7d-dedc5a564448','2024-04-18',272410),(57,18,1118757,'2024-01-02','Debit Card','f8d2e901-df94-44b2-98ca-17cc2572a36e','2024-05-18',149450),(58,8,814447,'2024-08-23','Credit Card','1357fec4-4307-476e-aa58-2f3ffb268616','2024-02-18',69348),(59,75,706125,'2023-12-30','Credit Card','09b2e56f-5eb5-4e64-8deb-457e0498ab97','2024-07-26',195203),(60,97,1481001,'2024-04-12','Debit Card','1d247202-cc43-44ce-9ee5-5508126af827','2024-06-12',364206),(61,50,734260,'2023-11-04','Credit Card','c88821d9-bf24-4d4f-81d2-77a17f15ed19','2024-09-10',107877),(62,77,1418873,'2024-05-01','Credit Card','c849dfd0-5aaa-4faf-a977-810be0cca11c','2024-05-13',90078),(63,39,867202,'2024-03-11','Debit Card','b7b9add0-319d-497b-8aa5-e75b4fb65f5b','2024-03-07',466490),(64,29,1328347,'2024-06-15','Credit Card','a61a8fce-7408-467b-a0e5-8d364dc4b488','2024-02-03',283965),(65,87,1338851,'2024-08-06','Cash','78dbac06-7f56-4698-8a7e-655d4f3012fb','2023-12-16',414751),(66,30,1674883,'2024-01-07','Credit Card','2c2c80f1-274e-4b60-ab43-7a9c6d74b17a','2024-10-07',261015),(67,30,821268,'2023-12-17','Cash','20987d0c-4527-4572-909a-e04be42c5eeb','2024-03-12',142334),(68,83,1472800,'2024-05-31','Cash','0a102781-a661-4393-b572-348c9a2e1235','2024-02-28',105065),(69,60,1116063,'2024-10-05','Credit Card','dfba8d7d-710e-47b2-a36b-7255d2a02cce','2024-05-30',490725),(70,98,1021684,'2024-03-31','Cash','9477dac2-80e8-4a8f-91f0-2ef3b4d6063f','2024-09-03',395900),(71,16,1639559,'2024-03-06','Cash','fcd81da2-e633-4b4f-a905-ae80e764881f','2023-11-23',420100),(72,10,869326,'2023-10-31','Debit Card','8dcbe0e6-10d9-4b67-bb8c-f0755ae88cd3','2024-02-16',131180),(73,10,846312,'2024-08-07','Debit Card','68b46ff7-0fa5-4824-9cd8-4eb1e986ecd2','2024-01-26',72880),(74,49,1680892,'2024-07-19','Debit Card','4d3b5dd2-34d5-456c-ae80-abab4cd341ec','2023-12-21',437427),(75,20,896095,'2024-01-09','Credit Card','8285e3c7-d826-4b66-9d8a-16ae8dba8b0c','2024-02-25',422102),(76,63,1458511,'2024-03-27','Credit Card','e507a383-10c3-4c2a-bfba-cedca9a22b3c','2024-01-30',342257),(77,60,1876753,'2024-07-12','Credit Card','acc2c208-24a6-4335-ae05-73c134b92eca','2024-04-25',97088),(78,65,765739,'2024-01-30','Debit Card','a54c1f19-6a62-4098-bba1-53a20d6f268c','2024-06-10',181626),(79,16,958912,'2024-06-24','Debit Card','707e9ad1-5e80-42cc-be9f-db5ba3137210','2024-09-10',483126),(80,47,1720453,'2023-11-19','Cash','3ee2f802-7c24-41f1-beb5-7cdf16727996','2024-03-10',435799),(81,72,628198,'2024-08-01','Cash','a1931ab3-5043-48ca-b8b0-756318be31ad','2024-02-02',112669),(82,4,1812713,'2024-04-08','Cash','72c2f44e-a7fc-4463-9b80-e3b7738f1e89','2024-04-17',187120),(83,30,729676,'2023-11-11','Cash','bb4b7ab6-d07d-4db8-b281-b8c0e1ecc4ee','2024-09-23',221586),(84,67,785128,'2024-01-16','Debit Card','fb05470f-eaa1-4854-9959-24f825ecb5c0','2024-01-13',311903),(85,40,1928854,'2023-12-02','Debit Card','7b8fbf2e-8c2f-4d41-bbed-c04e8a3f9638','2024-07-20',293436),(86,84,2094955,'2023-12-03','Cash','63267de4-e525-436b-b6fd-0a0ebe4ddc60','2024-07-05',315653),(87,54,538751,'2024-06-14','Cash','3bcdbf8c-bb32-4dfe-b7ac-f07c2ab06fa5','2023-12-12',152061),(88,84,1812426,'2024-04-01','Credit Card','6ba7e6da-17a7-42b1-b1d5-d713ceb68153','2024-10-18',355939),(89,25,1001036,'2024-01-13','Debit Card','425bc4cc-b346-447f-adf4-bd9597f97fee','2024-07-13',488408),(90,39,1922540,'2024-07-07','Debit Card','df92c81b-2abe-4a2b-9cd2-e295fa10daef','2024-07-31',188732),(91,31,1300898,'2024-09-26','Debit Card','55803792-0056-4a83-9cbc-de67f43041d9','2023-12-19',159888),(92,82,2059788,'2024-02-01','Cash','7d747bb1-0f05-4169-b573-9ae522d54323','2023-12-25',235423),(93,50,1707713,'2023-11-07','Cash','d2475ae0-dd6a-477a-962b-3f18646c91ec','2024-07-05',297789),(94,39,1425613,'2024-05-02','Cash','5517bfb8-9544-471b-9ccf-7f3687d27ade','2024-06-18',268324),(95,19,1871928,'2024-07-18','Cash','054d5fd1-bc61-4e20-be7c-02cc0ef64866','2024-07-26',61815),(96,93,1738284,'2024-08-23','Cash','03f2170d-053b-4ed7-86e2-6e58dceee908','2024-04-05',480653),(97,71,1797522,'2024-07-07','Credit Card','939749af-239a-44d5-94f3-b70b418156ea','2024-08-07',276039),(98,92,1336904,'2023-12-22','Cash','252c09b5-e465-4556-9cf7-94c13acae3c6','2024-05-01',307094),(99,83,886163,'2024-10-03','Cash','44a2f71e-24b7-42ab-aa05-38f4ca6865a0','2024-01-20',150514),(100,5,1572912,'2024-10-02','Debit Card','895e90b0-4163-40aa-bb43-945cd43e326a','2024-03-25',299960);
/*!40000 ALTER TABLE `Payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sale`
--

DROP TABLE IF EXISTS `Sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sale` (
  `SaleID` int NOT NULL AUTO_INCREMENT,
  `CustomerID` int DEFAULT NULL,
  `CarID` int DEFAULT NULL,
  `SalespersonID` int DEFAULT NULL,
  `PaymentID` int DEFAULT NULL,
  `SaleDate` date DEFAULT NULL,
  `SalePrice` int DEFAULT NULL,
  PRIMARY KEY (`SaleID`),
  KEY `CustomerID` (`CustomerID`),
  KEY `CarID` (`CarID`),
  KEY `SalespersonID` (`SalespersonID`),
  KEY `PaymentID` (`PaymentID`),
  CONSTRAINT `Sale_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `Customer` (`CustomerID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Sale_ibfk_2` FOREIGN KEY (`CarID`) REFERENCES `Car` (`CarID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Sale_ibfk_3` FOREIGN KEY (`SalespersonID`) REFERENCES `SalesPerson` (`SalesPersonID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Sale_ibfk_4` FOREIGN KEY (`PaymentID`) REFERENCES `Payment` (`PaymentID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sale`
--

LOCK TABLES `Sale` WRITE;
/*!40000 ALTER TABLE `Sale` DISABLE KEYS */;
INSERT INTO `Sale` VALUES (1,30,91,1,57,'2024-06-21',1468022),(2,19,14,4,47,'2024-04-14',1945170),(3,47,85,15,33,'2024-03-15',1869022),(4,23,94,12,10,'2023-12-08',1158377),(5,23,55,4,33,'2023-12-04',1198415),(6,33,17,6,20,'2024-06-19',1948842),(7,21,31,5,82,'2024-06-14',809415),(8,17,29,3,35,'2024-03-24',513448),(9,6,75,18,11,'2023-12-03',1050205),(10,21,54,2,93,'2024-03-26',664519),(11,47,48,7,52,'2024-08-14',1057254),(12,32,69,14,16,'2023-11-04',1327480),(13,39,79,14,41,'2023-12-28',853167),(14,50,49,11,14,'2024-08-06',1901971),(15,8,49,10,61,'2024-03-02',1089510),(16,39,76,16,88,'2024-06-10',990071),(17,19,83,7,46,'2024-08-13',1325497),(18,5,96,10,19,'2024-06-17',1268745),(19,11,16,6,59,'2024-01-29',1970871),(20,46,3,12,61,'2024-10-15',1599341),(21,22,65,16,72,'2024-07-04',1877627),(22,34,94,4,17,'2024-10-09',1678830),(23,8,13,4,83,'2024-10-22',1401442),(24,40,52,6,99,'2023-12-29',547604),(25,16,37,19,9,'2024-01-08',1448470),(26,45,83,6,22,'2024-06-28',1545280),(27,6,61,18,27,'2024-08-09',557754),(28,18,39,4,87,'2024-04-27',1210125),(29,24,76,16,41,'2024-05-03',1906892),(30,27,91,14,29,'2024-01-01',1214429),(31,50,76,3,40,'2024-09-30',1690300),(32,8,54,7,42,'2024-06-09',1773775),(33,5,68,8,39,'2023-12-31',1931746),(34,19,8,16,85,'2024-04-28',933949),(35,42,8,11,34,'2024-03-23',1780560),(36,17,67,6,57,'2024-07-03',1903720),(37,5,78,6,90,'2024-10-19',904239),(38,16,83,4,19,'2024-09-04',1674363),(39,1,77,8,72,'2023-11-25',1447755),(40,34,63,19,60,'2024-01-18',1013297),(41,14,63,13,32,'2024-08-03',1481657),(42,30,53,14,96,'2024-09-10',926920),(43,13,88,18,48,'2024-02-20',827472),(44,46,60,13,4,'2024-02-16',1572693),(45,20,93,5,37,'2023-12-20',997149),(46,37,24,17,35,'2024-10-05',1326569),(47,14,47,19,31,'2024-09-13',1989539),(48,27,36,2,16,'2024-05-18',1953626),(49,1,57,20,46,'2023-12-25',882820),(50,16,91,19,1,'2024-07-21',1732823),(51,24,43,15,44,'2024-02-25',1066835),(52,7,21,8,44,'2024-06-06',1395064),(53,19,93,8,100,'2023-11-11',775693),(54,11,50,14,11,'2024-06-24',1327930),(55,23,86,3,76,'2024-10-02',1361217),(56,34,89,4,96,'2024-07-05',1888625),(57,1,93,20,59,'2024-06-06',1166109),(58,33,94,6,96,'2024-08-29',1601903),(59,22,81,4,87,'2024-06-12',1176920),(60,14,4,8,25,'2024-02-13',527907),(61,13,33,20,76,'2024-09-19',1200919),(62,14,89,15,86,'2024-10-03',1960786),(63,32,86,1,26,'2023-12-08',713266),(64,20,9,11,4,'2024-02-21',1579600),(65,30,77,9,46,'2024-10-17',1417723),(66,28,45,2,91,'2023-12-20',1622679),(67,12,53,8,31,'2024-04-09',1012432),(68,16,57,11,15,'2024-10-17',1719881),(69,14,59,14,7,'2024-05-18',812172),(70,11,81,14,45,'2023-11-19',836526),(71,20,97,10,10,'2023-12-07',1883748),(72,17,54,8,85,'2024-07-25',717927),(73,26,36,20,68,'2024-03-16',1931206),(74,32,86,3,74,'2024-01-05',1663251),(75,29,89,11,47,'2024-09-19',1058172),(76,36,73,17,62,'2024-03-17',1848270),(77,25,95,14,14,'2024-07-19',579532),(78,21,87,19,89,'2024-06-17',1720403),(79,8,81,5,8,'2024-01-01',508830),(80,50,93,17,81,'2024-02-03',1144503),(81,9,47,1,95,'2024-03-01',673509),(82,28,49,13,25,'2024-10-06',736512),(83,8,90,18,85,'2024-08-19',933172),(84,16,47,9,55,'2024-01-21',1988027),(85,41,50,13,41,'2024-10-21',975522),(86,26,82,1,56,'2024-03-30',1112423),(87,32,82,1,7,'2024-03-29',1265703),(88,45,44,12,62,'2024-09-16',1527954),(89,45,57,16,83,'2023-12-09',915960),(90,23,21,13,10,'2024-04-25',635330),(91,32,51,13,7,'2024-04-19',1133593),(92,37,78,2,49,'2023-11-30',1900174),(93,35,50,15,42,'2023-11-13',1804881),(94,26,62,15,12,'2024-04-18',1374103),(95,16,59,9,58,'2024-06-15',1973253),(96,34,49,3,40,'2024-06-23',1065530),(97,45,16,13,29,'2024-05-08',581219),(98,14,29,10,3,'2024-05-24',1596494),(99,4,31,5,4,'2023-12-11',1243381);
/*!40000 ALTER TABLE `Sale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SalesPerson`
--

DROP TABLE IF EXISTS `SalesPerson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SalesPerson` (
  `SalesPersonID` int NOT NULL AUTO_INCREMENT,
  `SP_Name` varchar(50) DEFAULT NULL,
  `Gender` varchar(10) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `MobileNo` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `Address1` varchar(100) NOT NULL,
  `Address2` varchar(100) NOT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `PinCode` varchar(20) NOT NULL,
  PRIMARY KEY (`SalesPersonID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SalesPerson`
--

LOCK TABLES `SalesPerson` WRITE;
/*!40000 ALTER TABLE `SalesPerson` DISABLE KEYS */;
INSERT INTO `SalesPerson` VALUES (1,'Pedro Hayes','Female','1965-08-10','(632)614-83','smithmatthew@example.com','196 Morgan Fields','Suite 422','Sharonchester','Wyoming','38156'),(2,'Justin Martin','Male','1991-10-29','780.897.183','gmoreno@example.org','9302 Angela Divide Apt. 228','Suite 786','Riverabury','Nevada','22713'),(3,'Michelle Vazquez','Female','1960-09-28','2056465489','patricia98@example.net','92848 Ortega Rest','Suite 306','Jennifershire','Washington','72547'),(4,'Mr. Mark Sanchez','Female','1972-09-23','+1-879-456-','danielbrady@example.net','296 Sarah Course','Suite 314','Rodriguezhaven','Montana','35824'),(5,'Juan Page','Female','1981-03-29','734-896-180','reevesangel@example.org','75263 Chelsea Court Apt. 503','Apt. 103','Laurenbury','New York','40599'),(6,'Jason Smith','Male','1963-04-28','(691)820-07','melissa56@example.com','9506 Morgan Manor Suite 178','Suite 687','Perryfort','Georgia','61858'),(7,'Elaine Reyes','Female','1962-03-18','(289)434-55','timothy91@example.org','70889 Contreras Groves Apt. 549','Apt. 108','Tonymouth','Arkansas','61484'),(8,'James Figueroa','Male','1993-08-28','+1-954-651-','deborahshannon@example.com','156 Ramos Meadows','Suite 791','Powersfurt','Arkansas','06497'),(9,'Eugene Cowan','Female','1980-10-13','683.926.644','brookegilmore@example.com','36829 Russell Bypass Suite 120','Apt. 507','South Briannaborough','New Hampshire','94705'),(10,'Jodi Love','Female','1967-09-10','747.362.739','dmartin@example.net','10785 Lewis Place','Suite 187','East Angelaberg','Wisconsin','56778'),(11,'Jeffery Smith','Male','1982-08-08','(380)357-83','rmathis@example.net','46890 Anthony Mountains Apt. 227','Suite 013','East Meganside','Washington','33868'),(12,'Michelle Sanders','Female','1988-10-11','(736)425-70','jackie52@example.com','695 Shaw Plains Suite 764','Suite 440','Mitchellview','Virginia','94462'),(13,'Rodney Snyder','Male','1980-08-21','(976)882-39','marcus84@example.com','1584 Nelson Plains Suite 380','Apt. 340','Williamsburgh','Idaho','59895'),(14,'Chase Burnett','Male','1978-11-08','001-679-278','kenneth72@example.com','8385 Dominguez Cape','Suite 199','Rebeccastad','Missouri','87227'),(15,'Suzanne Cook','Male','1983-07-01','802.221.609','chapmandaniel@example.org','111 Mark Underpass Apt. 377','Suite 686','Port Scottchester','Pennsylvania','58818'),(16,'Kim Cherry','Female','1964-04-10','384.915.827','sean17@example.org','2457 Brown Plains','Apt. 271','Clarkborough','Colorado','98652'),(17,'Jennifer Harvey','Female','1991-12-13','466.918.415','michaelwhite@example.org','77428 Bailey Lights Apt. 350','Apt. 507','South Jamesview','Massachusetts','15987'),(18,'Wendy Klein','Male','1986-03-17','001-879-825','grahamanthony@example.org','5584 Howard Pines','Apt. 917','Danielhaven','New York','70904'),(19,'Erika Potts','Female','1977-12-07','001-831-436','carlos21@example.net','095 Nguyen Common Suite 894','Suite 099','West Ericamouth','Maine','40301'),(20,'Eric Mccarthy','Male','1974-10-25','419.435.299','louis19@example.com','275 Bishop Lakes','Apt. 658','Lake Kristenton','Vermont','49355');
/*!40000 ALTER TABLE `SalesPerson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `role` varchar(50) NOT NULL DEFAULT 'User',
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (6,'lokeshdangi','pbkdf2:sha256:600000$NfeKEQ1s8rOHHDdR$dbc02a2c5d25b9287a9bbfe2610c842f5fe5c67652a1683544b86c9481da7498','User'),(7,'paritosh','pbkdf2:sha256:600000$ZF925voHBib9KqSb$ecaa5cbfeef22fcc7acedefd243f7c599a911e59ae123e0526ae1e258909d687','User'),(8,'anilgehlot','pbkdf2:sha256:600000$yPtqDmLC8D7ckLKK$69a16695387dc37a86b98dd984eebb40c7abb702f6ed4d96e342ce74da71f37d','User'),(9,'kapil','pbkdf2:sha256:600000$9JNQsdeoHZfpJLnd$28d87f5fdda231943c6e1ee8a54b030194366c27d3c964c327caa3d75226d9dc','User');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-28  9:44:41
