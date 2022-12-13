SELECT CustomerId , UPPER(City) ||' '|| UPPER(Country)                 
FROM customers c;   #대문자     #문자 합치기(가운데 공백)


SELECT SUBSTRING(FirstName, 1 ,4) #글자 제한(1번째부터 4번째까지)
FROM customers c;


SELECT EmployeeId
FROM employees e
WHERE (DATE(HireDate) - date(2020-01-01))/365 > 7
      #날짜(DATE, DATETIME)


SELECT t.Name
FROM tracks t ,
	(
	SELECT *
	FROM albums a
	WHERE a.Title IN ('Unplugged', 'Outbreak')
	) a1
    #subquery : 이중 쿼리문
WHERE t.AlbumId = a1.AlbumId;


SELECT s.teacher_id, s.student_id, ROWID
FROM Student s;                    #ROWID : 인덱스


SELECT s.teacher_id, s.student_id,
ROW_NUMBER() OVER(PARTITION BY teacher_id ORDER BY teacher_id)
#ROW_NUMBER() OVER(PARTITION BY 그룹핑 필드 ORDER BY 정렬 필드)
    # => 그룹핑 한 후 순번매기기(한 세트)
FROM Student s;


SELECT *
FROM Student s
ORDER BY ROWID
LIMIT 1 OFFSET (SELECT count(*) FROM Student)/2; #중앙값 위치 출력
                #전체 레코드 수 / 2
