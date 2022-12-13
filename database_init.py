from database.database_interface import ExecuSQL

# 建立模式
schema_create = """
--若数据库中存在模式gaussdb的话将删除
DROP SCHEMA IF EXISTS gaussdb CASCADE;
--在数据库中创建名为gaussdb的模式，并授权给用户gaussdb所有。
CREATE SCHEMA gaussdb AUTHORIZATION gaussdb;
"""
# 设置会话路径
search_path = """
--设置当前会话的搜索路径为gaussdb模式、Public模式，
--随后创建的基本表就会自动创建gaussdb模式下。
SET SEARCH_PATH TO gaussdb, Public;
"""
# 建表
createTable_UserRemembered = """
DROP TABLE IF EXISTS user_remembered;
create table user_remembered
(user_name     varchar               not null
        constraint user_remembered_pk
            primary key,
    user_secret   varchar               not null,
    is_remembered boolean default false not null
);

comment on table user_remembered is '记住账户表：用于记住上一个登陆成功的账户';

comment on column user_remembered.user_name is '记住账号';

comment on column user_remembered.user_secret is '记住密码';

comment on column user_remembered.is_remembered is '是否记住密码';

create unique index user_remembered_user_name_uindex
    on user_remembered (user_name);"""

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

ExecuSQL(schema_create + search_path + createTable_UserRemembered + createTable_UserTable)
