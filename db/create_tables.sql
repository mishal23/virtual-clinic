CREATE DATABASE IF NOT EXISTS `vclinic`;
use `vclinic`;

CREATE TABLE IF NOT EXISTS `speciality` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(50) NOT NULL,
	`description` varchar(100) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `symptom` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(50) NOT NULL,
	`description` varchar(100) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `location` (
	`id` int NOT NULL AUTO_INCREMENT,
	`city` varchar(50) NOT NULL,
	`zip` varchar(50) NOT NULL,
	`state` varchar(50) NOT NULL,
	`country` varchar(50) DEFAULT 'India',
	`address` varchar(50) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `hospital` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(50) NOT NULL,
	`phone` varchar(10) NOT NULL,
	`location_id` int  REFERENCES `location`(`id`) ON DELETE CASCADE, 
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `User` (
	`id` int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `account` (
	`id` int NOT NULL AUTO_INCREMENT,
	`role` ENUM ('Patient','Doctor','Admin','Lab','Chemist'),
	`profile_id` int REFERENCES `profile`(`id`) ON DELETE CASCADE,
	`user_id` int UNIQUE REFERENCES `User`(`id`) ON DELETE CASCADE,
	`archived` bool DEFAULT False,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `profile` (
	`id` int NOT NULL AUTO_INCREMENT,
	`firstname` varchar(50),
	`lastname` varchar(50),
	`sex` ENUM ('M', 'F'),
	`birthday` timestamp DEFAULT CURRENT_TIMESTAMP,
	`phone` varchar(10),
	`allergies` varchar(250),
	`created` timestamp DEFAULT CURRENT_TIMESTAMP,
	`prefHospital_id` int REFERENCES `hospital`(`id`) ON DELETE CASCADE,
	`primaryCareDoctor_id` int REFERENCES `account`(`id`) ON DELETE CASCADE,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `appointment` (
	`id` int NOT NULL AUTO_INCREMENT ,
	`doctor_id` int UNIQUE REFERENCES `account`(`id`) ON DELETE CASCADE,
	`patient_id` int UNIQUE REFERENCES `account`(`id`) ON DELETE CASCADE,
	`description` varchar(250) NOT NULL,
	`status` varchar(50) NOT NULL DEFAULT 'Active',
	`hospital_id` int UNIQUE REFERENCES `hospital`(`id`) ON DELETE CASCADE,
	`appointment_type` varchar(10) DEFAULT 'Offline',
	`startTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`endTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `message` (
	`id` int NOT NULL AUTO_INCREMENT,
	`target_id` int UNIQUE REFERENCES `account`(`id`) ON DELETE CASCADE,
	`sender_id` int UNIQUE REFERENCES `account`(`id`) ON DELETE CASCADE,
	`header` varchar(100) NOT NULL,
	`body` varchar(1000) NOT NULL,
	`timestamp` timestamp NOT NULL ,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `prescription` (
	`id` int NOT NULL AUTO_INCREMENT,
	`patient_id` int UNIQUE REFERENCES `account`(`id`) ON DELETE CASCADE,
	`doctor_id` int UNIQUE REFERENCES `account`(`id`) ON DELETE CASCADE,
	`date` timestamp NOT NULL,
	`medication` varchar(100) NOT NULL,
	`instruction` varchar(100) NOT NULL,
	`active` bool DEFAULT True,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `medical_test` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(100) NOT NULL,
	`hospital_id` int UNIQUE REFERENCES `hospital`(`id`) ON DELETE CASCADE,
	`description` varchar(100) NOT NULL,
	`doctor_id` int UNIQUE REFERENCES `account`(`id`) ON DELETE CASCADE,
	`patient_id` int UNIQUE REFERENCES `account`(`id`) ON DELETE CASCADE,
	`date` timestamp NOT NULL,
	`completed` bool DEFAULT False,
	PRIMARY KEY (`id`)
);

