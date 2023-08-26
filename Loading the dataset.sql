CREATE DATABASE blackcoffer_data;
USE blackcoffer_data;

CREATE TABLE articles (
    end_year INT DEFAULT NULL,
    intensity INT DEFAULT NULL,
    sector VARCHAR(255),
    topic VARCHAR(255),
    insight VARCHAR(255),
    url TEXT,
    region VARCHAR(255),
    start_year INT DEFAULT NULL,
    impact VARCHAR(50),
    added VARCHAR(255),
    published VARCHAR(255),
    country VARCHAR(255),
    relevance INT,
    pestle VARCHAR(255),
    `source` VARCHAR(255),
    title TEXT,
    likelihood INT DEFAULT NULL
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\updated_data.csv'
INTO TABLE articles
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country, relevance, pestle, `source`, title, likelihood);
SELECT * FROM articles;