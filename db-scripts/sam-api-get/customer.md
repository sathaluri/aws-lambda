```postgresql
  -- DROP SCHEMA loans;

  CREATE SCHEMA loans AUTHORIZATION tinitiate;

  -- DROP TABLE loans.customer;

  CREATE TABLE loans.customer (
      customer_id int4 NOT NULL,
      customer_name varchar(200) NULL,
      application_date date NULL,
      customer_creditscore int4 NULL,
      customer_req_loanamount numeric NULL,
      CONSTRAINT customer_pkey PRIMARY KEY (customer_id)
  );
```
