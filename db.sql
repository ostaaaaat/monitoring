DROP TABLE climate_data;
CREATE TABLE climate_data (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    co2 FLOAT NOT NULL,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL
);

INSERT INTO climate_data (date, temperature, humidity, co2, latitude, longitude) VALUES
('2024-05-01', 15.0, 55.0, 400.0, 42.858844, 33.294351),
('2024-05-02', 23.0, 54.5, 405.0, 44.052235, 36.243683),
('2024-05-03', 18.0, 60.0, 410.0, 53.507351, 41.127758),
('2024-05-04', 24.0, 50.0, 395.0, 47.712776, 37.005974),
('2024-05-05', 12.0, 45.0, 420.0, 57.689487, 46.691711),
('2024-04-06', 20.0, 70.0, 430.0, 55.868820, 48.209290),
('2024-04-07', 19.0, 65.0, 415.0, 55.755825, 42.617298),
('2024-03-08', 14.0, 55.5, 400.0, 35.904202, 67.407394),
('2024-03-09', 23.0, 50.5, 405.0, 38.550520, 62.633308),
('2024-03-10', 28.0, 53.0, 410.0, 32.774929, 65.419418);

--Вывести все записи со значениями температуры за май
SELECT date, temperature FROM climate_data
WHERE date_trunc('month', date) = '2024-05-01';

--Вывести все записи со значениями влажности по дням
SELECT date, humidity FROM climate_data
ORDER BY date;

--Вывести все записи со значениями CO2 в диапазоне [40.000000; 50.000000] по latitude:
SELECT co2, latitude, longitude FROM climate_data
WHERE latitude BETWEEN 40.000000 AND 50.000000
ORDER BY latitude;
