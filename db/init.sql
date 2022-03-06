CREATE DATABASE demo;
use demo;

CREATE TABLE `task` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `status` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `task`(`id`,`name`,`status`) values
(1,'Eat Breakfast','0'),
(2,'East Lunch','1');