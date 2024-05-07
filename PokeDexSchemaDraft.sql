SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pokedex`
--

-- --------------------------------------------------------

--
-- Table structure for table `evolution`
--

CREATE TABLE `evolution` (
  `EvolutionID` int(11) NOT NULL,
  `PreEvolutionPokemonID` int(11) DEFAULT NULL,
  `PostEvolutionPokemonID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `evolution`
--

INSERT INTO `evolution` (`EvolutionID`, `PreEvolutionPokemonID`, `PostEvolutionPokemonID`) VALUES
(1, 1, 2),
(2, 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pokemon`
--

CREATE TABLE `pokemon` (
  `PokemonID` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Type_1` int(11) DEFAULT NULL,
  `Type_2` int(11) DEFAULT NULL,
  `Species` int(11) DEFAULT NULL,
  `Height` float NOT NULL,
  `Weight` float NOT NULL,
  `Description` varchar(300) NOT NULL,
  `ImagePath` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pokemon`
--

INSERT INTO `pokemon` 
(`PokemonID`, `Name`, `Type_1`, `Type_2`, `Species`, `Height`, `Weight`, `Description`, `ImagePath`) VALUES
(1, 'Bulbasaur', 1, NULL, 1, 0.7, 6.9, 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.', 'C:\\programming\\sie557\\Pokedex_prototype\\sprite_images\\1.png'),
(2, 'Charmander', 2, NULL, 2, 0.6, 8.5, 'Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.', 'C:\\programming\\sie557\\Pokedex_prototype\\sprite_images\\2.png'),
(3, 'Venusaur', 1, NULL, 3, 2.0, 100.0, 'The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.', 'C:\\programming\\sie557\\Pokedex_prototype\\sprite_images\\3.png'),
(4, 'Charizard', 2, 3, 2, 1.7, 90.5, 'Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.', 'C:\\programming\\sie557\\Pokedex_prototype\\sprite_images\\4.png'),
(5, 'Squirtle', 3, NULL, 4, 0.5, 9.0, 'After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth.', 'C:\\programming\\sie557\\Pokedex_prototype\\sprite_images\\5.png');

-- --------------------------------------------------------

--
-- Table structure for table `species`
--

CREATE TABLE `species` (
  `SpeciesID` int(11) NOT NULL,
  `SpeciesName` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `species`
--

INSERT INTO `species` (`SpeciesID`, `SpeciesName`) VALUES
(2, 'Lizard Pokémon'),
(1, 'Seed Pokémon');

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

CREATE TABLE `types` (
  `TypeID` int(11) NOT NULL,
  `TypeName` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `types`
--

INSERT INTO `types` (`TypeID`, `TypeName`) VALUES
(2, 'Fire'),
(1, 'Grass');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserID` int(11) NOT NULL,
  `Username` varchar(45) DEFAULT NULL,
  `Password` varchar(90) DEFAULT NULL,
  `FavoritePokemon` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserID`, `Username`, `Password`, `FavoritePokemon`) VALUES
(1, 'Ash', 'pikachu', 1),
(2, 'Misty', 'starmie', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `evolution`
--
ALTER TABLE `evolution`
  ADD PRIMARY KEY (`EvolutionID`),
  ADD KEY `PreEvolutionPokemonID_idx` (`PreEvolutionPokemonID`),
  ADD KEY `PostEvolutionPokemonID_idx` (`PostEvolutionPokemonID`);

--
-- Indexes for table `pokemon`
--
ALTER TABLE `pokemon`
  ADD PRIMARY KEY (`PokemonID`),
  ADD UNIQUE KEY `Name_UNIQUE` (`Name`),
  ADD KEY `Type_1_ID_idx` (`Type_1`),
  ADD KEY `SpeciesID _idx` (`Species`),
  ADD KEY `Type_2_ID_idx` (`Type_2`);

--
-- Indexes for table `species`
--
ALTER TABLE `species`
  ADD PRIMARY KEY (`SpeciesID`),
  ADD UNIQUE KEY `Species` (`SpeciesName`);

--
-- Indexes for table `types`
--
ALTER TABLE `types`
  ADD PRIMARY KEY (`TypeID`),
  ADD UNIQUE KEY `TypeName` (`TypeName`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`),
  ADD KEY `FavoritePokemon_idx` (`FavoritePokemon`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `evolution`
--
ALTER TABLE `evolution`
  MODIFY `EvolutionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pokemon`
--
ALTER TABLE `pokemon`
  MODIFY `PokemonID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `species`
--
ALTER TABLE `species`
  MODIFY `SpeciesID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `TypeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `evolution`
--
ALTER TABLE `evolution`
  ADD CONSTRAINT `PostEvolutionPokemonID` FOREIGN KEY (`PostEvolutionPokemonID`) REFERENCES `pokemon` (`PokemonID`) ON DELETE SET NULL ON UPDATE NO ACTION,
  ADD CONSTRAINT `PreEvolutionPokemonID` FOREIGN KEY (`PreEvolutionPokemonID`) REFERENCES `pokemon` (`PokemonID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `pokemon`
--
ALTER TABLE `pokemon`
  ADD CONSTRAINT `SpeciesID ` FOREIGN KEY (`Species`) REFERENCES `species` (`SpeciesID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Type_1_ID` FOREIGN KEY (`Type_1`) REFERENCES `types` (`TypeID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Type_2_ID` FOREIGN KEY (`Type_2`) REFERENCES `types` (`TypeID`) ON DELETE SET NULL ON UPDATE NO ACTION;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `FavoritePokemon` FOREIGN KEY (`FavoritePokemon`) REFERENCES `pokemon` (`PokemonID`) ON DELETE SET NULL ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
