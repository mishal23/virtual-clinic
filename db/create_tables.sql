-- DO NOT USE THIS, PLEASE USE DJANGO MIGRATIONS, THIS IS JUST FOR ILLUSTRATORY PURPOSE
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
	`location_id` int UNIQUE, 
	PRIMARY KEY (`id`),
	CONSTRAINT FOREIGN KEY (`location_id`) REFERENCES `location`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `User` (
	`id` int NOT NULL AUTO_INCREMENT,
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
	`created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`prefHospital_id` int UNIQUE,
	`primaryCareDoctor_id` int UNIQUE,
	PRIMARY KEY (`id`),
	CONSTRAINT FOREIGN KEY(`prefHospital_id`) REFERENCES `hospital`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `account` (
	`id` int NOT NULL AUTO_INCREMENT,
	`role` ENUM ('Patient','Doctor','Admin','Lab','Chemist'),
	`profile_id` int UNIQUE,
	`user_id` int UNIQUE,
	`archived` bool DEFAULT False,
	PRIMARY KEY (`id`),
	FOREIGN KEY(`profile_id`) REFERENCES `profile`(`id`) ON DELETE CASCADE,
	FOREIGN KEY(`user_id`) REFERENCES `User`(`id`) ON DELETE CASCADE
);

ALTER TABLE `profile` ADD FOREIGN KEY(`primaryCareDoctor_id`) REFERENCES `account`(`id`) ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS `appointment` (
	`id` int NOT NULL AUTO_INCREMENT,
	`doctor_id` int NOT NULL UNIQUE,
	`patient_id` int NOT NULL UNIQUE,
	`description` varchar(250) NOT NULL,
	`status` varchar(50) NOT NULL DEFAULT 'Active',
	`hospital_id` int UNIQUE,
	`appointment_type` varchar(10) DEFAULT 'Offline',
	`startTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`endTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`),
	CONSTRAINT FOREIGN KEY(`doctor_id`) REFERENCES `account`(`id`) ON DELETE CASCADE,
	CONSTRAINT FOREIGN KEY(`patient_id`) REFERENCES `account`(`id`) ON DELETE CASCADE,
	CONSTRAINT FOREIGN KEY(`hospital_id`) REFERENCES `hospital`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `message` (
	`id` int NOT NULL AUTO_INCREMENT,
	`target_id` int UNIQUE,
	`sender_id` int UNIQUE,
	`header` varchar(100) NOT NULL,
	`body` varchar(1000) NOT NULL,
	`timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ,
	PRIMARY KEY (`id`),
	CONSTRAINT FOREIGN KEY(`target_id`) REFERENCES `account`(`id`) ON DELETE CASCADE,
	CONSTRAINT FOREIGN KEY(`sender_id`) REFERENCES `account`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `prescription` (
	`id` int NOT NULL AUTO_INCREMENT,
	`patient_id` int UNIQUE,
	`doctor_id` int UNIQUE,
	`date` timestamp NOT NULL,
	`medication` varchar(100) NOT NULL,
	`instruction` varchar(100) NOT NULL,
	`active` bool DEFAULT True,
	PRIMARY KEY (`id`),
	CONSTRAINT FOREIGN KEY(`patient_id`) REFERENCES `account`(`id`) ON DELETE CASCADE,
	CONSTRAINT FOREIGN KEY(`doctor_id`) REFERENCES `account`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `medical_test` (
	`id` int NOT NULL AUTO_INCREMENT,
	`name` varchar(100) NOT NULL,
	`hospital_id` int UNIQUE,
	`description` varchar(100) NOT NULL,
	`doctor_id` int UNIQUE,
	`patient_id` int UNIQUE,
	`date` timestamp NOT NULL,
	`completed` bool DEFAULT False,
	PRIMARY KEY (`id`),
	CONSTRAINT FOREIGN KEY(`patient_id`) REFERENCES `account`(`id`) ON DELETE CASCADE,
	CONSTRAINT FOREIGN KEY(`doctor_id`) REFERENCES `account`(`id`) ON DELETE CASCADE
);
