# #save image in mysql
# from web.models import Map
# import os
# import time
# import re
# def saveImageBack(filepath):
#
#      listProperty = ['SatelliteID', 'Maptype', 'SensorID', 'ReceiveTime', 'name',
#                      'Band', 'WidthInPixels', 'HeightInPixels', 'EarthEllipsoid', 'TopLeftLatitude',
#                      'TopLeftLongitude', 'TopRightLatitude', 'TopRightLongitude', 'BottomRightLatitude','BottomRightLongitude',
#                      'BottomLeftLatitude', 'BottomLeftLongitude', 'filepath', 'cut_row', 'cut_col',
#                      'gen_date', 'folder', 'isPublish', 'ProductLevel','GlobeID','ImageDesc']
#
#      def readXML(xml, dic):
#          info = open(xml, 'r')
#          infoLine = info.readline()
#          while (len(dic) != len(listProperty)):
#              propertyKey = infoLine[infoLine.find('<') + 1:infoLine.find('>')]
#              propertyValue = infoLine[infoLine.find('>') + 1:infoLine.find('</')]
#              if (propertyKey in listProperty):
#                  if (propertyKey != 'ReceiveTime'):
#                      dic[propertyKey] = propertyValue
#                  else:
#                      dic[propertyKey] = propertyValue[:propertyValue.find(" ")]
#              infoLine = info.readline()
#          image = Map.objects.create(SatelliteID=dic['SatelliteID'], Maptype=dic['Maptype'], SensorID=dic['SensorID'],
#                                     ReceiveTime=dic['ReceiveTime'], name=dic['name'],
#                                     Bands=dic['Bands'], WidthInPixels=dic['WidthInPixels'],
#                                     HeightInPixels=dic['HeightInPixels'], EarthEllipsoid=dic['EarthEllipsoid'],
#                                     TopLeftLatitude=dic['TopLeftLatitude'], TopLeftLongitude=dic['TopLeftLongitude'],
#                                     TopRightLatitude=dic['TopRightLatitude'], TopRightLongitude=dic['TopRightLongitude'],
#                                     BottomRightLatitude=dic['BottomRightLatitude'],
#                                     BottomRightLongitude=dic['BottomRightLongitude'],
#                                     BottomLeftLatitude=dic['BottomLeftLatitude'],
#                                     BottomLeftLongitude=dic['BottomLeftLongitude'], filepath=dic['filepath'],
#                                     cut_row=dic['cut_row'], cut_col=dic['cut_col'], gen_date=dic['gen_date'],
#                                     folder=dic['folder'], isPublish=dic['isPublish'], ProductLevel=dic['ProductLevel'])
#          image.save()
#          info.close()
#
#
#      def travase(f):
#          dicProperty = {}
#          fs = os.listdir(f)
#          for f1 in fs:
#              tmp_path = os.path.join(f, f1)
#              if not os.path.isdir(tmp_path):
#                  if re.search(r'MSS\d.tif',tmp_path) and not re.search('txt',tmp_path):
#                      if (Map.objects.filter(name=f1).count() == 0):
#                          xml = os.path.join(os.path.dirname(tmp_path), (os.path.basename(tmp_path)
#                                                                         [:os.path.basename(tmp_path).find(
#                              "tif")] + "xml"))
#                          dicProperty['name'] = f1
#                          dicProperty['filepath'] = tmp_path
#                          dicProperty['folder'] = f
#                          dicProperty['gen_date'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#                          dicProperty['Maptype'] = '多光谱'
#                          dicProperty['Bands'] = 4
#                          dicProperty['cut_row'] = 512
#                          dicProperty['cut_col'] = 512
#                          dicProperty['isPublish'] = False
#                          dicProperty['GlobeID']=0
#                          dicProperty['ImageDesc']='Describe this Image'
#                          dicProperty['IsUnit8']=False
#
#                          readXML(xml, dicProperty)
#                          dicProperty = {}
#                  elif re.search(r'PAN\d.tif',tmp_path) and not re.search('txt',tmp_path):
#                      if (Map.objects.filter(name=f1).count() == 0):
#                          xml = os.path.join(os.path.dirname(tmp_path), (os.path.basename(tmp_path)
#                                                                         [:os.path.basename(tmp_path).find(
#                              "tif")] + "xml"))
#                          dicProperty['name'] = f1
#                          dicProperty['filepath'] = tmp_path
#                          dicProperty['folder'] = f
#                          dicProperty['gen_date'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#                          dicProperty['Maptype'] = '全色彩'
#                          dicProperty['Bands'] = 1
#                          dicProperty['cut_row'] = 512
#                          dicProperty['cut_col'] = 512
#                          dicProperty['isPublish'] = False
#                          dicProperty['GlobeID'] = 0
#                          dicProperty['ImageDesc'] = 'Describe this Image'
#                          dicProperty['IsUnit8'] = False
#
#                          readXML(xml, dicProperty)
#                          dicProperty = {}
#                  elif re.search('_fusion.tif',tmp_path) :
#                      if (Map.objects.filter(name=f1).count() == 0):
#                          baseName = os.path.basename(tmp_path)[
#                                     :os.path.basename(tmp_path).find("_fusion")] + ".xml"
#                          xml = os.path.join(os.path.dirname(tmp_path), baseName.replace('MSS', 'PAN'))
#                          dicProperty['name'] = f1
#                          dicProperty['filepath'] = tmp_path
#                          dicProperty['folder'] = f
#                          dicProperty['gen_date'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#                          dicProperty['Maptype'] = '融合'
#                          dicProperty['Bands'] = 4
#                          dicProperty['cut_row'] = 512
#                          dicProperty['cut_col'] = 512
#                          dicProperty['isPublish'] = False
#                          dicProperty['GlobeID'] = 0
#                          dicProperty['ImageDesc'] = 'Describe this Image'
#                          dicProperty['IsUnit8'] = False
#
#                          readXML(xml, dicProperty)
#                          dicProperty = {}
#              else:
#                  travase(tmp_path)
#      travase(filepath)