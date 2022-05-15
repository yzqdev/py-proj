/*
 Navicat Premium Data Transfer

 Source Server         : localpg
 Source Server Type    : PostgreSQL
 Source Server Version : 140002
 Source Host           : localhost:5432
 Source Catalog        : pytodolist
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 140002
 File Encoding         : 65001

 Date: 15/05/2022 23:13:59
*/


-- ----------------------------
-- Table structure for todolist
-- ----------------------------
DROP TABLE IF EXISTS "public"."todolist";
CREATE TABLE "public"."todolist" (
  "id" int4 NOT NULL,
  "user_id" int4 NOT NULL,
  "title" varchar(1024) COLLATE "pg_catalog"."default" NOT NULL,
  "status" int4 NOT NULL,
  "create_time" int4 NOT NULL
)
;
COMMENT ON COLUMN "public"."todolist"."status" IS '是否完成';

-- ----------------------------
-- Records of todolist
-- ----------------------------
INSERT INTO "public"."todolist" VALUES (1, 1, '习近平五谈稳中求进织密扎牢民是犯法第三方生保障网', 0, 1482214350);
INSERT INTO "public"."todolist" VALUES (2, 1, '特朗普获超270张选举人票将入主白 宫', 1, 1482214350);
INSERT INTO "public"."todolist" VALUES (4, 1, '啊啊啊', 1, 1644454997);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "public"."user";
CREATE TABLE "public"."user" (
  "id" int4 NOT NULL,
  "username" varchar(24) COLLATE "pg_catalog"."default",
  "password" varchar(24) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO "public"."user" VALUES (1, 'admin', 'admin');

-- ----------------------------
-- Primary Key structure for table todolist
-- ----------------------------
ALTER TABLE "public"."todolist" ADD CONSTRAINT "todolist_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_pkey" PRIMARY KEY ("id");
