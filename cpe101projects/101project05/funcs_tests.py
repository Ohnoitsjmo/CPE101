# Project 5 - Earthquakes
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17 
import unittest
import quake_funcs

class TestCases(unittest.TestCase):
   def test_output_0(self):
      quake
   def test_earthquake_init(self):
      quake = quake_funcs.Earthquake("12km SSW of Idyllwild, CA", 0.97,
                                     -116.7551651, 33.6391678, 1488177290)
      self.assertEqual(quake.place, "12km SSW of Idyllwild, CA")
      self.assertAlmostEqual(quake.mag, 0.97)
      self.assertAlmostEqual(quake.longitude, -116.7551651)
      self.assertAlmostEqual(quake.latitude, 33.6391678)
      self.assertEqual(quake.time, 1488177290)

   def test_earthquake_init2(self):
      quake = quake_funcs.Earthquake("14km SSE of Cupertino, CA", 1.1, -173.4234, 24.234523, 193029402)
      self.assertEqual(quake.place, "14km SSE of Cupertino, CA")
      self.assertAlmostEqual(quake.mag, 1.1)
      self.assertAlmostEqual(quake.longitude, -173.4234)
      self.assertAlmostEqual(quake.latitude, 24.234523)
      self.assertEqual(quake.time, 193029402)

   def test_earthquakes_equal_0(self):
      quake1 = quake_funcs.Earthquake("12km SSW of Idyllwild, CA", 0.97,
                                      -116.7551651, 33.6391678, 1488177290)
      quake2 = quake_funcs.Earthquake("12km SSW of Idyllwild, CA", 0.97,
                                      -116.7551651, 33.6391678, 1488177290)
      self.assertEqual(quake1, quake2)

   def test_earthquakes_equal_1(self):
      quake1 = quake_funcs.Earthquake("12km SSW of Idyllwild, CA", 0.97,
                                      -116.7551651, 33.6391678, 1488177290)
      quake2 = quake_funcs.Earthquake("13km SSW of Idyllwild, CA", 0.97,
                                      -116.7551651, 33.6391678, 1488177290)
      self.assertNotEqual(quake1, quake2)

   def test_earthquakes_equal_3(self):
      quake1 = quake_funcs.Earthquake("14km SSE of Cupertino, CA", 0.97,
                                      -127.84234, 37.55556, 73273273)
      quake2 = quake_funcs.Earthquake("14km SSE of Cupertino, CA", 0.97,
                                      -127.84234, 37.55556, 73273273)
      self.assertEqual(quake1, quake2)

   def test_earthquakes_equal_4(self):
      quake1 = quake_funcs.Earthquake("12km SSW o Idyllwild, CA", 0.97,
                                      -116.755151, 33.6391678, 1488177290)
      quake2 = quake_funcs.Earthquake("13km SSWof Idyllwild, CA", 0.97,
                                      -116.7551651, 3.691678, 1488177290)
      self.assertNotEqual(quake1, quake2)

   def test_read_file_0(self):
      quakes = []
      quakes.append(quake_funcs.Earthquake("12km SSW of Idyllwild, CA", 0.97,
                                           -116.7551651, 33.6391678,
                                           1488177290))
      quakes.append(quake_funcs.Earthquake("5km S of Gilroy, California", 2.19,
                                           -121.5801697, 36.9580002,
                                           1488173538))
      self.assertEqual(quake_funcs.read_quakes_from_file("test0.txt"), quakes)
   
 
   def test_read_file_1(self):
      quakes = []
      quakes.append(quake_funcs.Earthquake("12km SSW of Idyllwild, CA", 0.97,
                                           -116.7551651, 33.6391678,
                                           1488177290))
      quakes.append(quake_funcs.Earthquake("5km S of Gilroy, California", 2.19,
                                           -121.5801697, 36.9580002,
                                           1488173538))
      self.assertEqual(quake_funcs.read_quakes_from_file("test0.txt"), quakes)

   def test_read_file_2(self):
      quakes = []
      quakes.append(quake_funcs.Earthquake("132km SSW of Idyllwild, CA", 0.97,
                                           -116.7551651, 33.6391678,
                                           1488177290))
      quakes.append(quake_funcs.Earthquake("5km S of Gilroy, California", 2.19,
                                           -121.5801697, 36.9580002,
                                           1488173538))
      self.assertNotEqual(quake_funcs.read_quakes_from_file("test0.txt"), quakes) 
   
   def test_read_file_3(self):
      quakes = []
      quakes.append(quake_funcs.Earthquake("77km SSW of Idyllwild, CA", 0.97,
                                           -12346.75231651, 33.6391678,
                                           14823477290))
      quakes.append(quake_funcs.Earthquake("5ksm S of Gilroy, California", 2.19,
                                           -121.5801697, 36.9580002,
                                           1488173538))
      self.assertNotEqual(quake_funcs.read_quakes_from_file("test0.txt"), quakes)

   # Use this test when ready to work on the json data.
   def test_quake_from_feature(self):
      feature = [{
          "geometry": {
              "coordinates": [
                  -117.4906667,
                  33.9131667,
                  0.25
              ],
              "type": "Point"
          },
          "id": "ci37814000",
          "properties": {
              "code": "37814000",
              "detail": "http://earthquake.usgs.gov/earthquakes/feed/v1.0"
                        "/detail/ci37814000.geojson",
              "dmin": 0.2836,
              "gap": 87,
              "ids": ",ci37814000,",
              "mag": 1.24,
              "magType": "ml",
              "net": "ci",
              "nst": 8,
              "place": "5km NE of Home Gardens, CA",
              "rms": 0.27,
              "sig": 24,
              "sources": ",ci,",
              "status": "automatic",
              "time": 1488179250520,
              "title": "M 1.2 - 5km NE of Home Gardens, CA",
              "tsunami": 0,
              "type": "earthquake",
              "types": ",geoserve,nearby-cities,origin,phase-data,"
                       "scitech-link,",
              "tz": -480,
              "updated": 1488179487273,
              "url": "http://earthquake.usgs.gov/earthquakes/eventpage/"
                     "ci37814000"
          },
          "type": "Feature"
      }]                                                           
      quake1 = quake_funcs.quake_from_feature(feature)
      quake2 = "1.24 -117.4906667 33.9131667 1488179250 5km NE of Home Gardens, CA\n"
      self.assertEqual(quake1, quake2)
   

   def test_quake_from_feature_1(self):
      feature = [{
          "geometry": {
              "coordinates": [
                  -127.3223349,
                  34.9131667,
                  0.25
              ],
              "type": "Point"
          },
          "id": "ci37814000",
          "properties": {
              "code": "37814000",
              "detail": "http://earthquake.usgs.gov/earthquakes/feed/v1.0"
                        "/detail/ci37814000.geojson",
              "dmin": 0.2836,
              "gap": 87,
              "ids": ",ci37814000,",
              "mag": 2.25,
              "magType": "ml",
              "net": "ci",
              "nst": 8,
              "place": "55km NS of Cupertino, CA",
              "rms": 0.27,
              "sig": 24,
              "sources": ",ci,",
              "status": "automatic",
              "time": 1488179250520,
              "title": "M 1.2 - 5km NE of Home Gardens, CA",
              "tsunami": 0,
              "type": "earthquake",
              "types": ",geoserve,nearby-cities,origin,phase-data,"
                       "scitech-link,",
              "tz": -480,
              "updated": 1488179487273,
              "url": "http://earthquake.usgs.gov/earthquakes/eventpage/"
                     "ci37814000"
          },
          "type": "Feature"
      }]
      quake1 = quake_funcs.quake_from_feature(feature)
      quake2 = "2.25 -127.3223349 34.9131667 1488179250 55km NS of Cupertino, CA\n"
      self.assertEqual(quake1, quake2)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
