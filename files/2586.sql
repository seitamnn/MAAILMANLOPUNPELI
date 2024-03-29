-- Changes in the database

use flight_game;

-- Delete all airports but large_airport
DELETE FROM airport WHERE type='seaplane_base';
DELETE FROM airport WHERE type='closed';
DELETE FROM airport WHERE type='heliport';
DELETE FROM airport WHERE type='small_airport';
DELETE FROM airport WHERE type='medium_airport';
DELETE FROM airport WHERE type='balloonport';

-- Remove columns from game table
ALTER TABLE game DROP COLUMN co2_consumed, DROP COLUMN co2_budget;

-- Add columns to game table
ALTER TABLE game ADD COLUMN currency INT, ADD COLUMN alien_distance INT, ADD COLUMN in_possession BOOLEAN;

-- From Norway & Cuba remove all but Oslo & Jose Marti airports

-- Norway
DELETE FROM airport WHERE ident = 'ENBR';
DELETE FROM airport WHERE ident = 'ENTC';
DELETE FROM airport WHERE ident = 'ENVA';
DELETE FROM airport WHERE ident = 'ENZV';
-- Cuba
DELETE FROM airport WHERE ident = 'MUVR';
