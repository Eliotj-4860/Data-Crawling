{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# blog url,title 크롤링"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "python version : 3.8.3 (64bit)\n",
    "\n",
    "Install module : pip install (selenium, tqdm, regex, times)\n",
    "\n",
    "necessary program : chromdriver, excel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import os\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "from bs4 import BeautifulSoup \n",
    "from selenium import webdriver\n",
    "import time\n",
    "import tqdm\n",
    "from tqdm.notebook import tqdm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. 찾고자 하는 키워드?챔스\n",
      "2. 조회를 시작하는 날짜?20200801\n",
      "3. 조회를 끝내는 날짜?20200806\n"
     ]
    }
   ],
   "source": [
    "query_txt = input(\"1. 찾고자 하는 키워드?\")\n",
    "start_date = input (\"2. 조회를 시작하는 날짜?\")\n",
    "end_date = input (\"3. 조회를 끝내는 날짜?\")\n",
    "# 1~3 에서 사용자가 찾고자 하는 키워드와 조회 날짜를 입력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = webdriver.Chrome(\"C:/Users/USER/Desktop/code/chromedriver\")\n",
    "# 현재 python을 실행하는 위치에 chromdriver를 함께 위치 시킬수 있도록 함 \n",
    "driver.get(\"https://www.naver.com/\")\n",
    "# 새로운 크롬창에서 검색을 할려는 사이트를 사용(현재는 네이버를 위주로 코드를 짰고 사이트 마다 사이트 elements가 다름)\n",
    "time.sleep(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "element = driver.find_element_by_id(\"query\")\n",
    "element.send_keys(query_txt)\n",
    "element.submit()\n",
    "# 사이트 element에서 id를 통해서 앞서 설정한 검색어를 검색하여 입력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.find_element_by_link_text('블로그').click()\n",
    "# 크롤링할 사이트를 text('')안에 입력 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.find_element_by_id(\"_search_option_btn\").click()\n",
    "# 네이버 사이트에 한해서 검색 옵션 버튼 클릭 (날짜 조회창이 검새 옵션 안에 있어서)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.find_element_by_xpath(\"\"\"//*[@id=\"snb\"]/div/ul/li[1]/a\"\"\").click()\n",
    "driver.find_element_by_xpath(\"\"\"//*[@id=\"snb\"]/div/ul/li[1]/div/ul/li[1]/a\"\"\").click()\n",
    "# 사이트의 copy.xpath를 사용하여 정렬버튼의 xpath 클릭 및 관련도순 xpath 클릭"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.find_element_by_xpath(\"\"\"//*[@id=\"snb\"]/div/ul/li[2]/a\"\"\").click()\n",
    "time.sleep(2)\n",
    "# 기간 카테고리 클릭"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "s_date = driver.find_element_by_xpath(\"\"\"//*[@id=\"blog_input_period_begin\"]\"\"\")\n",
    "#블로그 말고 다른 키워드를 사용 할시에는 @id=\"blog_input_period_begin 에서 blog 대신 다른 키워드를 넣어주면 된다\n",
    "driver.find_element_by_xpath(\"\"\"//*[@id=\"blog_input_period_begin\"]\"\"\").click()\n",
    "# 기존에 작성되어 있던 날짜를 제거하고 앞서 언급한 날짜를 입력할수 있게 준비함\n",
    "s_date.clear()\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "for c in start_date:\n",
    "    s_date.send_keys(c)\n",
    "    time.sleep(0.1)\n",
    "# for 반복문이 실행 될때 마다 1 글자씩 입력하는 부분입니다.\n",
    "# ex 코드 실행시 20200701 을 0.1초마다 한 글자씩 입력된다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.find_element_by_class_name(\"tx\").click()\n",
    "# 날짜 입력 버튼 적용 하기 클릭됨 \"tx\"는 적용하기 버튼의 element\n",
    "time.sleep(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4a37e967143f4ead8b53ee89f2641601",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(FloatProgress(value=0.0, max=10.0), HTML(value='')))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[맨시티:레알, 챔스 16강 2차전 프리뷰] 핵심자원 빠진 레알, 공격이 절실한 지단의 묘수는? 맨시티는 여유롭지만 레알의 챔스 DNA가 신경쓰인다\n",
      "EPL 2019/2020 시즌 종료! 유로파 진출권 챔스진출권 결정완료!\n",
      "15-16 레알마드리드 써드/반팔/챔스버전/7.Ronaldo\n",
      "8월 챔스-유로파리그 일정, 어디서 어떻게 열리나\n",
      "레알 마드리드ㆍ스페인 '레전드 GK' 이케르 카시야스, 현역 은퇴! UEFA 챔스 3회ㆍ스페인 라리가 5회 등 우승! 레알 마드리드서만 16년간 725경기 출전!\n",
      "EPL 2020-2021시즌 개막은 언제일까? / 2019-2020 UEFA 챔스 8강 대진표!\n",
      "주말부터는 챔스 리뷰 갑니다\n",
      "[EPL 결산Ⅰ]EPL 챔스 진출, 유로파 진출, 강등은 누가?\n",
      "쿠키런 챔스 키위맛3 아레나1 2 3 조합\n",
      "FA컵에서 강한 빅6중한팀 아스날 이제 빅6라부르기도 민망해졌지만 아르테타감독의 FA컵우승경험이 큰도움이되었다~ 주장 오바메양 맹활약!!!! 이로써 챔스 유로파팀 결정되었다~\n",
      "피파온라인4 - 패키지에서 챔스 금카가 나오긴하는데..\n",
      "< 멤버집에 와서 축구보라고?ㅎㅎ > 월드컵 본선 한번 나가본 적 없으면서, 챔스경기엔 개열광ㅎ by 불방망이\n",
      "[UCL] 챔스 16강 2차전 프리뷰! 맨시티 v 레알 마드리드    (세르히오 와 세르히오가 없다..)\n",
      "챔스리그와 유로파 한달 안에 끝낸다\n",
      "이해찬 손민수 후기. 그대는 본챔스 광인.\n",
      "2020 롤챔스 서머 33일차 [한화생명 vs 담원] [T1 vs 샌드박스]\n",
      "[유럽여행] <2>런던여행 1일차 : 토트넘 직관후기(토트넘 올림피아코스 챔스), 손흥민 직관!\n",
      "이번 바르샤 챔스\n",
      "본챔스모자 인기상품Best\n",
      "롤챔스야식추천 | 농심 앵그리 짜파구리 후기 칼로리 꿀조합 추천\n",
      "[피파온라인4] 19/20시즌 챔피언스리그 재개됩니다! 챔피언스리그 일정 / 19UCL 클래스에도 라이브 퍼포먼스 적용? (feat. 19챔스, 19챔스시즌, 라부)\n",
      "'차기 시즌 챔스 진출' 맨체스터 유나이티드는 여름 이적시장을 어떻게 보내고 있을까? / 제이든 산초, 파우 토레스, 가브리엘 마갈레스 영입설 / 알렉시스 산체스 인테르행?\n",
      "유튜브 여자친구 예린 화이트 반팔티_본챔스(BORN CHAMPS)\n",
      "챔스 재개 5일전\n",
      "마크 손민수 (본챔스 백팩)\n",
      "챔스 ost, Theme\n",
      "2020 롤챔스 서머 32일차 [젠지 vs 설해원] [DRX vs 아프리카]\n",
      "\n",
      "[유벤투스-리옹 CL 16강 2차전 프리뷰] 기동력과 압박으로 측면봉쇄 노리는 리옹과 다득점에 부담 가중되는 유벤투스\n",
      "\n",
      "[잉글랜드 FA컵 결승 끝장 프리뷰] 아스날 vs 첼시 _토끼와 거북이의 외나무 다리 승부\n",
      "\n",
      "\n",
      "\n",
      "리버풀 여름 이적시장-티아고는 멀어지고 자말 루이스와 가까워졌다\n",
      "[검토현황] 세비야 AS로마, 레버쿠젠 레인저스 8월7일 유로파리그\n",
      "\n",
      "\n",
      "\n",
      "FA컵 결승 아스날 v 첼시 프리뷰, 런던더비로 역대급 결승전이 펼쳐진다\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "[문제해결] 바젤 프랑크푸르트, 울버햄튼 올림피아코스 유로파리그 8월7일\n",
      "\n",
      "\n",
      "[문제해결] 세비야 AS로마, 레버쿠젠 레인저스 유로파리그 8월7일\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "솔샤르 맨유를 재건하다 - 맨유, 사상 초유의 리그 전승우승에 성공하다(69)\n",
      "[김콜러]FM2020 자유계약 로스터 - 레알 마드리드 전설의 시작 #5 (새로운 도전)\n",
      "\n",
      "울버햄튼 올림피아코스 ] 유로파리그 정확분석글] 전력도 중요하지만 1차전상황도 생각해야한다.\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "[UEFA 유로파리그] 8월6일 _ 맨체스터유나이티드 VS LASK린츠 _ 해외축구경기\n",
      "\n",
      "\n",
      "\n",
      "30년 만의 리그 우승! 공홈에서 산 19-20 프리미어리그 우승 헨더슨 마킹 클럽월드컵 패치 리버풀 유니폼 리뷰\n",
      "잉글랜드 FA컵 결승 아스날 첼시 중계 런던더비 아르테타 램파드 맞대결 첼시 아스날 프리뷰(feat. 토트넘 유로파리그 플레이오프 여부는?!)\n",
      "\n",
      "\n",
      "\n",
      "뒤늦은 아스날 FA컵 우승과 유로파 본선 진출! 토트넘은 예선부터... 하루만에 바뀐 북런던의 주인\n",
      "\n",
      "\n",
      "\n",
      "울버햄튼 올림피아코스 바젤 프랑크푸르트 [8월7일 UEL 최종예상]\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "(유로파리그 일정) 맨체스터 유나이티드 FC vs LASK 린츠 (2020년 8월 6일)\n",
      "오피셜)레알 마드리드 레전드 골키퍼인 카시야스가 39세의 나이로 은퇴선언\n",
      "2019-2020 이탈리아 세리에 A 최종 라운드 결과 : 임모빌레의 득점왕 등극과 제노아 잔류 성공, 도움왕은 라치오의 루이스 알베르토\n",
      "\n",
      "[국내 배송 진행 ♥ 바르셀로나, 레알 마드리드, PSG, 바이에른 뮌헨, 인터밀란] 바르셀로나 9899 리메이크 유니폼, PSG 조던 드릴탑, 레알 프레젠테이션 자켓,\n",
      "\n",
      "챔피언스리그 16강 2차전 맨시티, 첼시 @일산축구 @일산epl @일산챔피언스리그\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "url_list = []\n",
    "title_list = []\n",
    "total_page = 10\n",
    "# 총 10페이지의 블로그의 url, title을 저장하기 위해서 사용\n",
    "\n",
    "for i in tqdm(range(0, total_page)):\n",
    "    i = i*10+1\n",
    "    # tqdm은 현재 진행된 정도를 시각화 하기 위해서 사용 하기에 필요 없는경우는 제거 해도 된다.\n",
    "    # 11, 21, 31로 증가 되는데 이는 url의 고유 html의 페이지 변경에 관한것이기에 건드리지 않는다\n",
    "    # 만일 다른 브라우저를 쓴다면 페이지 1번과 페이지 2번의 url을 확인해보고 맨 뒤에 오는 숫자를 확인해서 for문 구성\n",
    "    \n",
    "    url = \"https://search.naver.com/search.naver\\\n",
    "?date_from={0}&date_option=8&date_to={1}\\\n",
    "&dup_remove=1&nso=p%3Afrom{2}to{3}post_blogurl=\\\n",
    "&post_blogurl_without=&query={4}&sm=tab_pge&srchby=all&st=sim&where=post&start={5}\".format(start_date,end_date,start_date,end_date,query_txt, i)\n",
    "    # url 내의 주소는 블로그내의 글 들의 url 주소이기에 다른것으로 변경 할 필요 없다.\n",
    "       \n",
    "    driver.get(url)\n",
    "    time.sleep(0.5)\n",
    "    \n",
    "    titles = \"a.sh_blog_title._sp_each_url._sp_each_title\"\n",
    "    # 블로그 메인 화면의 제목을 f12 눌렀을때 나오는 것으로 사용 . 만일 이때 글자와 글자 사이가 띄어있을경우 코드 내에서는 마침표로 대체함\n",
    "    \n",
    "    article_raw = driver.find_elements_by_css_selector(titles)\n",
    "    \n",
    "    for article in article_raw:\n",
    "        url = article.get_attribute('href')\n",
    "        url_list.append(url)\n",
    "    # url을 크롤링 시작해서 url_list에 저장\n",
    "\n",
    "    for article in article_raw:\n",
    "        title = article.get_attribute('title')\n",
    "        title_list.append(title)\n",
    "    # 제목을 크롤링 시작해서 title_list에 저장\n",
    "        print(title)\n",
    "     # 크롤링한 글들의 제목을 확인할 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "url갯수:  100\n",
      "title갯수:  100\n"
     ]
    }
   ],
   "source": [
    "print('url갯수: ', len(url_list))\n",
    "print('title갯수: ', len(title_list))\n",
    "\n",
    "df = pd.DataFrame({'url':url_list, 'title':title_list})\n",
    "# url과 title을 이용하여 DataFrame을 작성\n",
    "\n",
    "df.to_excel(\"blog.xlsx\")\n",
    "# blog_url이라는 파일을 xlsx 형식으로 저장"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
