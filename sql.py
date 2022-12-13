SELECT * #모든 필드 조회
FROM data #데이터
WHERE data.id = 31; #조건


SELECT d.id #한 개 필드 조회
FROM data d #약자
WHERE (d.name IN ('A', 'B', 'C')) AND (d.num BETWEEN 10 AND 20); #다중 조건
              #포함 조건1                    #포함 조건2


SELECT d1.id AS 'ID' #필드 이름 지정
FROM data1 d1
JOIN data2 #두 테이블 합병
ON d1.id = d2.id; #합칠 기준 필드


SELECT count(name) #집계
FROM data
GROUP BY name; #그룹계산


SELECT *
FROM data
ORDER BY SUM(total) #정렬 (기본 : 오름, DESC : 내림)
LIMIT 4 OFFSET 10; #츌력 개수(10번째부터 4개만)


SELECT *
FROM data1 d1 JOIN data2 d2
ON d1.id = d2.id
WHERE d2.name isnull; #null인 지점만 출력

