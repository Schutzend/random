CREATE TABLE IF NOT EXISTS `quotes` (
  `id` mediumint unsigned NOT NULL AUTO_INCREMENT,
  `author` varchar(200) NOT NULL,
  `quote` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
