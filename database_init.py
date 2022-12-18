import psycopg2


# 系统管理员数据库连接接口
# Database = "GamingPlatform"
Database = "nbuuser"
User = "gaussdb"
Password = "openGauss@2022"


# 建立连接函数：连接数据库,返回psycopg2的连接对象
def create_conn():
    conn = psycopg2.connect(database=Database,
                            user=User,
                            password=Password,
                            host="127.0.0.1",
                            port="5432")
    return conn


# sql语句执行函数(无返回值),argv:需要执行的sql语句
def ExecuSQL(argv):
    conn = create_conn()
    cur = conn.cursor()  # 生成游标对象
    cur.execute(argv)  # 执行SQL语句
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接


# 建立模式
schema_create = """
--若数据库中存在模式gaussdb的话将删除
DROP SCHEMA IF EXISTS gaussdb CASCADE;
--在数据库中创建名为gaussdb的模式，并授权给用户gaussdb所有。
CREATE SCHEMA gaussdb AUTHORIZATION gaussdb;"""

# 设置会话路径
search_path = """
--设置当前会话的搜索路径为gaussdb模式、Public模式，
--随后创建的基本表就会自动创建gaussdb模式下。
SET SEARCH_PATH TO gaussdb, Public;"""

# 建表：记住账户表
createTable_UserRemembered = """
DROP TABLE IF EXISTS user_remembered;
create table user_remembered
(
    user_name     varchar               not null
        constraint user_remembered_pk
            primary key,
    user_secret   varchar               not null,
    is_remembered boolean default false not null,
    is_logged     boolean default false not null
);

comment on table user_remembered is '记住账户表：用于记住上一个登陆成功的账户';

comment on column user_remembered.user_name is '记住账号';

comment on column user_remembered.user_secret is '记住密码';

comment on column user_remembered.is_remembered is '是否记住密码';

comment on column user_remembered.is_logged is '是否已经登陆';

create unique index user_remembered_user_name_uindex
    on user_remembered (user_name);"""

# 建表：账户表
createTable_UserTable = """
DROP TABLE IF EXISTS user_table;
create table user_table
(
    user_name      varchar               not null
        constraint user_table_pk
            primary key,
    user_secret    varchar               not null,
    user_forbidden boolean default FALSE not null
);

comment on table user_table is '账户表';

comment on column user_table.user_name is '账号';

comment on column user_table.user_secret is '密码';

comment on column user_table.user_forbidden is '账号禁用标志';

create unique index user_table_user_name_uindex
    on user_table (user_name);"""

# 建表管理员表
createTable_AdministratorTable = """
DROP TABLE IF EXISTS administrator_table;
create table administrator_table
(
    administrator_name   varchar not null
        constraint administrator_table_pk
            primary key,
    administrator_secret varchar not null,
    administrator_type   varchar not null
);

comment on table administrator_table is '管理员账户表';

comment on column administrator_table.administrator_name is '管理员账号';

comment on column administrator_table.administrator_secret is '管理员密码';

comment on column administrator_table.administrator_type is '管理员类型：music代表音乐管理员，game代表游戏管理员，user代表用户管理员';

create unique index administrator_table_administrator_name_uindex
    on administrator_table (administrator_name);"""

# 创建AdministratorMusic,AdministratorGame,AdministratorUser管理员(数据库用户),并分配权限
createUser_Administrator = """
DROP USER IF EXISTS "AdministratorMusic" CASCADE;
DROP USER IF EXISTS "AdministratorGame" CASCADE;
DROP USER IF EXISTS "AdministratorUser" CASCADE;

CREATE USER "AdministratorMusic" WITH CREATEROLE PASSWORD 'AdministratorMusic@2022';
CREATE USER "AdministratorGame" WITH CREATEROLE PASSWORD 'AdministratorGame@2022';
CREATE USER "AdministratorUser" WITH CREATEROLE PASSWORD 'AdministratorUser@2022';

GRANT SELECT ON TABLE user_table to "AdministratorUser" WITH GRANT OPTION;
GRANT UPDATE ON TABLE user_table to "AdministratorUser" WITH GRANT OPTION;
GRANT INSERT ON TABLE user_table to "AdministratorUser" WITH GRANT OPTION;
grant usage on schema gaussdb to "AdministratorUser";
grant connect, create on database "GamingPlatform" to "AdministratorUser";
grant delete, insert, select, update on user_table to "AdministratorUser";
revoke insert, select, update on user_table from "AdministratorUser";
"""
# commitRole_Administrator = """
# comment on role AdministratorMusic is '音乐管理员';
# comment on role AdministratorGame is '游戏管理员';
# comment on role AdministratorUser is '用户管理员';"""

#


ExecuSQL(schema_create + search_path +
         createTable_UserRemembered + createTable_UserTable + createTable_AdministratorTable +
         createUser_Administrator)
