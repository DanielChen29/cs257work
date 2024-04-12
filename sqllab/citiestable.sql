DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS states;
CREATE TABLE cities (
  City text,
  State text,
  Population real,
  Latitude real,
  Longitude real
);
CREATE TABLE States (
  Code text,
  State text,
  Population real
);