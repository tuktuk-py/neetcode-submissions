CREATE TABLE products (
    name TEXT not NULL DEFAULT 'Unknown',
    price INTEGER not NULL,
    quantity INTEGER DEFAULT 0
);



-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
