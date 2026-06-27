''' Test cases:
6 https://cf.geekdo-images.com/imagepage/img/5lvEWGGTqWDFmJq_MaZvVD3sPuM=/fit-in/900x600/filters:no_upscale()/pic260745.jpg
10 cute_dog.jpg
6 turtle.jpg
'''
'''
Final means:
1 : (155.75275884055128, 113.44788856736476, 68.4198832703909) => 20389
2 : (202.10345204282282, 170.10345204282282, 121.78894472361809) => 9154
3 : (114.66537638789855, 75.27880207802791, 39.36121014566568) => 9817
4 : (243.64666359871146, 224.0891854578923, 187.1955821445007) => 10865
'''
#width (column) x height (row)
from math import sqrt
import PIL
from PIL import Image
import urllib.request
import io, sys, os, random

#need to fix move count

def choose_random_means(k, img, pix):
   m = []
   for i in range(k):
      m.append(pix[random.randint(0,img.size[0]-1),random.randint(0,img.size[1]-1)]) #pix[w,h]
   # if k == 3, return 3 tuples in a list. e.g. [(123, 0, 13), (32, 152, 255), (33, 56, 123)]
   return m

def check_move_count(mc):
   # mc is a list
   # if every single value in mc is 0, return True
   return True if mc.count(0) == len(mc) else False

def dist(color, m):
   # m is a list of pixels (list of means)
   # return the means bucket index of the minimum distance from the current color
   minIndex = 0
   distances = [-1 for mean in m]
   for i in range(len(distances)):
      distances[i] = sqrt((m[i][0] - color[0])**2 + (m[i][1] - color[1])**2 + (m[i][2] - color[2])**2)
   minIndex = distances.index(min(distances))
   #bfs?
   return minIndex 

def clustering(img, pix, cb, mc, m, count): #organize by bucket and moves
   #cb = count_buckets mc = move_counts m = random means
   width, height = img.size
   temp_pb, temp_mc, temp_m = [[] for x in m], [0 for x in m], []
   temp_cb = [0 for x in m]
   og_inds_dict = {}
   for w in range(width):
    for h in range(height):
      bucket_ind = dist(pix[w,h],m)
      temp_pb[bucket_ind].append(pix[w,h])
      temp_cb[bucket_ind] += 1
      og_inds_dict[pix[w,h]] = bucket_ind
   #pick new mean with temp_pb, check if index changes
   for pb in range(len(temp_pb)):
      red_sum = sum([r[0] for r in temp_pb[pb]])
      green_sum = sum([g[1] for g in temp_pb[pb]])
      blue_sum = sum([b[2] for b in temp_pb[pb]])
      pb_len = len(temp_pb[pb])
      if pb_len != 0:
         temp_m.append(((red_sum / pb_len),(green_sum / pb_len),(blue_sum / pb_len)))
      else:
         temp_m.append(m[pb])
   for w in range(width):
    for h in range(height):
      og_ind = og_inds_dict[pix[w,h]]
      new_ind = dist(pix[w,h],temp_m)
      if og_ind != new_ind and mc[og_ind] != 0:
         temp_mc[og_ind] -= 1
         temp_mc[new_ind] += 1
   return temp_cb, temp_mc, temp_m

def update_picture(img, pix, means):
   region_dict = {}
   for w in range(img.size[0]):
      for h in range(img.size[1]):
         ind = dist(pix[w,h], means)
         dec = means[ind]
         pix[w,h] = (int(dec[0]), int(dec[1]), int(dec[2]))
   return pix, region_dict
   
def distinct_pix_count(img, pix):
   colors = {}
   max_color, max_count = pix[0, 0], 0
   for c in range(img.size[0]):
      for r in range(img.size[1]):
         if pix[c,r] in colors:
            colors[pix[c,r]] += 1
            if colors[max_color] < colors[pix[c,r]]:
               max_color = pix[c,r]
               max_count = colors[max_color]
         else: colors[pix[c,r]] = 1
   #distinct, most common color, how much
   return len(colors.keys()), max_color, max_count

def fill_region_nums(img, pix, means):
   temp_mat = [[0 for col in range(img.size[1])] for row in range(img.size[0])]
   return []

def BFS(initial_pos, region_dict, colors, img):  
   visited = {initial_pos}
   frontier = [initial_pos]
   return visited
   
def count_regions(img, region_dict, pix, means):
   '''
   • Visited pixels = empty collection
   • Iterate through each pixel:
      o If point not in visited points:
         ▪ Run BFS on all adjacent pixels that are the same color
         ▪ Add these pixels to the visited pixels set and to the BFS queue
         ▪ Add 1 to your region counts list for that color
         • Return region counts list
   '''
   visited_point = set()
   color = (0, 0, 0)
   region_count = [0 for x in means]
   return region_count
 
def main():
   k = int(input("k: "))
   file = input("image file: ")
   if not os.path.isfile(file):
      file = io.BytesIO(urllib.request.urlopen(file).read())
   img = Image.open(file)
   img.show()
   pix = img.load()   # pix[0, 0] : (r, g, b) 
   c = 0
   for x in range(img.size[0]):
      for y in range(img.size[1]):
         if pix[x, y] == (255, 255, 255):
            c += 1
   print (img.size[0], img.size[1], c)
   print ('Size:', img.size[0], 'x', img.size[1])
   print ('Pixels:', img.size[0]*img.size[1])
   d_count, m_col, m_count = distinct_pix_count(img, pix)
   print ('Distinct pixel count:', d_count)
   print ('Most common pixel:', m_col, '=>', m_count)

   count_buckets = [0 for x in range(k)] #this is how many pixels belong to each mean
   move_count = [10 for x in range(k)] #this is how many that group hop
   means = choose_random_means(k, img, pix)
   print ('random means:', means)
   count = 1
   while not check_move_count(move_count):
      count += 1
      count_buckets, move_count, means = clustering(img, pix, count_buckets, move_count, means, count)
      print(f"count: {count} | {move_count}")
      if count == 2:
         print ('first means:', means)
         print ('starting sizes:', count_buckets)
   pix, region_dict = update_picture(img, pix, means)
   print ('Final sizes:', count_buckets)
   print ('Final means:')
   for i in range(len(means)):
      print (i+1, ':', means[i], '=>', count_buckets[i])

   '''
   Distinct regions:
      1: # of regions of means[0]
   Final regions:
      1: # of final regions of means[0] after taking care of step 3
   Save your file in the subdirectory, kmeans/userid.png
   '''
   img.show()
   
if __name__ == '__main__': 
   #print ((2, 3, 4) == (2, 3, 5))
   main()

   '''instructions:
   -randomize the points to have k random means (done)
   -cluster the remaining points to one of the random means by distance (BFS)
   -randomize k more random means from the cluster
   -repeat until there are no more changes'''