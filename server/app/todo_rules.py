from __future__ import annotations

from typing import Iterable

from .schemas import TodoItem


RULES: list[tuple[Iterable[str], str]] = [
    (["전시회", "갤러리"], "전시회 일정 잡기"),
    (["영화", "극장"], "같이 영화 보기"),
    (["여행", "놀러", "휴가"], "여행 일정 정리하기"),
    (["맛집", "식당", "밥"], "맛집 찾아보기"),
    (["카페", "커피"], "카페 데이트 계획하기"),
    (["운동", "헬스", "산책"], "함께 운동/산책하기"),
    (["공연", "콘서트"], "공연 예매하기"),
    (["사진", "촬영"], "데이트 사진 찍기"),
    (["꽃", "플라워"], "꽃 선물 준비하기"),
    (["선물", "기념일"], "기념일 선물 준비하기"),
    (["요리", "집밥"], "집에서 요리하기"),
    (["캠핑", "글램핑"], "캠핑 예약하기"),
    (["도서관", "책"], "같이 책 읽기"),
    (["드라이브", "차"], "드라이브 코스 정하기"),
    (["쇼핑", "백화점"], "쇼핑 일정 잡기"),
    (["공원", "피크닉"], "공원 피크닉 준비하기"),
    (["게임", "보드게임"], "보드게임 카페 가기"),
    (["뮤지컬", "연극"], "뮤지컬/연극 예매하기"),
    (["동물원", "수족관"], "동물원/수족관 방문하기"),
    (["야경", "전망대"], "야경 명소 가보기"),
]


def extract_todos(raw_text: str) -> list[TodoItem]:
    normalized = raw_text.lower()
    todos: list[TodoItem] = []
    for keywords, title in RULES:
        if any(keyword in normalized for keyword in keywords):
            todos.append(TodoItem(title=title))
    return todos
