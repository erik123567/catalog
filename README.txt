This is the Item Catalog project of the fullstack nanodegree by Erik Hedin
To run:
	- Clone this repository
	- run your vagrant machine using vagrant up 
	- connect to the vm with vagrant ssh
	- cd into /vagrant/catalog
	- run the script using python application.py
	-visit it at http://localhost:5000

API Endpoints:
	- /team/<team_id>/roster/JSON - shows the teams roster
	- /team/<team_id>/roster/<player_id>/JSON - shows info about an individual player
	- /team/JSON - lists all current teams