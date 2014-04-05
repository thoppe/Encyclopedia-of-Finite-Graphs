SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `graph1` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `graph1` ;

-- -----------------------------------------------------
-- Table `graph1`.`graph`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `graph1`.`graph` (
  `graph_id` INT NOT NULL,
  `dual_graph_id` INT NULL,
  `name` VARCHAR(45) NOT NULL DEFAULT 'Untitled graph',
  `isdirected` TINYINT(1) NULL,
  `isconnected` TINYINT(1) NULL,
  `iscomplete` TINYINT(1) NULL,
  `isbipartite` TINYINT(1) NULL,
  `isplanar` TINYINT(1) NULL,
  `istree` TINYINT(1) NULL,
  `nvertices` INT NULL,
  `nedges` INT NULL,
  `diameter` INT NULL,
  `radius` INT NULL,
  `chrom_nbr` INT NULL,
  `rank` INT NULL,
  `max_matching` INT NULL,
  `min_covering` INT NULL,
  `last_updt_ts` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`graph_id`),
  UNIQUE INDEX `idgraph_UNIQUE` (`graph_id` ASC),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `graph1`.`nodes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `graph1`.`nodes` (
  `graph_id` INT NOT NULL,
  `node_nbr` INT NOT NULL,
  `node_degree` INT NULL,
  `node_in_degree` INT NULL,
  `node_out_degree` INT NULL,
  `last_updt_ts` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`graph_id`, `node_nbr`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `graph1`.`edges`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `graph1`.`edges` (
  `graph_id` INT NOT NULL,
  `edge_id` INT NULL,
  `node_nbr` INT NOT NULL,
  `start_end_ind` INT NOT NULL,
  `last_updt_ts` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`edge_id`, `graph_id`, `node_nbr`),
  INDEX `fk_edges_graph_idx` (`graph_id` ASC),
  INDEX `node_nbr` (`node_nbr` ASC),
  INDEX `fk_edges_nodes_idx` (`graph_id` ASC, `node_nbr` ASC),
  CONSTRAINT `fk_edges_graph`
    FOREIGN KEY (`graph_id`)
    REFERENCES `graph1`.`graph` (`graph_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_edges_nodes`
    FOREIGN KEY (`graph_id` , `node_nbr`)
    REFERENCES `graph1`.`nodes` (`graph_id` , `node_nbr`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `graph1`.`connected_components`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `graph1`.`connected_components` (
  `graph_id` INT NOT NULL,
  `component_id` INT NOT NULL,
  `edge_id` INT NULL,
  `last_updt_ts` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`graph_id`, `component_id`),
  INDEX `fk_connected_components_edges_idx` (`graph_id` ASC, `edge_id` ASC),
  CONSTRAINT `fk_connected_components_edges`
    FOREIGN KEY (`graph_id` , `edge_id`)
    REFERENCES `graph1`.`edges` (`graph_id` , `edge_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `graph1`.`ref_invariants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `graph1`.`ref_invariants` (
  `invariant_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `description` BLOB NULL,
  `last_updt_ts` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`invariant_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `graph1`.`draw_nodes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `graph1`.`draw_nodes` (
  `graph_id` INT NOT NULL,
  `node_nbr` INT NOT NULL,
  `xcoord` FLOAT NOT NULL DEFAULT 0,
  `ycoord` FLOAT NOT NULL DEFAULT 0,
  `zcoord` FLOAT NOT NULL DEFAULT 0,
  `last_updt_ts` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`graph_id`, `node_nbr`),
  CONSTRAINT `fk_draw_nodes_nodes`
    FOREIGN KEY (`graph_id` , `node_nbr`)
    REFERENCES `graph1`.`nodes` (`graph_id` , `node_nbr`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

USE `graph1` ;

-- -----------------------------------------------------
-- procedure truncate_insert_nodes
-- -----------------------------------------------------

DELIMITER $$
USE `graph1`$$
CREATE PROCEDURE truncate_insert_nodes () -- refresh the nodes table with the values given in the edges table
BEGIN
truncate nodes; -- clears out all the rows

insert into nodes -- inserts with most up to date nodes
select graph_id, node_nbr
from edges
group by graph_id, edges
;
END$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
