-- cria o esquema 'azure_company' se ainda não existir
create schema if not exists azure_company;

-- usa o esquema 'azure_company'
use azure_company;

-- seleciona todas as restrições de tabela do esquema 'azure_company'
select * from information_schema.table_constraints
    where constraint_schema = 'azure_company';
-- constraint_schema refere-se a um conjunto de regras que definem as restrições aplicadas aos dados dentro de um banco de dados.

-- restrição atribuida a um domínio
-- create domain D_num as int check(D_num> 0 and D_num< 21);

/* ------------------------------------ x ----------------------------------- */

CREATE TABLE employee(
	Fname varchar(15) not null, -- varchar determina a quantidade de caractesres
    Minit char, -- só char declarado pode levar a erro, ou dependendo do sistema de banco de dados pode existir um char padrão 
    Lname varchar(15) not null,
    Ssn char(9) not null, 
    Bdate date,
    Address varchar(30),
    Sex char,
    Salary decimal(10,2),
    Super_ssn char(9),
    Dno int not null,
    constraint chk_salary_employee check (Salary> 2000.0), --chk_salary_employee é nome da restrição criada
    constraint pk_employee primary key (Ssn)
    -- constraint define uma restrição na tabela
);

alter table employee 
	add constraint fk_employee 
	foreign key(Super_ssn) references employee(Ssn)
    on delete set null
    on update cascade;

alter table employee modify Dno int not null default 1; -- int = tipo de dados / no null = todos os registros devem ter um valor valido para essa coluna / default 1 indica que se nenhum valor for especificado durante uma operação de inserção, o valor padrão será assumido como 1

desc employee; -- descreve a estrura

create table departament( -- cria a tabela departamento
	Dname varchar(15) not null,
    Dnumber int not null,
    Mgr_ssn char(9) not null,
    Mgr_start_date date, 
    Dept_create_date date,
    constraint chk_date_dept check (Dept_create_date < Mgr_start_date),
    constraint pk_dept primary key (Dnumber),
    constraint unique_name_dept unique(Dname),
    foreign key (Mgr_ssn) references employee(Ssn)
);

-- 'def', 'company_constraints', 'departament_ibfk_1', 'company_constraints', 'departament', 'FOREIGN KEY', 'YES'
-- modificar uma constraint: drop e add

alter table departament drop  departament_ibfk_1;--drop é usado para remover algum objeto
alter table departament 
		add constraint fk_dept foreign key(Mgr_ssn) references employee(Ssn)
        on update cascade;--ON UPDATE CASCADE a uma restrição de chave estrangeira, isso significa que se o valor da coluna referenciada for atualizado na tabela pai, todas as correspondências na tabela filha serão atualizadas automaticamente para refletir essa mudança.

desc departament;

/* ------------------------------------ x ----------------------------------- */

create table dept_locations(
	Dnumber int not null,
	Dlocation varchar(15) not null,
    constraint pk_dept_locations primary key (Dnumber, Dlocation),
    constraint fk_dept_locations foreign key (Dnumber) references departament (Dnumber)
);
alter table dept_locations drop fk_dept_locations;

/* ------------------------------------ x ----------------------------------- */

alter table dept_locations 
	add constraint fk_dept_locations foreign key (Dnumber) references departament(Dnumber)
	on delete cascade
    on update cascade;

create table project(
	Pname varchar(15) not null,
	Pnumber int not null,
    Plocation varchar(15),
    Dnum int not null,
    primary key (Pnumber),
    constraint unique_project unique (Pname),
    constraint fk_project foreign key (Dnum) references departament(Dnumber)
);


create table works_on(
	Essn char(9) not null,
    Pno int not null,
    Hours decimal(3,1) not null,
    primary key (Essn, Pno),
    constraint fk_employee_works_on foreign key (Essn) references employee(Ssn),
    constraint fk_project_works_on foreign key (Pno) references project(Pnumber)
);

drop table dependent;
create table dependent(
	Essn char(9) not null,
    Dependent_name varchar(15) not null,
    Sex char,
    Bdate date,
    Relationship varchar(8),
    primary key (Essn, Dependent_name),
    constraint fk_dependent foreign key (Essn) references employee(Ssn)
);

show tables;
desc dependent;