# Solar_energy_management

 ## Project presentation:

The purpose of Solar_energy_management is to provide a simple interface to manage data from solar panels and integrate them with blockchain ad web3
for, in the future, make the unused energy sellable to others in the net for a more greener world with sustainable cities.

[Canva presentation](https://www.canva.com/design/DAFHHsTn8L8/aVLqRqMF2Hv61A4Fd6ql6w/view?utm_content=DAFHHsTn8L8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)

## Technologies:

- Django
- Web3.py
- Redis
- django_crontab
- Task scheduler

## Isntallation:
 - Make your virtual enviroment
 - Activate it
 - Install pakages with requirements.txt
   ```js
   pip install -r requirements.txt
   ```
 - Migrate
    ```js
   python manage.py migrate
   ```
 - Create super user
   ```js
   python manage.py createsuperuser
   ```
 - Activate Django_crontab
   ```js
   python manage.py crontab add
   ```
 - I made a manage.py command to retrive data manually
    ```js
   python manage.py data_retriever
   ```
 - Make sure to insert your data in secret.py and you are ready to go...

### For Windows users:
**Django_crontab** isn't compatible with windows then you can delete 
*"django_crontab"* from *INSTALLED_APPS* and *CRONJOBS* in *eco_hotel/settings.py*
and skip the **Django_crontab** installation. Instead for the automatic operation you can use the **management commad** *data_retriever*
with **Windows task scheduler** just import the *data_retriever.xml* file, make sure to modify it with your values. 
 
 URL to my endpoint for retrieve data: "https://955cf8ae-5a74-4e4d-85d4-e8095a57862a.mock.pstmn.io"
   
### You can visit the online website [Here](http://18.195.120.80:8000/):

- I made some users that you can try out the website

> Admin:
- Username = admin
- Password = adminpassword1

> User:
- Username = user
- Pssword = userpassword

## Functionality:

- Data structured in a **Table** with integrated **search box**, where you can search transaction on the page along with a **pagination** function for moving around the pages.

- The site has been designed to work in **autonomy** thanks to a server side **taimed** tasks with the **django_crontab** and for windows *Task scheduler*, where daily send a GET request to the endpoint to retrieve the data, make a Ethereum ropsten (Testnet) transaction with the data as notes and finally store all the values in the database.

- **Login Security** for the admin user in case of login from different IP made it superfast thanks to **redis** cache to store the IPs, dont forget to run the background server.

## Preview of the site:
<picture>
  <img src="https://github.com/Kaido997/Solar_energy_management/blob/main/Solar_energy_menagement.png">
</picture>

*Thanks for reading*
