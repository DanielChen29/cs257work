DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  time timestamp with time zone,
  latitude real,
  longitude real,
  mag real,
  id text,
  place text
);