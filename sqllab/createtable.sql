DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time,
  latitude real,
  longitude real,
  mag real,
  id text,
  place text
);