import gdal, osr
import numpy as np
import time

fn = 'gpw_v4_population_density_rev11_2020_30_sec.tif'
dt = np.float32
soft_nan = -3.4028230607370965e+38
np.set_printoptions(precision=8)
# np.set_printoptions(formatter={'int_kind': '{:,}'.format})

def raster2array(rasterfn,datatype):
    raster = gdal.Open(rasterfn)
    band = raster.GetRasterBand(1)
    array = band.ReadAsArray().astype(datatype)
    return array

print('begin np.sort timing')

two_d_array = raster2array(fn,dt)
print('shape of input array')
print(two_d_array.shape)
two_d_masked_array = np.ma.masked_values(two_d_array, soft_nan)
one_d_array = np.ma.compressed(two_d_masked_array)
size_of_array = one_d_array.shape[0]
print('size of array')
print(f"{size_of_array:,} items")
print('first item')
print(one_d_array[0])
print('median')
print(np.median(one_d_array))
print('last item')
print(one_d_array[size_of_array - 1])
print('\nstart sort')

tic = time.perf_counter()
one_d_array_sorted = np.sort(one_d_array, kind='quicksort')
toc = time.perf_counter()

print(f"sorted the array in {toc - tic:0.4f} seconds")
print('\nfirst item')
print(one_d_array_sorted[0])
print('middle item')
print(one_d_array_sorted[np.floor(size_of_array/2).astype(int)])
print('last item')
print(one_d_array_sorted[size_of_array - 1])

print('end np.sort timing')



