# National Cyber Threat Tracking System
 
This application will provide an interface for the general public to submit vulnerabilities they have discovered to be remedied by the appropriate government body.

**User roles:**
- General Public:
  - No account required.
  - Submit vulnerabilities.
  - View fixed vulnerabilities.
- Admin:
  - Account required.
  - Create and manage user accounts.
- Operator: 
  - Account required.
  - Verify/escalate submitted vulnerabilities.

## Getting Started

### Running The Software


There are two ways to test the software.

**1. Use the software from the cloud**
   1. Visit and try out the website at https://www.nctts-essex.com
   2. Click on Login.
   3. Login using the admin credentials.
   4. Click on Add users.
   5. Enter the user username, password, and public IP address.
     **6. Note: it is important you add the public IP address of the user otherwise you will not be able to log into the operator page.**
   7. Click on save and logout.
   8. Click on login and enter the operator user credentials.


**2. Run the software locally**
    1. Install the latest version of Python. As of writing this document is is 3.11
       1. https://www.python.org/downloads/ 
    2. Install the latest version of Django. As of writing this document it is 4.1.3
       1. https://www.djangoproject.com/download/ 
    3. Install the latest version of Git. As of writing this document it is 2.38.1
       1. https://git-scm.com/downloads 
    4. Clone the project from GitHub using the following link https://github.com/mustafa-sibai-essex/4_SSDCS_PCOM7E_2_Coding_Output
    5. Navigate to the nctts folder in the cloned project
    6. Running the following command to run the http server
       1. Python manage.py runserver
       **2. Note: When running the above command, Django will start a development server running on the less secure http protocol rather than the https protocol. This is ok since it is a development server. To view the website using the https protocol please visit the https://www.nctts-essex.com website.**
    7. Click on Login.
    8. Login using the admin credentials.
    9. Click on Add users.
    10. Enter the user username, password, and add the loopback IP address which is 127.0.0.1
       **1. Note: it is important you add the loopback IP address otherwise you will not be able to log into the operator page. The loopback IP address is only used in the development server. In the production server the user public IP address must be used instead.**
    11. Click on save and logout.
    12. Click on login and enter the operator user credentials.


## Authors

Mustafa Sibai - https://github.com/mustafa-sibai

Etkin Getir - https://github.com/etKing666

Gianluca Cannone - https://github.com/gicanon

Aaron Willis - https://github.com/aw22433

Ola Durowoju - https://github.com/O1aDee

## License

Copyright (c) [2022] [NCTTS]

Permission is hereby granted, free of charge, to any person obtaining a copy of the project without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project, and to permit persons to whom the project is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of this project.

THE PROJECT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE PROJECT OR THE USE OR OTHER DEALINGS IN THE PROJECT.
