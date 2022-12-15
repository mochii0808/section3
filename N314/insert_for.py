# 1. 데이터가 리스트 형태인 경우

list_data = [
    ["AlbumId","Title","ArtistId"],
    [1,"For Those About To Rock We Salute You",1],
    [2,"Balls to the Wall",2]
]

for album in list_data[1:]: #2번째 행부터(필드명 제외)
    cur.execute("""
        INSERT INTO Albums_Part1 ('AlbumId', 'Title', 'ArtistId') 
        VALUES (?,?,?);
        """, 
        album #리스트 요소
    )

#-------------------------------------------------------------------

# 2. 데이터가 딕셔너리인 경우

dictionary_data = {
		"Columns":["AlbumId", "Title", "ArtistId"], #key : [val[0], val[1], val[2]]
		"1" : ["For Those About To Rock We Salute You",1], #key : [val[0], val[1]]
    	"2" : ["Balls to the Wall",2]
		}

for key, val in dictionary_data.items():
	if key == 'Columns': continue #Columns인 행은 아래 코드 건너뛰기(필드명 제외)
	cur.execute(
			"""
			INSERT INTO Albums_Part2 (AlbumId, Title, ArtistId)
			VALUES (?, ?, ?);""", 
			(int(key), val[0], val[1])	
	)

#--------------------------------------------------------------------

# 3. 리스트, 딕셔너리 결합

json_data = {
"DATA": [ #key : 리스트[dic1, dic2, ...]
	{
		"AlbumId" : 1,
		"Title" : "For Those About To Rock We Salute You",
		"ArtistId" : 1
	},
	{
		"AlbumId" : 2,
		"Title" : "Balls to the Wall",
		"ArtistId" : 2
	}
]}

for data in json_data['DATA']: #key가 'DATA'인 요소
	cur.execute("""
		INSERT INTO Albums_Part3 (AlbumId, Title, ArtistId)
		VALUES (?, ?, ?);""",
		(data['AlbumId'], data['Title'], data['ArtistId'])
	)