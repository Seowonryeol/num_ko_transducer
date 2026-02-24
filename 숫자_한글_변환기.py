"""
Docstring for 숫자_한글_변환기
십진수 숫자를 입력했을 때 이를 한글 발음으로 변환하여 출력해주는 코드
ex) 3 -> 삼, 43 -> 사십삼, 1211 ->천이백십일
편의상 억 단위까지만 사용가능 - 9999억 9999만 9999 ~ + 9999억 9999만 9999

"""


num_to_ko_table={1:"일",2:"이",3:"삼",4:"사",5:"오",6:"육",7:"칠",8:"팔",9:"구"}

def num_to_ko (num:int) -> str :
  #각각 억, 만, 그리고 이 아래 단위 부분의 값을 의미 ex 1234억 5678만 9012 -> millions_part=1234, thousands_part=5678, hundreds_part=9012
  
  #0이거나 마이너스일 경우
  if(num==0): return "영"
  if(num<0): 
    num=-num
    is_minus=True
  else:
    is_minus=False
  
  millions_part= num//100000000
  thousands_part= (num//10000)%10000
  hundreds_part=num%10000

  #각 자리별 숫자값들과 변환된 한글 문자열이 들어간 딕셔너리 자료형
  part_values_and_strs={"millions_part": [millions_part,""], "thousands_part":[thousands_part,""], "hundreds_part":[hundreds_part,""]} 

  for part in part_values_and_strs.values(): #각 부분별로 각자리의 값을 구하고 한글 변환 후 단위 추가
      thousand_value=part[0]//1000 
      hundred_value=(part[0]//100)%10 
      ten_value=(part[0]//10)%10 
      one_value=part[0]%10

      if thousand_value !=0 :
        part[1]+=num_to_ko_table[thousand_value]+"천"
      if hundred_value !=0 :
        part[1]+=num_to_ko_table[hundred_value]+"백"
      if ten_value !=0 :
        part[1]+=num_to_ko_table[ten_value]+"십"
      if one_value !=0 :
        part[1]+=num_to_ko_table[one_value]

  if part_values_and_strs["millions_part"][1]!="":
    part_values_and_strs["millions_part"][1]+="억"
  if part_values_and_strs["thousands_part"][1]!="":
    part_values_and_strs["thousands_part"][1]+="만"
  if is_minus : part_values_and_strs["millions_part"][1]="마이너스 " +part_values_and_strs["millions_part"][1]
  return part_values_and_strs["millions_part"][1] + " "+ part_values_and_strs["thousands_part"][1]+ " " + part_values_and_strs["hundreds_part"][1]

while(1):
  num=int(input("한글 변환을 원하는 숫자를 입력하세요 : "))
  ko_num=num_to_ko(num)

  print(f"{num}을 한글변환한 결과는 {ko_num}입니다. 프로그램 종료를 원하시면 Ctrl+C를 눌러주세요. ")