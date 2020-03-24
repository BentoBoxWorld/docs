# Database transition
The default database for BentoBox is one that stores files on the file system using JSON (it used to be YAML, but since 1.5.0 it is JSON). JSON should work for most servers. However, it may be that your server has grown to the point where having the database on another machine will help. Alternatively, you may have other software that wants to access that data, e.g., a web site. BentoBox offers the ability to migrate your data from one type of database to another seamlessly. If you wish to move from JSON to another database you can do that easily by using a transition database option such as JSON2MYSQL. 

## Steps

1. Stop the server
2. Make a backup of your database. If it is a flat file database then this means copy the whole database folder to a safe place.
3. Edit BentoBox's config.yml file and select a transition database option. They always have the number 2 in them, for example, JSON2MYSQL.
4. Ensure that you have also set up the database name, login and password, if required. If you are transitioning to MYSQL then you must make sure the server has the database and it is a sufficiently recent version (5.7 or later)
5. If you have a very large database, then a transition may take longer than your server timeout. So edit *spigot.yml* timeout-time and set it to a large number so the server does not crash out.
6. Start the server. BentoBox will immediately transition all islands and some other files to the database because these are loaded at startup. 
7. After the server is completely up and running, execute the *bbox migrate* command in the console. This will copy over all the players, names and all the data from the addons to the database.
8. You are done!
9. You can leave the database as the transition database, or you can now change it to the single database option, e.g., MYSQL.

