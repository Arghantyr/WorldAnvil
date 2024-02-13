# Introduction
The code here (working name: PI-stack) is a sandbox created for backup and statistics purposes mostly. All hail knowledge!

# Changelog
2023-02-13	Utility.py module is created; the 'test.py' is cleaned and adjusted to the new module
2023-02-09	this README file is created; the TO-DO list is populated
2023-02-06	basic code uploaded - the journey begins

# TO-DO

- ~~maintenance: refactor the 'test.py' code into externally loaded module~~
- feature: add a logger and form a log retention policy
- feature: automatic pinging for change in articles based on a config file (define world, list of categories/accept ALL, ...) -- based on /article endpoint with granularity -1; if the article has changed add it to the a special list of the articles to back-up
- feature: setup a private github repo for backups
- feature: automatic daily backup of changed articles based on the /article endpoint with granularity 3
- feature: adjustment of the backup system to listen to the changes made in the pinging list; if there is a change it should act on it and call the /article endpoint on all article ids in the list, then add it to the back-up system
- feature: setup a basic statistics stack using /article endpoint with granularity 0; these data should be gathered finely, e.g., hourly
- feature: expand the statistics section to include information gained from the daily backups with granularity 3 API calls
