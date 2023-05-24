```sql
  -- DROP SCHEMA shoppingcart;
  CREATE SCHEMA shoppingcart AUTHORIZATION tinitiate;

  -- DROP TABLE shoppingcart.products;

  CREATE TABLE shoppingcart.products (
    product_id int4 NOT NULL,
    product_category varchar NOT NULL,
    product_name varchar NOT NULL,
    unit_price float8 NULL,
    CONSTRAINT products_pkey PRIMARY KEY (product_id)
);
```
