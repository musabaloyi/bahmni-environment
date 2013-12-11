#!/bin/sh
set -e -x

java -Dliquibase.databaseChangeLogTableName=liquibasechangelog -Dliquibase.databaseChangeLogLockTableName=liquibasechangeloglock -jar <%= tomcatInstallationDirectory %>/webapps/<%= openerp_atomfeed_war_file_name %>/WEB-INF/lib/liquibase-core-2.0.3.jar --driver=org.postgresql.Driver --classpath=$1/<%= openerp_atomfeed_war_file_name %>.war --changeLogFile=<%= tomcatInstallationDirectory %>/webapps/<%= openerp_atomfeed_war_file_name %>/WEB-INF/classes/sql/db_migrations.xml --url=jdbc:postgresql://localhost:5432/openerp --username=postgres --password=postgres update