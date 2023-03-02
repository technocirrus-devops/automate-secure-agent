# Automate Informatica Secure Agent Installation and configuration.

### What is Informatica Secure Agent?

*Informatica Cloud Secure Agent uses a token-based authentication mechanism to secure communication between the Secure Agent and Informatica Cloud Services. To automate the token generation process, you can write a script that leverages the Informatica Cloud REST API.*

---

### Process run the secure agent installler:

**Pre-requisites :**

- Latest version of Docker should be installed.
- Keep your Informatica login username and password handy.

**Steps for installation :**

1. Clone the repository and navigate to *`'automate-secure-agent'`* directory using the terminal.

2. Run **`docker build -t my_image_name .`**
<br>Example: **`docker build -t secure-agent:latest .`**<br>
*(Note: Don't forget the . (dot) in the end)*

3. Once the build is successful, run **`docker run --env USERNAME='<my_username>' --env PASSWORD='<supersecretpassword>' my_image_name`**
<br>Example: **`docker run --env USERNAME='username' --env PASSWORD='secretpassword' secure-agent:latest`**

- *Wait for the script to complete it's execution. If the script executes successfully, you get a message in the end saying **'Secure Agent Configuration Successful'***


