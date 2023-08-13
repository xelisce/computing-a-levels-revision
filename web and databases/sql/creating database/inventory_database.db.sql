BEGIN TRANSACTION;
DROP TABLE IF EXISTS `Product`;
CREATE TABLE IF NOT EXISTS `Product` (
	`ProductCode`	TEXT UNIQUE,
	`Name`	TEXT,
	`Type`	TEXT,
	`Location`	TEXT,
	`Price`	TEXT,
	PRIMARY KEY(`ProductCode`)
);
DROP TABLE IF EXISTS `Loaf`;
CREATE TABLE IF NOT EXISTS `Loaf` (
	`ProductCode`	TEXT,
	`Weight`	TEXT,
	FOREIGN KEY(`ProductCode`) REFERENCES `Product`(`ProductCode`)
);
DROP TABLE IF EXISTS `Cake`;
CREATE TABLE IF NOT EXISTS `Cake` (
	`ProductCode`	TEXT,
	`ServingSize`	TEXT,
	`Shape`	TEXT,
	FOREIGN KEY(`ProductCode`) REFERENCES `Product`(`ProductCode`)
);
DROP TABLE IF EXISTS `Bun`;
CREATE TABLE IF NOT EXISTS `Bun` (
	`ProductCode`	TEXT,
	`PiecesPerPackage`	TEXT,
	FOREIGN KEY(`ProductCode`) REFERENCES `Product`(`ProductCode`)
);
COMMIT;
