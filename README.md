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

1. Visit and try out the website at https://www.nctts-essex.com
2. Install the following softwares:
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
        2. Note: When running the above command, Django will start a development server running on the less secure http protocol rather than the https protocol. This is ok since it is a development server. To view the website using the https protocol please visit the https://www.nctts-essex.com website.



