DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime timestamp,
  latitude real,
  longitude real,
  mag real,
  id text,
  place text
);