/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : bus

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2017-12-21 17:32:41
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
  `arrivePlace` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of busarrive
-- ----------------------------
INSERT INTO `busarrive` VALUES ('4', 'BD31B6B6-2455-4655-AD1C-EC7CDF8E6780', '15:12:47', '2017-12-21', '南浜');
INSERT INTO `busarrive` VALUES ('5', 'BD31B6B6-2455-4655-AD1C-EC7CDF8E6780', '16:44:40', '2017-12-21', '南浜');

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
  `needRecordPlace` text,
  `guid` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of recordplace
-- ----------------------------
INSERT INTO `recordplace` VALUES ('1', '吉祥小区东,南浜', 'BD31B6B6-2455-4655-AD1C-EC7CDF8E6780');
INSERT INTO `recordplace` VALUES ('2', '张巷桥', 'A7193AC1-74DF-4770-8208-C5C64FDECC62');
