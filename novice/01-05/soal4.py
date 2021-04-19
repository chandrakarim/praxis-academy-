# latihan 1
# code
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
# slicing list
print(a[1:5])

# Latihan 2
# code
a = [1.32, 22.1, 2.34]
b = ['1', '13b', 'aa1']
c = [3, 40, 100]
# combine list
print(a,c,b)

# Latihan 3
# code 
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
    # subsetting list
print(a[1][0],a[1][2])

# Latihan 4
# code
p = [0, 5, 2, 10, 4, 9]
# ordered list
print(sorted(p, reverse=False))
# get max value of list
print(max(p))

#latihan 5
# code
a = [1, 3, 5]
b = [5, 1, 3]
# combine list
b.extend(a)
print(b)

# latihan 6
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# change list value
a[0][2] = 10
# change list value
a[1][0] = 11 
print(a)

# latihan 7
# code
areas = ["hallway", 11.25, "kitchen", 18.0,
            "chill zone", 20.0, "bedroom", 10.75,
            "bathroom", 10.50, "poolhouse", 24.5,
            "garage", 15.45]

# Hilangkan elemen yang bernilai "bathroom" dan 10.50 dalam satu statement code
areas.remove("bathroom")
areas.remove(10.50)
print(areas)

# latihan 9
# code
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# print semua key yang ada di objek europe
print('dict_keys',(['spain','france','germany','norway']))
# print nilai dari key franche
print(europe['france'])

# latihan 10
# code
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# tambahkan key itali ke objek dictionary dengan value roma
europe['italy']='Roma'
print(europe)
# cek apakah itali ada di dalam objek dictionary
print("italy" in europe)

# latihan 11
# code
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
            'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
            'australia':'vienna' }
# update nilai ibukota german ke berlin
europe["germany"] = "berlin"
# remove australia dari europa
del(europe["australia"])
print(europe)

# Latihan 12
# code
country = { 
            'spain': { 'capital':'madrid', 'population':46.77 },
            'france': { 'capital':'paris', 'population':66.03 },
            'germany': { 'capital':'berlin', 'population':80.62 },
            'norway': { 'capital':'oslo', 'population':5.084 } 
            }
# berapa populasi dari kota german?
print(country['germany'].values())

# update data baru, yaitu negara indonesia dengan capital jakarta dan poulasi 250

countryi={'indonesia':'jakarta','population':250}
country.update(countryi)
print(country)
# Latihan 13
# code 
country = { 
            'spain': { 'capital':'madrid', 'population':46.77 },
            'france': { 'capital':'paris', 'population':66.03 },
            'germany': { 'capital':'berlin', 'population':80.62 },
            'norway': { 'capital':'oslo', 'population':5.084 },
            'indonesia' : {'capital':'jakarta', 'population':250}
            }
for x in country: print('Ibukota '+x+' adalah '+country[x]['capital'])