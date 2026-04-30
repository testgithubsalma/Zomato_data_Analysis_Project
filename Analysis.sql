-- View data
SELECT * FROM Zomato_Data_Set LIMIT 10;

-- Average rating by location
SELECT location, AVG(rate) AS avg_rating
FROM zomato_data
GROUP BY location
ORDER BY avg_rating DESC;

-- Top 10 restaurants
SELECT name, rate
FROM zomato_data
ORDER BY rate DESC
LIMIT 10;

-- Most common locations
SELECT location, COUNT(*) AS total
FROM zomato_data
GROUP BY location
ORDER BY total DESC
LIMIT 10;

-- Cost distribution
SELECT "approx_cost(for two people)", COUNT(*) AS total
FROM zomato_data
GROUP BY "approx_cost(for two people)"
ORDER BY total DESC;