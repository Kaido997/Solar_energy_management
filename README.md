# Solar_energy_management

Project presentation:

The purpose of Solar_energy_management is to provide a simple interface to manage data from solar panels and integrate them with blockchain ad web3
for, in the future, make the unused energy sellable to others in the net for a more greener world with sustainable cities.

Technologies:

-Django
-Web3.py
-Redis
-Threading

Isntallation:

Install pakages with requirements.txt
Make sure to insert your data in secret.py and you are ready to go...

You can use the following pre-made users:

Admin:
Username = admin
Password = adminpassword1

User:
Username = user
Pssword = userpassword

Functionality:

-Data structured in a table with integrated search box, where you can search transaction on the page along with a pagination function for moving around the pages.

-The site has been designed to work in autonomy thanks to a server side timer with the Threading library, where every 24H send a GET request to the endpoint to retrieve the data, make a Ethereum  ropsten transaction with the data as notes and finally store all the values in the database.

-Login Security for the admin user in case of login from different IP made it superfast thanks to redis cache to store the IPs, dont forget to run the background server :).

