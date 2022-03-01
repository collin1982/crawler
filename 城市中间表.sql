/*
 Navicat Premium Data Transfer

 Source Server         : MySQL8
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3307
 Source Schema         : house

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 01/03/2022 15:19:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 城市中间表
-- ----------------------------
DROP TABLE IF EXISTS `城市中间表`;
CREATE TABLE `城市中间表`  (
  `省份` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `城市` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `城市主键` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `城市链接` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `当前信息获取时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `当前城市下属区域是否已获取` int NOT NULL,
  PRIMARY KEY (`城市主键`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 城市中间表
-- ----------------------------
INSERT INTO `城市中间表` VALUES ('安徽', '安庆', 'aq', 'https://aq.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('陕西', '宝鸡', 'baoji', 'https://baoji.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('内蒙古', '包头', 'baotou', 'https://baotou.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('河北', '保定', 'bd', 'https://bd.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('广西', '北海', 'bh', 'https://bh.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('北京', '北京', 'bj', 'https://bj.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('海南', '保亭', 'bt.fang', 'https://bt.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('内蒙古', '巴彦淖尔', 'byne.fang', 'https://byne.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('吉林', '长春', 'cc', 'https://cc.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('四川', '成都', 'cd', 'https://cd.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('内蒙古', '赤峰', 'cf', 'https://cf.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('湖南', '常德', 'changde', 'https://changde.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '常熟', 'changshu', 'https://changshu.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '常州', 'changzhou', 'https://changzhou.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('河北', '承德', 'chengde', 'https://chengde.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('海南', '澄迈', 'cm', 'https://cm.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('重庆', '重庆', 'cq', 'https://cq.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('湖南', '长沙', 'cs', 'https://cs.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('安徽', '滁州', 'cz.fang', 'https://cz.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('云南', '大理', 'dali', 'https://dali.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '丹阳', 'danyang', 'https://danyang.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('四川', '达州', 'dazhou', 'https://dazhou.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('辽宁', '丹东', 'dd', 'https://dd.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('广东', '东莞', 'dg', 'https://dg.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('辽宁', '大连', 'dl', 'https://dl.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('四川', '德阳', 'dy', 'https://dy.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('海南', '儋州', 'dz.fang', 'https://dz.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('湖北', '鄂州', 'ez', 'https://ez.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('广西', '防城港', 'fcg', 'https://fcg.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('广东', '佛山', 'fs', 'https://fs.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('辽宁', '抚顺', 'fushun', 'https://fushun.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('安徽', '阜阳', 'fy', 'https://fy.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('福建', '福州', 'fz', 'https://fz.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('江西', '赣州', 'ganzhou', 'https://ganzhou.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('广西', '桂林', 'gl', 'https://gl.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('四川', '广元', 'guangyuan', 'https://guangyuan.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('贵州', '贵阳', 'gy', 'https://gy.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('广东', '广州', 'gz', 'https://gz.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '淮安', 'ha', 'https://ha.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '海门', 'haimen', 'https://haimen.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('陕西', '汉中', 'hanzhong', 'https://hanzhong.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('河北', '邯郸', 'hd', 'https://hd.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('山东', '菏泽', 'heze', 'https://heze.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('安徽', '合肥', 'hf', 'https://hf.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('内蒙古', '呼和浩特', 'hhht', 'https://hhht.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('海南', '海口', 'hk', 'https://hk.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('黑龙江', '哈尔滨', 'hrb', 'https://hrb.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('湖北', '黄石', 'huangshi', 'https://huangshi.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('广东', '惠州', 'hui', 'https://hui.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '湖州', 'huzhou', 'https://huzhou.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '杭州', 'hz', 'https://hz.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '金华', 'jh', 'https://jh.lianjia.com/ershoufang/', '2022-02-23 17:33:12', 0);
INSERT INTO `城市中间表` VALUES ('江西', '吉安', 'jian', 'https://jian.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('广东', '江门', 'jiangmen', 'https://jiangmen.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('山东', '济宁', 'jining', 'https://jining.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('江西', '九江', 'jiujiang', 'https://jiujiang.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('河南', '济源', 'jiyuan.fang', 'https://jiyuan.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('吉林', '吉林', 'jl', 'https://jl.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('山东', '济南', 'jn', 'https://jn.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '句容', 'jr', 'https://jr.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '嘉兴', 'jx', 'https://jx.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '江阴', 'jy', 'https://jy.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('山西', '晋中', 'jz', 'https://jz.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('河南', '开封', 'kf', 'https://kf.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('云南', '昆明', 'km', 'https://km.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '昆山', 'ks', 'https://ks.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('海南', '乐东', 'ld.fang', 'https://ld.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('四川', '乐山', 'leshan.fang', 'https://leshan.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('河北', '廊坊', 'lf', 'https://lf.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('海南', '临高', 'lg.fang', 'https://lg.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('四川', '凉山', 'liangshan', 'https://liangshan.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('山东', '临沂', 'linyi', 'https://linyi.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('广西', '柳州', 'liuzhou', 'https://liuzhou.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('海南', '陵水', 'ls.fang', 'https://ls.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('河南', '洛阳', 'luoyang', 'https://luoyang.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('甘肃', '兰州', 'lz', 'https://lz.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('安徽', '马鞍山', 'mas', 'https://mas.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('四川', '绵阳', 'mianyang', 'https://mianyang.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('四川', '眉山', 'ms.fang', 'https://ms.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('四川', '南充', 'nanchong', 'https://nanchong.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '宁波', 'nb', 'https://nb.lianjia.com/ershoufang/', '2022-02-23 17:33:12', 0);
INSERT INTO `城市中间表` VALUES ('江西', '南昌', 'nc', 'https://nc.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '南京', 'nj', 'https://nj.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('广西', '南宁', 'nn', 'https://nn.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '南通', 'nt', 'https://nt.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('河南', '平顶山', 'pds', 'https://pds.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('河南', '濮阳', 'py', 'https://py.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('四川', '攀枝花', 'pzh', 'https://pzh.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('山东', '青岛', 'qd', 'https://qd.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('海南', '琼海', 'qh.fang', 'https://qh.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('河北', '秦皇岛', 'qhd.fang', 'https://qhd.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('福建', '泉州', 'quanzhou', 'https://quanzhou.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '衢州', 'quzhou', 'https://quzhou.lianjia.com/ershoufang/', '2022-02-23 17:33:12', 0);
INSERT INTO `城市中间表` VALUES ('贵州', '黔西南', 'qxn.fang', 'https://qxn.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('广东', '清远', 'qy', 'https://qy.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('海南', '三亚', 'san', 'https://san.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('上海', '上海', 'sh', 'https://sh.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('河北', '石家庄', 'sjz', 'https://sjz.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('河南', '三门峡', 'smx.fang', 'https://smx.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('四川', '遂宁', 'sn', 'https://sn.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('江西', '上饶', 'sr', 'https://sr.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '苏州', 'su', 'https://su.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '绍兴', 'sx', 'https://sx.lianjia.com/ershoufang/', '2022-02-23 17:33:12', 0);
INSERT INTO `城市中间表` VALUES ('辽宁', '沈阳', 'sy', 'https://sy.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('广东', '深圳', 'sz', 'https://sz.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('山东', '泰安', 'ta', 'https://ta.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '太仓', 'taicang', 'https://taicang.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '台州', 'taizhou', 'https://taizhou.lianjia.com/ershoufang/', '2022-02-23 17:33:12', 0);
INSERT INTO `城市中间表` VALUES ('甘肃', '天水', 'tianshui', 'https://tianshui.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('天津', '天津', 'tj', 'https://tj.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('内蒙古', '通辽', 'tongliao', 'https://tongliao.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('河北', '唐山', 'ts', 'https://ts.lianjia.com/ershoufang/', '2022-02-23 17:33:03', 0);
INSERT INTO `城市中间表` VALUES ('山西', '太原', 'ty', 'https://ty.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('海南', '文昌', 'wc.fang', 'https://wc.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('山东', '威海', 'weihai', 'https://weihai.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('山东', '潍坊', 'wf', 'https://wf.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('湖北', '武汉', 'wh', 'https://wh.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('新疆', '乌鲁木齐', 'wlmq', 'https://wlmq.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('海南', '万宁', 'wn.fang', 'https://wn.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('安徽', '芜湖', 'wuhu', 'https://wuhu.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '无锡', 'wx', 'https://wx.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '温州', 'wz', 'https://wz.lianjia.com/ershoufang/', '2022-02-23 17:33:12', 0);
INSERT INTO `城市中间表` VALUES ('海南', '五指山', 'wzs.fang', 'https://wzs.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('陕西', '西安', 'xa', 'https://xa.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('河南', '许昌', 'xc', 'https://xc.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('陕西', '咸阳', 'xianyang', 'https://xianyang.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('河南', '新乡', 'xinxiang', 'https://xinxiang.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('福建', '厦门', 'xm', 'https://xm.lianjia.com/ershoufang/', '2022-02-23 17:33:01', 0);
INSERT INTO `城市中间表` VALUES ('云南', '西双版纳', 'xsbn.fang', 'https://xsbn.fang.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('湖南', '湘西', 'xx', 'https://xx.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('湖北', '襄阳', 'xy', 'https://xy.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '徐州', 'xz', 'https://xz.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('四川', '雅安', 'yaan', 'https://yaan.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '盐城', 'yc', 'https://yc.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('四川', '宜宾', 'yibin', 'https://yibin.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('湖北', '宜昌', 'yichang', 'https://yichang.lianjia.com/ershoufang/', '2022-02-23 17:33:06', 0);
INSERT INTO `城市中间表` VALUES ('宁夏', '银川', 'yinchuan', 'https://yinchuan.lianjia.com/ershoufang/', '2022-02-23 17:33:08', 0);
INSERT INTO `城市中间表` VALUES ('山东', '烟台', 'yt', 'https://yt.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('山西', '运城', 'yuncheng', 'https://yuncheng.lianjia.com/ershoufang/', '2022-02-23 17:33:11', 0);
INSERT INTO `城市中间表` VALUES ('浙江', '义乌', 'yw', 'https://yw.lianjia.com/ershoufang/', '2022-02-23 17:33:12', 0);
INSERT INTO `城市中间表` VALUES ('湖南', '岳阳', 'yy', 'https://yy.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('山东', '淄博', 'zb', 'https://zb.lianjia.com/ershoufang/', '2022-02-23 17:33:09', 0);
INSERT INTO `城市中间表` VALUES ('广东', '珠海', 'zh', 'https://zh.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('福建', '漳州', 'zhangzhou', 'https://zhangzhou.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('广东', '湛江', 'zhanjiang', 'https://zhanjiang.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('湖南', '株洲', 'zhuzhou', 'https://zhuzhou.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('四川', '资阳', 'ziyang', 'https://ziyang.lianjia.com/ershoufang/', '2022-02-23 17:33:10', 0);
INSERT INTO `城市中间表` VALUES ('江苏', '镇江', 'zj', 'https://zj.lianjia.com/ershoufang/', '2022-02-23 17:33:07', 0);
INSERT INTO `城市中间表` VALUES ('河北', '张家口', 'zjk', 'https://zjk.lianjia.com/ershoufang/', '2022-02-23 17:33:04', 0);
INSERT INTO `城市中间表` VALUES ('河南', '周口', 'zk', 'https://zk.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('河南', '驻马店', 'zmd', 'https://zmd.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);
INSERT INTO `城市中间表` VALUES ('广东', '中山', 'zs', 'https://zs.lianjia.com/ershoufang/', '2022-02-23 17:33:02', 0);
INSERT INTO `城市中间表` VALUES ('河南', '郑州', 'zz', 'https://zz.lianjia.com/ershoufang/', '2022-02-23 17:33:05', 0);

SET FOREIGN_KEY_CHECKS = 1;
