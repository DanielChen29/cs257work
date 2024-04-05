DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate date,
  quaketime time with time zone,
  latitude real,
  longitude real,
  depth real,
  mag real,
  magType text,
  id text,
  nst int,
  gap int,
  dmin real,
  rms real,
  net text,
  id text,
  updated time with time zone,
  place text,
);