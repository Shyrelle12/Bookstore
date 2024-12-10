-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2023 at 06:28 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shyrelle`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL,
  `i_id` int(80) NOT NULL,
  `c_id` int(80) NOT NULL,
  `qty` int(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`cart_id`, `i_id`, `c_id`, `qty`) VALUES
(5, 11, 19, 1);

-- --------------------------------------------------------

--
-- Table structure for table `checkout_items`
--

CREATE TABLE `checkout_items` (
  `id` int(10) NOT NULL,
  `title` varchar(80) NOT NULL,
  `author` varchar(80) NOT NULL,
  `genre` varchar(80) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `type` varchar(80) NOT NULL,
  `customer_name` varchar(80) NOT NULL,
  `customer_id` int(10) NOT NULL,
  `customer_address` varchar(80) NOT NULL,
  `qty` int(10) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `checkout_datetime` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `checkout_items`
--

INSERT INTO `checkout_items` (`id`, `title`, `author`, `genre`, `price`, `type`, `customer_name`, `customer_id`, `customer_address`, `qty`, `total_price`, `checkout_datetime`) VALUES
(35, 'The Chronicles of Narnia', 'C.S. Lewis', 'Fantasy', 800.00, 'Book', 'Kim Nengasca', 0, 'Urgello', 1, 800.00, '2023-12-13 14:49:38'),
(36, ' You Should See Me in a Crown', 'Leah Johnson', 'Fantasy', 900.00, 'Book', 'Nedrey Golosino', 0, 'Basak Pardo', 1, 900.00, '2023-12-13 14:50:13');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(10) NOT NULL,
  `name` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL,
  `address` varchar(100) NOT NULL,
  `password` varchar(80) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `name`, `email`, `address`, `password`, `role`) VALUES
(1, 'Shyrelle Managaytay', 'mshyrelleshine@gmail.com', 'Mandaue City', '123', 'admin'),
(13, 'Kim Nengasca', 'kim@gmail.com', 'Urgello', '123', 'user'),
(19, 'Shine Lumacang', 'shy@gmail.com', 'Pardo', '123', 'user'),
(21, 'Nedrey Golosino', 'nedrey1@gmail.com', 'Basak Pardo', '123', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `itemlist`
--

CREATE TABLE `itemlist` (
  `id` int(10) NOT NULL,
  `isbn` int(10) NOT NULL,
  `title` varchar(80) NOT NULL,
  `author` varchar(80) NOT NULL,
  `genre` varchar(80) NOT NULL,
  `price` decimal(60,0) NOT NULL,
  `type` varchar(80) NOT NULL,
  `qty` int(80) NOT NULL,
  `total_price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `itemlist`
--

INSERT INTO `itemlist` (`id`, `isbn`, `title`, `author`, `genre`, `price`, `type`, `qty`, `total_price`) VALUES
(3, 124, 'The Chronicles of Narnia', 'C.S. Lewis', 'Fantasy', 800, 'Book', 38, 0.00),
(6, 476, 'War of Code', 'Allan V.', 'Action', 600, 'Book', 17, 0.00),
(7, 123, 'Harry Potter', 'J.K. Rowling', 'Fantasy', 1200, 'Book', 23, 0.00),
(8, 134, 'They Both Die at the End', 'Adam Silvera', 'Fantasy', 1000, 'Book', 39, 0.00),
(9, 154, ' You Should See Me in a Crown', 'Leah Johnson', 'Fantasy', 900, 'Book', 8, 0.00),
(10, 657, 'The Heir and the General', 'M. Dalto', 'Action', 1500, 'Book', 15, 0.00),
(11, 143, 'Tantei High 1', 'Purpleyhan ', 'Fantasy', 1200, 'Book', 1, 0.00),
(12, 2147483647, 'Harry', 'Potter', 'Fantasy, Action', 24, 'Book', 0, 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `o_id` int(50) NOT NULL,
  `c_id` int(50) NOT NULL,
  `address` varchar(80) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`o_id`, `c_id`, `address`, `date`) VALUES
(1021, 13, 'Urgello', '2023-12-14 01:19:50'),
(1022, 13, 'Urgello', '2023-12-14 01:22:23'),
(1023, 13, 'Urgello', '2023-12-14 01:26:57');

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `o_id` int(60) NOT NULL,
  `i_id` int(50) NOT NULL,
  `qty` int(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_items`
--

INSERT INTO `order_items` (`o_id`, `i_id`, `qty`) VALUES
(1021, 3, 1),
(1021, 6, 1),
(1022, 7, 1),
(1022, 8, 1),
(1023, 3, 1),
(1023, 11, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`),
  ADD KEY `fk_i_id` (`i_id`),
  ADD KEY `fk_c_id` (`c_id`);

--
-- Indexes for table `checkout_items`
--
ALTER TABLE `checkout_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `itemlist`
--
ALTER TABLE `itemlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`o_id`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD KEY `fk_name__i_id` (`i_id`),
  ADD KEY `fk_name__o_id` (`o_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `checkout_items`
--
ALTER TABLE `checkout_items`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `itemlist`
--
ALTER TABLE `itemlist`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `o_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1024;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `fk_c_id` FOREIGN KEY (`c_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `fk_i_id` FOREIGN KEY (`i_id`) REFERENCES `itemlist` (`id`);

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `fk_name__i_id` FOREIGN KEY (`i_id`) REFERENCES `itemlist` (`id`),
  ADD CONSTRAINT `fk_name__o_id` FOREIGN KEY (`o_id`) REFERENCES `orders` (`o_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
