# Email OTP System

**Description**
--
This project is created for mimicing the email OTP validation system with the help of Python and Flask framework
</br>
<br/>



**How to run?**
--
- First install python from https://www.python.org
- Clone this repository by running the below command:
</br>

```bash
git clone https://github.com/shayansaha85/email_otp_system.git
```
- Set up *pip* if not done
- Open Command Prompt/Powershell/Terminal in the repository folder and run the below command to install all the dependencies for running this utility
</br>
```bash
pip install -r requirements.txt
```
- Update the details in the **config.properties** file
- Make sure to have proper settings in your email client in order to send email with SMTP server with the help of Python
- Run the **app.py** file with the below command
</br>
```bash
python app.py
```
- Development server will be created with the port 5151 (<i>You can change if you want in the **app.py** file</i>)
- Open browser and hit this URL : **http://<YOUR_IP_ADDRESS>:5151/home**