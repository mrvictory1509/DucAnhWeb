-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 26, 2021 at 03:50 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vests_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add vests', 8, 'add_vests'),
(30, 'Can change vests', 8, 'change_vests'),
(31, 'Can delete vests', 8, 'delete_vests'),
(32, 'Can view vests', 8, 'view_vests'),
(33, 'Can add cart', 9, 'add_cart'),
(34, 'Can change cart', 9, 'change_cart'),
(35, 'Can delete cart', 9, 'delete_cart'),
(36, 'Can view cart', 9, 'view_cart'),
(37, 'Can add bill', 10, 'add_bill'),
(38, 'Can change bill', 10, 'change_bill'),
(39, 'Can delete bill', 10, 'delete_bill'),
(40, 'Can view bill', 10, 'view_bill');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$gdXATVu63bT0$LrmKaXqNkwA+J/ul1YR/x6TNKYbBmoIHg1ouSuXZFvg=', '2021-03-24 13:22:37.110702', 1, 'thang', '', '', '', 1, 1, '2021-03-24 13:22:17.515098');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-03-25 01:46:45.781161', '1', 'Vests', 1, '[{\"added\": {}}]', 7, 1),
(2, '2021-03-25 01:47:01.030405', '2', 'Pants', 1, '[{\"added\": {}}]', 7, 1),
(3, '2021-03-25 01:47:16.415288', '3', 'Belts', 1, '[{\"added\": {}}]', 7, 1),
(4, '2021-03-25 01:47:32.884466', '4', 'Shoes', 1, '[{\"added\": {}}]', 7, 1),
(5, '2021-03-25 01:47:45.651589', '5', 'Shirts', 1, '[{\"added\": {}}]', 7, 1),
(6, '2021-03-25 01:47:59.542000', '6', 'Ties', 1, '[{\"added\": {}}]', 7, 1),
(7, '2021-03-25 01:50:32.406504', '1', 'Air Jordan OG', 1, '[{\"added\": {}}]', 8, 1),
(8, '2021-03-25 01:51:09.376257', '2', 'Air Jordan 7 Retro', 1, '[{\"added\": {}}]', 8, 1),
(9, '2021-03-25 01:54:01.242726', '3', 'Pants1', 1, '[{\"added\": {}}]', 8, 1),
(10, '2021-03-25 01:54:31.894591', '4', 'Pants2', 1, '[{\"added\": {}}]', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'Home', 'bill'),
(9, 'Home', 'cart'),
(7, 'Home', 'category'),
(8, 'Home', 'vests'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-03-24 13:18:19.096864'),
(2, 'auth', '0001_initial', '2021-03-24 13:18:21.473197'),
(3, 'admin', '0001_initial', '2021-03-24 13:18:29.336140'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-03-24 13:18:31.180266'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-03-24 13:18:31.268785'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-03-24 13:18:32.176425'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-03-24 13:18:33.525098'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-03-24 13:18:33.747110'),
(9, 'auth', '0004_alter_user_username_opts', '2021-03-24 13:18:33.820568'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-03-24 13:18:34.488757'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-03-24 13:18:34.518930'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-03-24 13:18:34.617943'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-03-24 13:18:34.810464'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-03-24 13:18:34.892464'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-03-24 13:18:35.147260'),
(16, 'auth', '0011_update_proxy_permissions', '2021-03-24 13:18:35.228021'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-03-24 13:18:35.388737'),
(18, 'sessions', '0001_initial', '2021-03-24 13:18:35.678011'),
(19, 'Home', '0001_initial', '2021-03-25 01:42:22.973666'),
(20, 'Home', '0002_auto_20210325_0842', '2021-03-25 01:42:26.630074');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('qpu7v15d00kkhy1dm4s8f18o2kxqz8w1', '.eJxVjDsOwjAQRO_iGlnr78aU9DmD5c8GB5AtxUmFuDuJlAK60bw382Y-bGvxW6fFz5ldmWCX3y6G9KR6gPwI9d54anVd5sgPhZ-087Flet1O9--ghF72dbJOGUsJEIYsFBm1ByulnnTWkQjQaVKkQBAOgDEFEk46hxZgMhLZ5wu-2za-:1lP3T3:jR1_hezof2eBvt8ItTbWd3T-Kh75q7YyaMiWF0pfYkM', '2021-04-07 13:22:37.179266');

-- --------------------------------------------------------

--
-- Table structure for table `home_bill`
--

CREATE TABLE `home_bill` (
  `id` int(11) NOT NULL,
  `Date` datetime(6) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `Ship` tinyint(1) DEFAULT NULL,
  `UserID_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `home_cart`
--

CREATE TABLE `home_cart` (
  `id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `UserID_id` int(11) DEFAULT NULL,
  `VestsID_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `home_category`
--

CREATE TABLE `home_category` (
  `id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `home_category`
--

INSERT INTO `home_category` (`id`, `Name`, `Description`) VALUES
(1, 'Vests', 'Đây là vest'),
(2, 'Pants', 'Đây là Pants'),
(3, 'Belts', 'Đây là Belts'),
(4, 'Shoes', 'Đây là Shoes'),
(5, 'Shirts', 'Đây là Shirts'),
(6, 'Ties', 'Đây là Ties');

-- --------------------------------------------------------

--
-- Table structure for table `home_vests`
--

CREATE TABLE `home_vests` (
  `id` int(11) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Price` int(11) DEFAULT NULL,
  `NumberBuy` int(11) DEFAULT NULL,
  `Made_in` varchar(40) NOT NULL,
  `Sales` tinyint(1) DEFAULT NULL,
  `New_Price` int(11) DEFAULT NULL,
  `Image` varchar(100) NOT NULL,
  `Description` longtext DEFAULT NULL,
  `CategoryID_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `home_vests`
--

INSERT INTO `home_vests` (`id`, `Name`, `Price`, `NumberBuy`, `Made_in`, `Sales`, `New_Price`, `Image`, `Description`, `CategoryID_id`) VALUES
(1, 'Air Jordan OG', 7, 2, 'VN', 0, NULL, '2.jpeg', 'aaaaa', 1),
(2, 'Air Jordan 7 Retro', 3, 3, 'HQ', 1, 2, '3.jpeg', 'aaaaaa', 1),
(3, 'Pants1', 5, 2, 'VN', 0, NULL, '3.jpg', 'ssss', 2),
(4, 'Pants2', 5, 2, 'VN', 1, 4, '4.jpg', 'asssssss', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `home_bill`
--
ALTER TABLE `home_bill`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Home_bill_UserID_id_d0b4d7c5_fk_auth_user_id` (`UserID_id`);

--
-- Indexes for table `home_cart`
--
ALTER TABLE `home_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Home_cart_UserID_id_9c91fbb5_fk_auth_user_id` (`UserID_id`),
  ADD KEY `Home_cart_VestsID_id_bd2a562b_fk_Home_vests_id` (`VestsID_id`);

--
-- Indexes for table `home_category`
--
ALTER TABLE `home_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home_vests`
--
ALTER TABLE `home_vests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Home_vests_CategoryID_id_4e2eac13_fk_Home_category_id` (`CategoryID_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `home_bill`
--
ALTER TABLE `home_bill`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `home_cart`
--
ALTER TABLE `home_cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `home_category`
--
ALTER TABLE `home_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `home_vests`
--
ALTER TABLE `home_vests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `home_bill`
--
ALTER TABLE `home_bill`
  ADD CONSTRAINT `Home_bill_UserID_id_d0b4d7c5_fk_auth_user_id` FOREIGN KEY (`UserID_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `home_cart`
--
ALTER TABLE `home_cart`
  ADD CONSTRAINT `Home_cart_UserID_id_9c91fbb5_fk_auth_user_id` FOREIGN KEY (`UserID_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `Home_cart_VestsID_id_bd2a562b_fk_Home_vests_id` FOREIGN KEY (`VestsID_id`) REFERENCES `home_vests` (`id`);

--
-- Constraints for table `home_vests`
--
ALTER TABLE `home_vests`
  ADD CONSTRAINT `Home_vests_CategoryID_id_4e2eac13_fk_Home_category_id` FOREIGN KEY (`CategoryID_id`) REFERENCES `home_category` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
