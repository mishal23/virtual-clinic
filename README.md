# Virtual Clinic - An Integrated Care System
A software to simplify the process of Health Care in hospitals to help the patients, doctor, labs, chemist.

## Introduction
- Project for Software Engineering Course
- Everything is well documented, please take a look at [docs](/docs) folder.
- All the required UML Diagrams are also drawn.
- Finally it is also deployed: http://virtual-clinic.herokuapp.com/
- Steps to deploy are mentioned [here](https://github.com/mishal23/virtual-clinic/blob/production/virtualclinic/README.md)

## Features:
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

- The repository has mainly three branches:
<table>
  <thead>
    <tr>
      <td><b>Branch</b></td>
      <td><b>Build Status</b></td>
      <td><b>Database</b></td>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>master</td>
      <td>Passing</td>
      <td>SQLite</td>
    </tr>
    <tr>
      <td>development</td>
      <td>Passing</td>
      <td>MySQL</td>
    </tr>
    <tr>
      <td>production</td>
      <td>Passing</td>
      <td>PostgreSQL</td>
    </tr>
  </tbody>
</table>

- All the documents are in `docs` folder.
- All the UML Diagrams are in `UML Diagrams` folder.
- In the virtualclinic folder
	- `public` folder contains all the templates.
	- `server` folder contains the views.
	- `testing` folder contains all the tests cases.
	- `virtualclinic` folder contains Django configuration files for the project.

## Contributing
- The repository is open for contributions from all interested developers.
- Also, you can write by opening an Issue and also solve a current issue if possible.
- Fork this project to your Github acoount.
- After forking, clone the repository to local system and make the necessary changes.
- Kindly send Pull Requests with explanation as to what changes you have done.

## License
- The software is under MIT License

## Contributors
- Mishal Shah ([@mishal23](https://github.com/mishal23))
- Samyak Jain ([@SamyakJ2512](https://github.com/SamyakJ2512))

