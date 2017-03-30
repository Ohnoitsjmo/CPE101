# Project 5 - Earthquakes
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17 
from urllib.request import urlopen
from json import loads
import json
from datetime import datetime
import operator
import math

# GIVEN FUNCTIONS: Use these two as-is and do not change them
def get_json(url):
   """Function to get a JSON dictionary from a website.

   Args:
      url (str): The url from which to get the JSON

   Returns:
      A Python dictionary containing the information from the JSON object
   """
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   """Converts integer seconds since unix epoch to a string.

   Args:
      time (int): Unix time

   Returns:
      A nicely formated time string
   """
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

# TODO: Add Earthquake class definition here
class Earthquake: 
   def __init__(self, place, mag, longitude, latitude, time):
      self.place = str(place)
      self.mag = float(mag)
      self.longitude = float(longitude)
      self.latitude = float(latitude)
      self.time = int(time)

   def __eq__(self, other):
      return self.place == other.place and self.mag == other.mag and self.longitude == other.longitude and self.latitude == other.latitude and self.time == other.time

#TODO: Required function - implement me!
def read_quakes_from_file(filename):
   txt_file = open(filename, "r")
   lines = txt_file.readlines()
   res = []
   for line in lines:
     attribute = line.split() 
     place_holder = (str(attribute[4]), str(attribute[5]), str(attribute[6]), str(attribute[7]), str(attribute[8]))
     place = ' '.join(place_holder)
     mag = float(attribute[0])
     longitude = float(attribute[1])   
     latitude = float(attribute[2])
     time = int(attribute[3])
     res.append(Earthquake(place, mag, longitude, latitude, time))
   txt_file.close()
   return res
   
def output(filename):
   txt_file = open(filename, "r")   
   lines = txt_file.readlines()
   res = []
   print("")
   print("Earthquakes:")
   print("------------")
   for line in lines:
      attribute = line.split()
      res.append(attribute)
   for each_list in res:
      attribute = ' '.join(each_list).split()
      place_holder = list(attribute[4:])
      place = ' '.join(place_holder)
      mag = float(attribute[0])
      longitude = float(attribute[1])
      latitude = float(attribute[2])
      time = int(attribute[3])
      print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))   
   print("")
   print("Options:")
   print("  (s)ort")
   print("  (f)ilter")
   print("  (n)ew quakes")
   print("  (q)uit")

