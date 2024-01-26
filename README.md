# FinvestHoldings
This repository will hold the code for Assignment 1 for the course SYSC 4810: Network and Software Security.


# Introduction
Imagine that you are an employee of a computer security consulting firm. Your consulting firm has recently been approached and contracted by a company called Finvest Holdings, which has requested the design and implementation of a user authentication and access control system prototype for their proprietary financial software and data systems to better support their clients. You have been assigned as the lead developer for this contract and are responsible for developing and documenting the prototype design and implementation to fulfill the contractual obligations of your consulting firm with Finvest Holdings. The details of these contractual obligations are provided in the sections below.
The different parts of this assignment are designed to guide your investigation into the client’s concerns. At the end of the assignment, you will be required to summarize your findings and provide recommendations to Finvest Holdings addressing their concerns.

# Context
Finvest Holdings specializes in financial planning and investment banking, with access to numerous financial instruments. Financial instruments are assets that can be traded, or they can also be seen as packages of capital that may be traded. Most types of financial instruments provide efficient flow and transfer of capital all throughout the world’s investors. These assets can be cash, a contractual right to deliver or receive cash or another type of financial instrument, or evidence of one’s ownership of an entity. Finvest Holdings operates numerous computer applications to manage and assist clients. They seek to have a new user authentication and access control system for their proprietary financial software and data systems. Details of their previous user authentication and access control system have not been provided.
It is clearly stated in the contract that the following access control policy must be enforced:
1. Clients can view their account balance, view their investments portfolio, and view the contact details of their Financial Advisor.
2. Premium Clients can modify their investment portfolio and view the contact details of their Financial Planner and Investment Analyst.
3. All Finvest Holdings employees (except for Technical Support) can view a client’s account balance and investment portfolio, but only Financial Advisors, Financial Planners, and Investment Analysts can modify a client’s investment portfolio.
4. Financial Planners can view money market instruments.
5. Financial Advisors and Financial Planners can view private consumer instruments.
6. Investment Analysts can view money market instruments, derivatives trading, interest instruments, and private consumer instruments.
7. Technical Support can view a client’s information and request client account access to troubleshoot client’s technical issues.
8. Tellers can only access the system during business hours from 9:00AM to 5:00PM.
9. Compliance Officers can validate modifications to investment portfolios.

In addition to the access control policy, the prototype must implement a proactive password checker that ensures all passwords adhere to the following password policy:
• Passwords must be least 8-12 characters in length
• Password must include at least:
– one upper-case letter;
– one lower-case letter;
– one numerical digit, and
– one special character from the set: {!, @, #, $, %, ?, ∗}
• Passwords found on a list of common weak passwords (e.g., Password1, Qwerty123, or Qaz123wsx) must be prohibited
– Special Note: The list should be flexible to allow for the addition of new exclusions over time.
• Passwords matching the format of calendar dates, license plate numbers, telephone numbers, or other
common numbers must be prohibited
• Passwords matching the user ID must be prohibited
In addition, to the access control and password policies described above, Finvest Holdings has expressed the following requirements and constraints of their system, which must be considered in the eventual design and implementation of the prototype.
1. A balance between performance and security is required.
2. Selected algorithms should not have any well-known weaknesses or vulnerabilities.

## Problem 1
Design the Access Control Mechanism: Consider the problem context outlined in Part I, and in particular, the access control policy provided by Finvest Holdings. In this problem, you are required to design and implement an access control mechanism that is suitable for control access the various functions/objects in the system. At this stage, assume that you are able to authenticate users. To complete this problem, do the following:

(a) Select the access control model: Choose an appropriate access control model (e.g., DAC, MAC, RBAC, ABAC, some combination) to be used in the development of your proptype. Justify your selection.

(b) Select the access control representation: Choose an appropriate representation for your access control policy control model (e.g., access control matrix, access control list, policy store, etc.) to be used in the development of your proptype. Justify your selection.

(c) Sketch a design of the access control mechanism: Provide a sketch of the access control mechanism using your chosen access control model from Task (a), and your chosen representation from Task (b). For example, if you choose to design a DAC model using an access control matrix, sketch what the access control matrix will look like for the access control policy provided by Finvest Holdings. If you choose to design an ABAC model, specify the policy rules for the access control policy provided by Finvest Holdings. If you choose to design an ABAC model, describe the security labels including levels and compartments for the access control policy provided by Finvest Holdings.

(d) Implement the access control mechanism: Provide an implementation of the access control mechanism that you designed in Task (c). Be sure to include code fragments in your report and to clearly describe how you implemented your design.
(e) Test the access control mechanism: Provide a description of how you tested the access control mechanism.

## Problem 2
Design the Password File: In this problem, you are required to design and implement a password file that is suitable for loading and verifying the passwords of system users. To complete this problem, do the following:

(a) Select the hash function: Consider the procedure. Choose the specific hashing algorithm that you will employ in your password file mechanism. Be sure to clearly justify your selection of all required parameters including hash length, salt length, salt generation, etc.

(b) Design password file record structure: Consider the information that you need to store in each record of the password file. Design and explain the structure of each record in your password file.
HINT: This may need to be done by considering the information you require for your access control mechanism designed in Problem 1.

(c) Implement the password file: Provide an implementation of the password file that you designed in Tasks (a) and (b) Your password file should be a plain text file called passwd.txt. You should have functions to add records to the password file and to retrieve records from the password file. Be sure to include code fragments in your report and to clearly describe how you implemented your design.

(d) Test the password file mechanism: Provide a description of how you tested the password file mechanism.

## Problem 3
Enrol Users: In this problem, you are required to design and implement a mechanism to enrol users in the system. To complete this problem, do the following:

(a) Design a simple user interface: Provide the design of a simple user interface that enables a user to enter their user ID and chosen password, as well as any other information that may be required. For this problem, you should ensure that you only ask for information that is necessary to operate the system, or that is required for user authentication and access control.

(b) Design the proactive password checker: Provide the design of a proactive password checker to enforce the password policy outlined in Part I. For this problem, you may wish to use pseudocode or another appropriate tool to sketch the design of the password checker. Be sure to justify your design decisions.

(c) Implement the enrolment mechanism and the proactive password checker: Provide an implementation of the enrolment interface and the proactive password checker that you designed in Tasks (a) and (b). Be sure to include code fragments in your report and to clearly describe how you implemented your designs.

(d) Test the enrolment mechanism and the proactive password checker: Provide a description of how you tested the enrolment mechanism and the proactive password checker.

## Problem 4
Login Users: In this problem, you are required to design and implement a mechanism to enable users to login to the system. To complete this problem, do the following:

(a) Design a simple user interface: Provide the design of a simple login user interface that enables a user to enter their user ID and password.

(b) Implement the password verification mechanism: Provide an implementation of the password verification mechanism that corresponds to the password file mechanism you designed in Problem 2. Be sure to include code fragments in your report and to clearly describe how you implemented your designs.

(c) Enforce the access control mechanism: Upon successful user authentication, provide an implementation to enforce the access control mechanism developed in Problem 1. Once logged in, the following information must be displayed for the authenticated user: user ID, role/attributes/labels associated with that user and that have been used for access control purposes, and a list of the access rights or permissions according to the access control policy provided by Finvest Holdings.

(d) Test the user login and access control enforcement mechanism: Provide a description of how you tested the user login and access control enforcement mechanism.