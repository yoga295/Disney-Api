-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2025 at 01:57 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `disney`
--

-- --------------------------------------------------------

--
-- Table structure for table `character_history`
--

CREATE TABLE `character_history` (
  `id` int(11) NOT NULL,
  `nama_char` varchar(100) DEFAULT NULL,
  `film` varchar(100) DEFAULT NULL,
  `tv_show` varchar(100) DEFAULT NULL,
  `video_game` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `character_history`
--

INSERT INTO `character_history` (`id`, `nama_char`, `film`, `tv_show`, `video_game`) VALUES
(1, 'Mickey', '(Tidak tersedia)', 'Mickey Mouse Works', '(Tidak tersedia)'),
(2, 'Achilles', 'Hercules (film)', 'Hercules (TV series)', 'Kingdom Hearts III'),
(6, 'Abdullah', 'Cheetah', '', ''),
(7, 'Baloo', 'The Jungle Book', 'The Mouse Factory', 'TaleSpin (NES video game)'),
(8, 'Alma', '', 'Doc McStuffins', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `character_history`
--
ALTER TABLE `character_history`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `character_history`
--
ALTER TABLE `character_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
