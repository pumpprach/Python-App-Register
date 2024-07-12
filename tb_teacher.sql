-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 12, 2024 at 09:04 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `register`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_teacher`
--

CREATE TABLE `tb_teacher` (
  `id_teacher` int(6) NOT NULL,
  `f_name_teacher` varchar(50) NOT NULL,
  `l_name_teacher` varchar(50) NOT NULL,
  `major` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `tel` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=tis620 COLLATE=tis620_bin;

--
-- Dumping data for table `tb_teacher`
--

INSERT INTO `tb_teacher` (`id_teacher`, `f_name_teacher`, `l_name_teacher`, `major`, `email`, `tel`) VALUES
(21481, 'Prach', 'Choksamritpol', 'Ce', 'pumpprach@gmail.com', '0958090462'),
(24924, 'Pakpom', 'kukkuk', 'Ce', 'pakpom@gmail.com', '0893214567');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_teacher`
--
ALTER TABLE `tb_teacher`
  ADD PRIMARY KEY (`id_teacher`,`email`,`tel`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
