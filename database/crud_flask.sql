
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `web_scrapping_db`
--

CREATE TABLE IF NOT EXISTS `website_scrape_logs` (
  `image_name` varchar(50) NOT NULL,
  `total_downloads` varchar(50) NOT NULL,
  `total_stars` varchar(50) NOT NULL,
  `total_pulls` varchar(50) NOT NULL,
  `ingested_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
