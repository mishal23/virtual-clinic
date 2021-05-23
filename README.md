# Virtual Clinic - An Integrated Care System

[![Build Status](https://travis-ci.org/mishal23/virtual-clinic.svg?branch=master)](https://travis-ci.org/mishal23/virtual-clinic)
[![Coverage Status](https://img.shields.io/codecov/c/github/mishal23/virtual-clinic.svg)](https://codecov.io/gh/mishal23/virtual-clinic)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1873/badge)](https://bestpractices.coreinfrastructure.org/projects/1873)
![my website](https://img.shields.io/website-up-down-green-red/http/virtual-clinic.herokuapp.com.svg?label=website)
[![Commits](https://github-basic-badges.herokuapp.com/commits/mishal23/virtual-clinic.svg)]()
[![License](https://github-basic-badges.herokuapp.com/license/mishal23/virtual-clinic.svg)]()
[![Pulls](https://github-basic-badges.herokuapp.com/pulls/mishal23/virtual-clinic.svg)]()
[![Issues](https://github-basic-badges.herokuapp.com/issues/mishal23/virtual-clinic.svg)]()

A software to simplify the process of Health Care in hospitals to help the patients, doctor, labs, chemist.

## Introduction

- Everything is well documented, please take a look at [docs](./docs) folder.
- All the required UML Diagrams are also drawn.
- Finally it is also deployed: http://virtual-clinic.herokuapp.com/
- Steps to setup the project are mentioned [here](./docs/INSTALLATION.md)
- Steps to deploy are mentioned [here](./docs/DEPLOY.md)

## Features:

- Common Login for all users
- Patient Registration

### Admin

- Add Doctor/Lab/Chemist
- Archive Users
- Restore Archived Users
- Add/Delete Speciality/Symptoms
- Add Hospitals
- View Activity
- View System Statistics
- View/Send Messages
- Update Profile
- Change Password

### Patient

- Create Appointments
- Update Medical Information
- View Prescriptions
- View Medical Tests
- View/Send Messages
- Generate Invoice of Prescription
- Update Profile
- Change Password

### Doctor

- Consult Appointments
- View/Update/Generate Prescriptions
- View Medical Information of patients
- Update Profile
- Change Password

### Lab

- Upload Medical Tests
- View/Send Messages
- Update Profile
- Change Password

### Chemist

- Update Medicine Delivery Status(Update Prescriptions)
- View/Send Messages
- Update Profile
- Change Password

## Structure of Repository

- All the documents are in `docs` folder.
- All the UML Diagrams are in `UML Diagrams` folder.
- In the virtualclinic folder
  - `public` folder contains all the templates.
  - `server` folder contains the views (business logic).
  - `testing` folder contains all the tests cases.
  - `virtualclinic` folder contains Django configuration files for the project.

## Contributing

- The repository is open for contributions from all interested developers.
- Also, you can write by opening an Issue and also solve a current issue if possible.
- Fork this project to your Github acoount.
- After forking, clone the repository to local system and make the necessary changes.
- Kindly send Pull Requests with explanation as to what changes you have done.

## Feature Requests

- Incase you would like to see a feature to be implemented in this project, please open an issue, or send an email to me!

## License

- The software is under MIT License
