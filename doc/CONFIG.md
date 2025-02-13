# Banqo - Config

This document goes into deeper detail about Banqo's config.

The config file should be created in the project root, and named `config.json`. It must have the following format:

```
{
	"db": {
		"host": "[ip address of database server]",
		"user": "[name of user for database access]",
		"password": "[password of user for database access]",
		"database": "[name of created database]"
	},
	"fun": {
		"isolation_level": "[One of: 'READ UNCOMMITTED', 'READ COMMITTED', 'REPEATABLE READ', 'SERIALIZABLE']"
	}
}
```


### db.host

The address of the MySQL database server.

### db.user

The username of the DB user you created for the application. The application will use it user to manipulate with the database. It must have these permissions: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `EXECUTE`.

### db.password

The password of the user.

### db.database

The name of the database you created for the application; the one in which you invoked `database/init.sql`.


### fun.isolation_level

This sets the MySQL transaction isolation level. Depending on your chosen level, this may trigger a non-repeatable read.

See also: `doc/nrr.md`