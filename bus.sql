/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : bus

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2017-12-20 17:41:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `busarrive`
-- ----------------------------
DROP TABLE IF EXISTS `busarrive`;
CREATE TABLE `busarrive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `busGuid` varchar(64) DEFAULT NULL,
  `arrivetime` time DEFAULT NULL,
  `arriveDay` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of busarrive
-- ----------------------------

-- ----------------------------
-- Table structure for `businfo`
-- ----------------------------
DROP TABLE IF EXISTS `businfo`;
CREATE TABLE `businfo` (
  `guid` varchar(64) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `arrivePlace` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`guid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of businfo
-- ----------------------------

-- ----------------------------
-- Table structure for `recordplace`
-- ----------------------------
DROP TABLE IF EXISTS `recordplace`;
CREATE TABLE `recordplace` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `needRecordPlace` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of recordplace
-- ----------------------------