def program_options(filename):
   quakes_dict = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
   feature = quakes_dict["features"]
   txt_file = open(filename, "r")
   lines = txt_file.readlines()
   res = []
   for line in lines:
      attribute = line.split()
      res.append(attribute)
   print("")
   user_input = str(input("Choice: "))
   while user_input != 'q' and user_input != 'Q':
      if user_input == 'n' or user_input == 'N': 
         final_res = []
         new_quakes = quake_from_feature(feature)
         txt_file = open(filename, "a")
         if new_quakes not in open(filename).read():      
            print("")
            print("New quakes found!!!")
            txt_file.write("{:s}".format(new_quakes))
         txt_file = open(filename, "r")
         lines = txt_file.readlines()
         res = []
         print("")
         print("Earthquakes:")
         print("------------")
         for line in lines:
            attribute = line.split()
            res.append(attribute)
         for each_list in res:
            attribute = ' '.join(each_list).split()
            place_holder = list(attribute[4:])
            place = ' '.join(place_holder)
            mag = float(attribute[0])  
            longitude = float(attribute[1])
            latitude = float(attribute[2])
            time = int(attribute[3])
            print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude)) 
         print("")
         print("Options:")
         print("  (s)ort")
         print("  (f)ilter")
         print("  (n)ew quakes")
         print("  (q)uit")
         print("")
         user_input = str(input("Choice: "))
      if user_input == 's' or user_input == 'S':
         sort_input = str(input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? "))
         if sort_input == 'm' or sort_input == 'M':
            txt_file = open(filename, "r")
            lines = txt_file.readlines()
            res = []
            print("")
            print("Earthquakes:")
            print("------------")
            for line in lines:
               attribute = line.split()
               res.append(attribute)
            res.sort(key=lambda x: float(x[0]), reverse = True)  
            for each_list in res:
               attribute = ' '.join(each_list).split()
               place_holder = list(attribute[4:])
               place = ' '.join(place_holder)
               mag = float(attribute[0])
               longitude = float(attribute[1])
               latitude = float(attribute[2])
               time = int(attribute[3])
               print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
            print("")
            print("Options:")
            print("  (s)ort")
            print("  (f)ilter")
            print("  (n)ew quakes")
            print("  (q)uit")
            print("")
            user_input = str(input("Choice: "))
            if user_input == 'f' or user_input == 'F':
               filter_input = str(input("Filter by (m)agnitude or (p)lace? "))
               if filter_input == 'm' or filter_input == 'M':
                  low = float(input("Lower bound: "))
                  high = float(input("Upper bound: "))
                  print("")
                  print("Earthquakes:")
                  print("------------")
                  filtered_mag = filter_by_mag(res, low, high)
                  for each_list in filtered_mag:
                     attribute = ' '.join(each_list).split()
                     place_holder = list(attribute[4:])
                     place = ' '.join(place_holder)
                     mag = float(attribute[0])
                     longitude = float(attribute[1])
                     latitude = float(attribute[2])
                     time = int(attribute[3])
                     print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
                  print("")
                  print("Options:")
                  print("  (s)ort")
                  print("  (f)ilter")
                  print("  (n)ew quakes")
                  print("  (q)uit")
                  print("")
                  user_input = str(input("Choice: "))
                  continue
               if filter_input == 'p' or filter_input == 'P':
                  word = str(input("Search for what string? "))
                  print("")
                  print("Earthquakes:")
                  print("------------")
                  filtered_place = filter_by_place(res, word)
                  for each_list in filtered_place:
                     attribute = ' '.join(each_list).split()
                     place_holder = list(attribute[4:])
                     place = ' '.join(place_holder)
                     mag = float(attribute[0])
                     longitude = float(attribute[1])
                     latitude = float(attribute[2])
                     time = int(attribute[3])
                     print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
                  print("")
                  print("Options:")
                  print("  (s)ort")
                  print("  (f)ilter")
                  print("  (n)ew quakes")
                  print("  (q)uit")
                  print("") 
                  user_input = str(input("Choice: "))
                  continue
         if sort_input == 't' or sort_input == 'T':
            txt_file = open(filename, "r")
            lines = txt_file.readlines()
            res = []
            print("")
            print("Earthquakes:")
            print("------------")
            for line in lines:
               attribute = line.split()
               res.append(attribute)
            res.sort(key=lambda x: int(x[3]), reverse = True)
            for each_list in res:
               attribute = ' '.join(each_list).split()
               place_holder = list(attribute[4:])
               place = ' '.join(place_holder)
               mag = float(attribute[0])
               longitude = float(attribute[1])
               latitude = float(attribute[2])
               time = int(attribute[3])
               print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
            print("")
            print("Options:")
            print("  (s)ort")
            print("  (f)ilter")
            print("  (n)ew quakes")
            print("  (q)uit") 
            print("")
            user_input = str(input("Choice: "))
            if user_input == 'f' or user_input == 'F':
               filter_input = str(input("Filter by (m)agnitude or (p)lace? "))
               if filter_input == 'm' or filter_input == 'M':
                  low = float(input("Lower bound: "))
                  high = float(input("Upper bound: "))
                  print("")
                  print("Earthquakes:")
                  print("------------")
                  filtered_mag = filter_by_mag(res, low, high)
                  for each_list in filtered_mag:
                     attribute = ' '.join(each_list).split()
                     place_holder = list(attribute[4:])
                     place = ' '.join(place_holder)
                     mag = float(attribute[0])
                     longitude = float(attribute[1])
                     latitude = float(attribute[2])
                     time = int(attribute[3])
                     print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
                  print("")
                  print("Options:")
                  print("  (s)ort")
                  print("  (f)ilter")
                  print("  (n)ew quakes")
                  print("  (q)uit")
                  print("")
                  user_input = str(input("Choice: "))
                  continue
               if filter_input == 'p' or filter_input == 'P':
                  word = str(input("Search for what string? "))
                  print("")
                  print("Earthquakes:")
                  print("------------")
                  filtered_place = filter_by_place(res, word)
                  for each_list in filtered_place:
                     attribute = ' '.join(each_list).split()
                     place_holder = list(attribute[4:])
                     place = ' '.join(place_holder)
                     mag = float(attribute[0])
                     longitude = float(attribute[1])
                     latitude = float(attribute[2])
                     time = int(attribute[3])
                     print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
                  print("")
                  print("Options:")
                  print("  (s)ort")
                  print("  (f)ilter")
                  print("  (n)ew quakes")
                  print("  (q)uit")
                  print("")
                  user_input = str(input("Choice: "))
                  continue
         if sort_input == 'l' or sort_input == 'L':
            txt_file = open(filename, "r")
            lines = txt_file.readlines()
            res = []
            print("")
            print("Earthquakes:")
            print("------------")
            for line in lines:
               attribute = line.split()
               res.append(attribute)
            res.sort(key=lambda x: float(x[1]))
            for each_list in res:
               attribute = ' '.join(each_list).split()
               place_holder = list(attribute[4:])
               place = ' '.join(place_holder)
               mag = float(attribute[0])
               longitude = float(attribute[1])
               latitude = float(attribute[2])
               time = int(attribute[3])
               print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
            print("")
            print("Options:")
            print("  (s)ort")
            print("  (f)ilter")
            print("  (n)ew quakes")
            print("  (q)uit")
            print("")
            user_input = str(input("Choice: "))
            if user_input == 'f' or user_input == 'F':
               filter_input = str(input("Filter by (m)agnitude or (p)lace? "))
               if filter_input == 'm' or filter_input == 'M':
                  low = float(input("Lower bound: "))
                  high = float(input("Upper bound: "))
                  print("")
                  print("Earthquakes:")
                  print("------------")
                  filtered_mag = filter_by_mag(res, low, high)
                  for each_list in filtered_mag:
                     attribute = ' '.join(each_list).split()
                     place_holder = list(attribute[4:])
                     place = ' '.join(place_holder)
                     mag = float(attribute[0])
                     longitude = float(attribute[1])
                     latitude = float(attribute[2])
                     time = int(attribute[3])
                     print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
                  print("")
                  print("Options:")
                  print("  (s)ort")
                  print("  (f)ilter")
                  print("  (n)ew quakes")
                  print("  (q)uit")
                  print("")
                  user_input = str(input("Choice: "))
                  continue
               if filter_input == 'p' or filter_input == 'P':
                  word = str(input("Search for what string? "))
                  print("")
                  print("Earthquakes:")
                  print("------------")
                  filtered_place = filter_by_place(res, word)
                  for each_list in filtered_place:
                     attribute = ' '.join(each_list).split()
                     place_holder = list(attribute[4:])
                     place = ' '.join(place_holder)
                     mag = float(attribute[0])
                     longitude = float(attribute[1])
                     latitude = float(attribute[2])
                     time = int(attribute[3])
                     print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
                  print("")
                  print("Options:")
                  print("  (s)ort")
                  print("  (f)ilter")
                  print("  (n)ew quakes")
                  print("  (q)uit")
                  print("")
                  user_input = str(input("Choice: "))
                  continue                     
         if sort_input == 'a' or sort_input == 'A':
            txt_file = open(filename, "r")
            lines = txt_file.readlines()
            res = []
            print("")
            print("Earthquakes:")
            print("------------")
            for line in lines:
               attribute = line.split()
               res.append(attribute)
            res.sort(key=lambda x: float(x[2]))
            for each_list in res:
               attribute = ' '.join(each_list).split()
               place_holder = list(attribute[4:])
               place = ' '.join(place_holder)
               mag = float(attribute[0])
               longitude = float(attribute[1])
               latitude = float(attribute[2])
               time = int(attribute[3])
               print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
            print("")
            print("Options:")
            print("  (s)ort")
            print("  (f)ilter")
            print("  (n)ew quakes")
            print("  (q)uit")
            print("")
            user_input = str(input("Choice: "))
            if user_input == 'f' or user_input == 'F':
               filter_input = str(input("Filter by (m)agnitude or (p)lace? "))
               if filter_input == 'm' or filter_input == 'M':
                  low = float(input("Lower bound: "))
                  high = float(input("Upper bound: "))
                  print("")
                  print("Earthquakes:")
                  print("------------")
                  filtered_mag = filter_by_mag(res, low, high)
                  for each_list in filtered_mag:
                     attribute = ' '.join(each_list).split()
                     place_holder = list(attribute[4:])
                     place = ' '.join(place_holder)
                     mag = float(attribute[0])
                     longitude = float(attribute[1])
                     latitude = float(attribute[2])
                     time = int(attribute[3])
                     print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
                  print("")
                  print("Options:")
                  print("  (s)ort")
                  print("  (f)ilter")
                  print("  (n)ew quakes")
                  print("  (q)uit")
                  print("")
                  user_input = str(input("Choice: "))
                  continue
               if filter_input == 'p' or filter_input == 'P':
                  word = str(input("Search for what string? "))
                  print("")
                  print("Earthquakes:")
                  print("------------")
                  filtered_place = filter_by_place(res, word)
                  for each_list in filtered_place:
                     attribute = ' '.join(each_list).split()
                     place_holder = list(attribute[4:])
                     place = ' '.join(place_holder)
                     mag = float(attribute[0])
                     longitude = float(attribute[1])
                     latitude = float(attribute[2])
                     time = int(attribute[3])
                     print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
                  print("")
                  print("Options:")
                  print("  (s)ort")
                  print("  (f)ilter")
                  print("  (n)ew quakes")
                  print("  (q)uit")
                  print("")
                  user_input = str(input("Choice: "))                  
                  continue            
      if user_input == 'f' or user_input == 'F': 
         filter_input = str(input("Filter by (m)agnitude or (p)lace? "))
         if filter_input == 'm' or filter_input == 'M':
            low = float(input("Lower bound: "))
            high = float(input("Upper bound: "))
            print("")
            print("Earthquakes:")
            print("------------")
            #txt_file = open(filename, "r")
            #lines = txt_file.readlines()
            #res = []
            #for line in lines:
               #attribute = line.split()
               #res.append(attribute)
            filtered_mag = filter_by_mag(res, low, high)
            for each_list in filtered_mag:
               attribute = ' '.join(each_list).split()
               place_holder = list(attribute[4:])
               place = ' '.join(place_holder)
               mag = float(attribute[0])
               longitude = float(attribute[1])
               latitude = float(attribute[2])
               time = int(attribute[3])
               print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
            print("")
            print("Options:")
            print("  (s)ort")
            print("  (f)ilter")
            print("  (n)ew quakes")
            print("  (q)uit")
            print("")
            user_input = str(input("Choice: "))
            continue       
         if filter_input == 'p' or filter_input == 'P':   
            word = str(input("Search for what string? ")) 
            print("")
            print("Earthquakes:")
            print("------------")  
            #txt_file = open(filename, "r")
            #lines = txt_file.readlines()
            #res = []
            #for line in lines:
               #attribute = line.split()
               #res.append(attribute)
            filtered_place = filter_by_place(res, word)
            for each_list in filtered_place:
               attribute = ' '.join(each_list).split()
               place_holder = list(attribute[4:])
               place = ' '.join(place_holder)
               mag = float(attribute[0])
               longitude = float(attribute[1])
               latitude = float(attribute[2])
               time = int(attribute[3])               
               print("({:.2f})".format(mag), "{:>40s}".format(place), "at", time_to_str(time), "({:8.3f},".format(longitude), "{:.3f})".format(latitude))
            print("")
            print("Options:")
            print("  (s)ort")
            print("  (f)ilter")
            print("  (n)ew quakes")
            print("  (q)uit")
            print("")
            user_input = str(input("Choice: "))         
   txt_file = open(filename, "w") 
   for each_list in res:
      each_list[0] = float(each_list[0])
      final_res = ' '.join(str(x) for x in each_list)
      txt_file.write("{:s}\n".format(final_res))

#TODO: Required function - implement me!
def filter_by_mag(res, low, high):
   new_res = []
   for each_list in res:
      attribute = ' '.join(each_list).split()
      place_holder = list(attribute[4:])
      place = ' '.join(place_holder)
      mag = float(attribute[0])
      longitude = float(attribute[1])
      latitude = float(attribute[2])
      time = int(attribute[3]) 
      if mag >= low and mag <= high:
         new_res.append(attribute)
   return new_res 


# TODO: Required function - implement me!
def filter_by_place(res, word):
   new_res = []
   for each_list in res:
      attribute = ' '.join(each_list).split()
      place_holder = list(attribute[4:])
      place = ' '.join(place_holder) 
      mag = float(attribute[0])
      longitude = float(attribute[1])
      latitude = float(attribute[2])
      time = int(attribute[3]) 
      if word.lower() in place.lower():
         new_res.append(attribute)
   return new_res 


# TODO: Required function for final part - implement me too!
def quake_from_feature(feature):
   res = []
   index = 0
   for each_feature in feature:
      mag = feature[index]['properties']['mag']
      time = (feature[index]['properties']['time']) // 1000
      place = feature[index]['properties']['place']
      longitude = feature[index]['geometry']['coordinates'][0]
      latitude = feature[index]['geometry']['coordinates'][1]
      index += 1
      res.append("{:s} {:s} {:s} {:s} {:s}\n".format(str(mag), str(longitude), str(latitude), str(time), str(place)))
   return ''.join(res)
