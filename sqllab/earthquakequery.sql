-- Find the 10 highest magnitude earthquakes
SELECT * FROM earthquakes ORDER BY magnitude DESC LIMIT 10;

-- Find all earthquakes that occurred on January 27th in Hawaii
SELECT * FROM earthquakes WHERE DATE(quaketime) = '2023-01-27' AND place LIKE '%Hawaii%';

-- Find all earthquakes below the equator
SELECT * FROM earthquakes WHERE latitude < 0;