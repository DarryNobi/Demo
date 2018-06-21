#!/usr/bin/env python
# coding:utf-8
# @author: KaiVen
"""
GPS坐标转换：
WGS-84：是国际标准，GPS坐标（Google Earth使用、或者GPS模块）
GCJ-02：中国坐标偏移标准，Google Map、高德、腾讯使用
BD-09：百度坐标偏移标准，Baidu Map使用
"""

import math


def transformLat(x, y):
    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
    ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
    return ret


def transformLon(x, y):
    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
    ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
    return ret


def delta(lat, lng):
    a = 6378245.0
    # a: 卫星椭球坐标投影到平面地图坐标系的投影因子
    ee = 0.00669342162296594323
    # ee: 椭球的偏心率
    dLat = transformLat(lng - 105.0, lat - 35.0)
    dLon = transformLon(lng - 105.0, lat - 35.0)
    radLat = lat / 180.0 * math.pi
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * math.pi)
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi)
    return dLat, dLon


def wgs2gcj(wgsLat, wgsLng):
    """
    WGS-84转成GCJ-02
    """
    if outOfChina(wgsLat, wgsLng):
        print("The latitude or longitude is out of China!")
        return wgsLat, wgsLng
    lat, lng = delta(wgsLat, wgsLng)
    return wgsLat + lat, wgsLng + lng


def gcj2wgs_rough(gcjLat, gcjLon):
    """
    GCJ-02 转 WGS-84 粗略版
    """
    if outOfChina(gcjLat, gcjLon):
        print("The latitude or longitude is out of China!")
        return gcjLat, gcjLon
    lat, lng = delta(gcjLat, gcjLon)
    return gcjLat - lat, gcjLon - lng


def gcj2wgs_accurate(gcjLat, gcjLon):
    """
    GCJ-02 转 WGS-84 精确版
    """
    initDelta = 0.01
    threshold = 0.000000001
    dLat = initDelta
    dLon = initDelta
    mLat = gcjLat - dLat
    mLon = gcjLon - dLon
    pLat = gcjLat + dLat
    pLon = gcjLon + dLon
    wgsLat = 0
    wgsLon = 0
    i = 0
    while 1:
        wgsLat = (mLat + pLat) / 2
        wgsLon = (mLon + pLon) / 2
        lat, lon = gcj2wgs_rough(wgsLat, wgsLon)
        dLat = lat - gcjLat
        dLon = lon - gcjLon
        if (abs(dLat) < threshold) and (abs(dLon) < threshold):
            break
        if dLat > 0:
            pLat = wgsLat
        else:
            mLat = wgsLat
        if dLon > 0:
            pLon = wgsLon
        else:
            mLon = wgsLon
        if ++i > 10000:
            break
    return wgsLat, wgsLon


def gcj2bd(gcjLat, gcjLon):
    """
    GCJ-02 转 BD-09
    """
    x_pi = math.pi * 3000.0 / 180.0
    x = gcjLon
    y = gcjLat
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * x_pi)
    bdLon = z * math.cos(theta) + 0.0065
    bdLat = z * math.sin(theta) + 0.006
    return bdLat, bdLon


def bd2gcj(bdLat, bdLon):
    """
    BD-09 转 GCJ-02
    """
    x_pi = math.pi * 3000.0 / 180.0
    x = bdLon - 0.0065
    y = bdLat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gcjLon = z * math.cos(theta)
    gcjLat = z * math.sin(theta)
    return gcjLat, gcjLon


def wgs2mercator(wgsLat, wgsLon):
    """
    WGS-84 to Web mercator
    mercatorLat -> y mercatorLon -> x
    """
    x = wgsLon * 20037508.34 / 180.
    y = math.log(math.tan((90. + wgsLat) * math.pi / 360)) / (math.pi / 180)
    y = y * 20037508.34 / 180.
    return y, x


def mercator2wgs(mercatorLat, mercatorLon):
    """
    Web mercator to WGS-84
    mercatorLat -> y mercatorLon -> x
    """
    x = mercatorLon / 20037508.34 * 180
    y = mercatorLat / 20037508.34 * 180
    y = 180 / math.pi * (2 * math.atan(math.exp(y * math.pi / 180.)) - math.pi / 2)
    return y, x


def outOfChina(lat, lng):
    """
    判断是否在中国范围外
    """
    if lng < 72.004 or lng > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False


def haversine(lat1, lon1, lat2, lon2):
    """
    :param: 纬度1，经度1，纬度2，经度2（十进制度数）
    :return: 二个坐标之间的距离（单位米）
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000